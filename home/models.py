from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

class HomePage(Page):
    hero_section_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Main Text displayed in the hero section over the background video."
    )

    hero_section_subtitle_text = models.TextField(
        max_length=350,
        blank=True,
        help_text="Subtitle Text displayed in the hero section over the background video."
    )

    cta_button_text = models.CharField(
        max_length=20,
        blank=True,
        default="Learn More",
        help_text="Call-To-Action Button Text",
    )

    cta_button_link = models.ForeignKey(
        'wagtailcore.page',
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Internal page link to send the user to when clicking CTA button."
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_section_text"),
        FieldPanel("hero_section_subtitle_text"),
        FieldPanel("cta_button_text"),
        PageChooserPanel("cta_button_link"),
    ]
