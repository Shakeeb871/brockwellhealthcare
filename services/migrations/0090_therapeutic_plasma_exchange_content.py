"""Create a new Therapeutic Plasma Exchange (plasmapheresis) service under the
Longevity | Healthspan category (level-2, so it appears in that category's nav
dropdown). Honest, narrative copy that separates the established medical use from
the investigational longevity use, with a 5-item FAQ. Images added later."""

from django.db import migrations

SLUG = "therapeutic-plasma-exchange"
NAME = "Therapeutic Plasma Exchange"
ICON = "plasma"

SEO_TITLE = "Therapeutic Plasma Exchange in Dubai | Plasmapheresis | Brockwell Healthcare"
SEO_DESCRIPTION = (
    "Therapeutic plasma exchange (plasmapheresis) in Dubai at Brockwell Healthcare. An "
    "honest, medically grounded look at an established procedure now being explored for "
    "longevity."
)
HERO_HEADING = "Therapeutic plasma exchange in Dubai"
SUMMARY = (
    "An established medical procedure, plasmapheresis, now being explored for longevity, "
    "presented with an honest line between what is proven and what is investigational."
)

DESCRIPTION = """
<p>Therapeutic plasma exchange is one of the more interesting treatments in longevity medicine, partly because it is not new at all. Doctors have used it for decades to treat serious illness, and only recently has it drawn attention as a possible way to clear out the ageing signals that accumulate in the blood. At Brockwell Healthcare we discuss therapeutic plasma exchange in Dubai with a clear line drawn between what it is proven to do and what is still being investigated, because that distinction is the most honest and useful thing we can offer.</p>

<h2>What is therapeutic plasma exchange?</h2>
<p>Therapeutic plasma exchange, also called plasmapheresis, is a procedure that removes a portion of the plasma, the liquid part of your blood, and replaces it with a substitute fluid. Plasma is the fraction that carries proteins, antibodies and a great deal else besides your blood cells, and the point of the treatment is to take away a volume of that fluid, along with whatever unwanted material it contains, and top the volume back up with a clean replacement.</p>

<h2>How it works</h2>
<p>The mechanics are well established because medicine has done this for years. Your blood is drawn from a vein and passed through an apheresis machine, which spins it to separate the plasma from the red cells, white cells and platelets. The cellular part of your blood is returned to you straight away, while a measured volume of plasma, often somewhere around two litres, is discarded and replaced with a solution of albumin, a natural blood protein, mixed with saline. A full session usually takes somewhere between two and three hours, and it is done under medical supervision with your observations monitored throughout.</p>

<h2>The longevity idea, and where it comes from</h2>
<p>This is the genuinely novel part, and it rests on a neat piece of science. For years the interest in "young blood" assumed the benefit came from adding youthful factors. Then work from the Conboy laboratory at Berkeley suggested something different, that much of the effect in mice came from removing and diluting old plasma, not from adding anything young at all. In their experiments, simply replacing a portion of an old animal's plasma with a plain albumin solution produced signs of rejuvenation in muscle, liver and brain tissue. That reframed the whole idea. If ageing is driven partly by a build-up of pro-ageing and inflammatory signals in the blood, then clearing some of them out might help, and plasma exchange is the established way to do exactly that in people.</p>

<h2>Established medicine and investigational longevity, kept separate</h2>
<p>Here is the line we will not blur. As a treatment for disease, therapeutic plasma exchange is thoroughly established, used for years in conditions such as Guillain-Barre syndrome, myasthenia gravis and certain autoimmune and neurological disorders, with a well-understood safety profile. As a longevity treatment, it is investigational. Early human studies have measured changes in inflammatory markers and biological-age estimates, and the results are interesting, but the human longevity evidence is still small, early and far from settled. We present the disease use as established and the longevity use as promising research, and anyone who tells you plasma exchange is a proven way to reverse ageing is going beyond what the science currently supports.</p>

<h2>What a session involves, and who it is for</h2>
<p>A session is a calm, monitored procedure, not anything dramatic. You are seated or reclined while blood is drawn, processed and returned continuously over a couple of hours, and most people tolerate it well, with side effects usually mild and related to fluid shifts or the access line. It is set aside where there are certain heart, clotting or infection concerns, and it is never appropriate without a thorough assessment first. It suits people who are genuinely informed about its investigational status in longevity and who want to explore it within a wider, well-supervised plan, and it is not a shortcut around the fundamentals of health.</p>

<h2>An honest word before you consider it</h2>
<p>Because this treatment sits where real science meets real hype, we say the quiet part plainly. The mechanism is sound, the procedure is safe in trained hands, and the early research is worth taking seriously, but none of that is the same as proof that it will extend your healthy years. We would rather you understood exactly where the evidence stands, and decided with clear eyes, than be sold a promise the field has not earned yet.</p>
"""

FAQS = [
    ("What is therapeutic plasma exchange?",
     "Therapeutic plasma exchange, or plasmapheresis, removes a portion of your blood plasma and replaces it with a solution of albumin and saline. A machine separates the plasma from your blood cells, which are returned to you, while the removed plasma and whatever it carries is discarded."),
    ("How does it work for longevity?",
     "The idea, from research led by the Conboy laboratory, is that ageing is driven partly by a build-up of inflammatory and pro-ageing signals in the blood, and that removing and diluting old plasma may help. In animal studies this produced signs of rejuvenation, and human longevity research is now exploring it, though the evidence is still early."),
    ("Is it a proven anti-ageing treatment?",
     "No. It is a well-established procedure for treating certain diseases, but its use for longevity is investigational. Early human data on inflammatory and biological-age markers is promising but small and unsettled, and it should not be presented as a proven way to reverse ageing."),
    ("Is therapeutic plasma exchange safe?",
     "As a medical procedure it has a well-characterised safety profile from decades of use, and it is performed under supervision with monitoring throughout. Side effects are usually mild, and a thorough assessment first is what confirms it is appropriate for you."),
    ("How long does a session take?",
     "Usually between two and three hours, during which blood is continuously drawn, separated, and returned while a measured volume of plasma is replaced with albumin and saline."),
]


def load_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")

    cat = ServiceCategory.objects.filter(region="uae", slug="longevity-healthspan").first()
    if not cat:
        return

    last = (
        Service.objects.filter(region="uae", category=cat, parent__isnull=True)
        .order_by("-order")
        .first()
    )
    next_order = (last.order + 1) if last else 1

    svc, _ = Service.objects.update_or_create(
        region="uae", slug=SLUG,
        defaults=dict(
            category=cat,
            parent=None,
            name=NAME,
            hero_heading=HERO_HEADING,
            icon=ICON,
            summary=SUMMARY,
            description=DESCRIPTION.strip(),
            benefits="",
            seo_title=SEO_TITLE,
            seo_description=SEO_DESCRIPTION,
            order=next_order,
            is_published=True,
        ),
    )

    ct, _ = ContentType.objects.get_or_create(app_label="services", model="service")
    FAQItem.objects.filter(content_type=ct, object_id=svc.id).delete()
    for i, (question, answer) in enumerate(FAQS):
        FAQItem.objects.create(
            content_type=ct, object_id=svc.id,
            question=question, answer=answer, order=i, is_published=True,
        )


def remove_content(apps, schema_editor):
    Service = apps.get_model("services", "Service")
    FAQItem = apps.get_model("core", "FAQItem")
    ContentType = apps.get_model("contenttypes", "ContentType")
    svc = Service.objects.filter(region="uae", slug=SLUG).first()
    if svc:
        ct, _ = ContentType.objects.get_or_create(app_label="services", model="service")
        FAQItem.objects.filter(content_type=ct, object_id=svc.id).delete()
        svc.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0089_stress_management_content_v2"),
        ("core", "0004_page_custom_head_faqitem"),
    ]

    operations = [migrations.RunPython(load_content, remove_content)]
