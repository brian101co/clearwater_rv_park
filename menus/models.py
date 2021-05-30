from django.db import models
from modelcluster.models import ClusterableModel
from django_extensions.db.fields import AutoSlugField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel
from condensedinlinepanel.edit_handlers import CondensedInlinePanel
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey

class MenuItem(Orderable):
    link_title = models.CharField(blank=True, max_length=50)
    link_url = models.CharField(blank=True, max_length=250)
    link_anchor = models.CharField(blank=True, max_length=250)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="+",
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        FieldPanel("link_anchor"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    page = ParentalKey("Menu", related_name="menu_items")

class Menu(ClusterableModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        CondensedInlinePanel("menu_items", label="Menu Item", card_header_from_field="link_title"),
    ]

    def __str__(self):
        return self.title



