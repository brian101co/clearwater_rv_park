from django.db import models

from wagtail.core.models import Page

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks

class AmenitiesPage(Page):
    page_title = models.CharField(
        max_length=200,
        blank=False,
        help_text="Main title for the page."
    )

    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="The banner image at the top of the page."
    )

    amenities_carousel = StreamField([
        ('Carousel', blocks.CarouselBlock()),
    ],
        null=True,
        blank=True,
    )

    amenities = StreamField([
        ('Amenity', blocks.AmenityBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("amenities_carousel"),
        StreamFieldPanel("amenities"),
    ]
    

class AttractionsPage(Page):
    page_title = models.CharField(
        max_length=200,
        blank=False,
        help_text="Main title for the page."
    )

    attractions = StreamField([
        ('Attraction', blocks.AttractionBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        StreamFieldPanel("attractions"),
    ]

class RatesPage(Page):
    pass
