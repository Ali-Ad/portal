from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel
from wagtail.core.fields import StreamField


class FooterPageOrder(Orderable):
    page = ParentalKey("footer.FooterPage", related_name="footer_order")
    title = models.CharField(max_length=40, blank=False, null=True)
    internal_url = models.ForeignKey("wagtailcore.Page", null=True, blank=True, on_delete=models.CASCADE,
                                     related_name="+")
    external_url = models.URLField(blank=True, null=True)


class FooterPage(Page):
    template = "footer/footer_page.html"
    max_count = 1

    content_panels = Page.content_panels + [
        InlinePanel("footer_order"),
    ]

    class Meta:
        verbose_name = "Footer Page"
        verbose_name_plural = "Footer Pages"
