from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from . import blocks

class HeaderPage(Page):
    template = "header/header_page.html"
    max_count = 1

    content = StreamField([
        ("headr", blocks.HeaderBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel("content")
    ]

    class Meta:
        verbose_name = "Header Page"
        verbose_name_plural = "Header Page"
