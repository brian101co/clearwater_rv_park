from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class AboutPage(Page):
    our_mission_text = models.TextField(
        max_length=300,
        help_text="Our Mission Text"
    )
    main_content = models.TextField(
        help_text="Main Content of the about page.",
    )
    content_panels = Page.content_panels + [
        FieldPanel("our_mission_text"),
        FieldPanel("main_content"),
    ]

