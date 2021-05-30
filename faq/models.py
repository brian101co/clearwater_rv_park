from django.db import models

from streams import blocks

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

class FAQPage(Page):
    page_title = models.TextField(
        max_length=300,
        help_text="Title of the page as the public would see it."
    )
    main_content = StreamField([
        ("Question", blocks.FAQBlock()),
    ])
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        StreamFieldPanel("main_content"),
    ]

