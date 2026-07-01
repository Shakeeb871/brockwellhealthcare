from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_list, name="list"),
    # A single flat route: the slug resolves to a category or a post.
    path("<slug:slug>/", views.blog_entry, name="entry"),
]
