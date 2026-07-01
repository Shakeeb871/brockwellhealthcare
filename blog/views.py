from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from core import seo
from core.regions import region_path

from .models import BlogCategory, BlogPost

PER_PAGE = 9


def _sidebar(code):
    return {
        "categories": BlogCategory.objects.filter(region=code, is_published=True),
        "recent_posts": BlogPost.objects.filter(region=code, is_published=True)[:4],
    }


def _paginate(request, qs):
    return Paginator(qs, PER_PAGE).get_page(request.GET.get("page"))


def blog_list(request):
    region = request.region
    code = region["code"]
    posts = BlogPost.objects.filter(region=code, is_published=True).select_related("category")
    page_obj = _paginate(request, posts)

    meta = seo.build_meta(
        request,
        title=f"Insights & Articles | {settings.BRAND_NAME}",
        description=(
            f"Expert insights on regenerative medicine, stem cell therapy, longevity and "
            f"patient care from {settings.BRAND_NAME} in {region['name']}."
        ),
        path="/blog/",
    )
    crumbs = seo.breadcrumb_schema(
        [
            ("Home", seo.absolute(region_path(code, "core:home"))),
            ("Insights", meta["canonical"]),
        ]
    )
    return render(
        request,
        "blog/list.html",
        {
            "meta": meta, "jsonld": [crumbs], "page_obj": page_obj,
            "posts": page_obj.object_list, "active_category": None, **_sidebar(code),
        },
    )


def blog_entry(request, slug):
    """A flat /blog/<slug>/ route — resolves to a category page or a post."""
    region = request.region
    code = region["code"]
    category = BlogCategory.objects.filter(region=code, slug=slug, is_published=True).first()
    if category is not None:
        return _render_category(request, region, category)
    post = get_object_or_404(
        BlogPost.objects.select_related("category"), region=code, slug=slug, is_published=True
    )
    return _render_post(request, region, post)


def _render_category(request, region, category):
    code = region["code"]
    posts = category.published_posts.select_related("category")
    page_obj = _paginate(request, posts)

    meta = seo.build_meta(
        request,
        title=f"{category.name} — Insights | {settings.BRAND_NAME}",
        description=category.description or f"{category.name} articles from {settings.BRAND_NAME}.",
        path=f"/blog/{category.slug}/",
    )
    crumbs = seo.breadcrumb_schema(
        [
            ("Home", seo.absolute(region_path(code, "core:home"))),
            ("Insights", seo.absolute(region_path(code, "blog:list"))),
            (category.name, meta["canonical"]),
        ]
    )
    return render(
        request,
        "blog/list.html",
        {
            "meta": meta, "jsonld": [crumbs], "page_obj": page_obj,
            "posts": page_obj.object_list, "active_category": category, **_sidebar(code),
        },
    )


def _render_post(request, region, post):
    code = region["code"]
    related = (
        BlogPost.objects.filter(region=code, is_published=True, category=post.category)
        .exclude(pk=post.pk)[:3]
        if post.category_id else BlogPost.objects.none()
    )

    meta = seo.build_meta(
        request,
        title=post.seo_title or post.title,
        description=post.seo_description or post.excerpt,
        path=f"/blog/{post.slug}/",
        og_type="article",
    )
    if post.image:
        meta["image"] = seo.absolute(post.image.url)

    crumbs = [("Home", seo.absolute(region_path(code, "core:home"))),
              ("Insights", seo.absolute(region_path(code, "blog:list")))]
    if post.category_id:
        crumbs.append((post.category.name, seo.absolute(region_path(code, "blog:entry", slug=post.category.slug))))
    crumbs.append((post.title, meta["canonical"]))

    jsonld = [seo.article_schema(post, region), seo.breadcrumb_schema(crumbs)]
    faqs = list(post.faqs.filter(is_published=True))
    faq_ld = seo.faq_schema(faqs)
    if faq_ld:
        jsonld.append(faq_ld)
    return render(
        request,
        "blog/detail.html",
        {"meta": meta, "jsonld": jsonld, "post": post, "related": related, "faqs": faqs, **_sidebar(code)},
    )
