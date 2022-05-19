from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from header.models import HeaderPage
from footer.models import FooterPageOrder


class HomePage(Page):
    template = "home/home_page.html"
    # discreption = models.TextField(max_length=20, null=False)
    max_count = 1
    content_panels = Page.content_panels + [
        # StreamFieldPanel("sub")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = HeaderPage.objects.live().public()
        context["footers"] = FooterPageOrder.objects.all()
        return context

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
