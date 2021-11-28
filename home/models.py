from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, MultiFieldPanel
from wagtailvideos.edit_handlers import VideoChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

class HomePage(Page):
    hero_video = models.ForeignKey(
        "wagtailvideos.Video",
        related_name="+",
        null=True,
        on_delete=models.SET_NULL,
        help_text="Background Video for the homepage hero section."
    )

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
        VideoChooserPanel("hero_video"),
        FieldPanel("hero_section_text"),
        FieldPanel("hero_section_subtitle_text"),
        FieldPanel("cta_button_text"),
        PageChooserPanel("cta_button_link"),
    ]

@register_setting
class SiteSettings(BaseSetting):
    class Meta:
        verbose_name = "Site Settings"
    
    daily_rate = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        help_text="The daily rate for a single site.",
        null=True
    )
    weekly_rate = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        help_text="The weekly rate for a single site.",
        null=True
    )
    monthly_rate = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        help_text="The monthly rate for a single site not including electricity.",
        null=True
    )
    monthly_rate_all_included = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        help_text="The monthly rate for a single site including electricity.",
        null=True
    )
    business_phone_number = models.CharField(
        max_length=20,
        help_text="Your business phone number.",
        null=True
    )
    address = models.TextField(
        null=True,
        help_text="Your business address."
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("daily_rate"),
                FieldPanel("weekly_rate"),
                FieldPanel("monthly_rate"),
                FieldPanel("monthly_rate_all_included")
            ],
            "Park Rates"
        ),
        MultiFieldPanel(
            [
                FieldPanel("business_phone_number"),
                FieldPanel("address"),
            ],
            "Business Information"
        )
    ]