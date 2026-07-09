"""Follow-up to 0117: the BlogPost and Event ``title`` fields were not re-adapted,
so a stray city could remain in an event/blog headline. Re-adapt those titles from
the UAE source, location-light (no city, no country mention in a headline)."""

import re

from django.db import migrations

_SUBS = [
    (re.compile(r"\s*[—-]\s*Dubai\b"), ""),   # "… — Dubai" tail in event titles
    (re.compile(r"\bin Dubai\b"), ""),
    (re.compile(r"Dubai['’]s"), "our"),
    (re.compile(r"\bDubai\b"), ""),
    (re.compile(r"\bthe UAE\b"), "the country"),
    (re.compile(r"\bUAE\b"), "the US"),
    (re.compile(r"[ \t]{2,}"), " "),
]


def adapt_title(text):
    if not text:
        return text
    for rx, rep in _SUBS:
        text = rx.sub(rep, text)
    return text.strip()


def relight_titles(apps, schema_editor):
    BlogPost = apps.get_model("blog", "BlogPost")
    Event = apps.get_model("events", "Event")
    for Model in (BlogPost, Event):
        for us in Model.objects.filter(region="us"):
            src = Model.objects.filter(region="uae", slug=us.slug).first()
            if src and isinstance(src.title, str):
                new = adapt_title(src.title)
                if new != us.title:
                    us.title = new
                    us.save(update_fields=["title"])


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0117_us_location_light"),
    ]

    operations = [migrations.RunPython(relight_titles, migrations.RunPython.noop)]
