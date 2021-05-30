from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class CarouselBlock(blocks.StructBlock):
    images = blocks.ListBlock(
       blocks.StructBlock(
           [
               ("image", ImageChooserBlock()),
           ]
       )
    )

    class Meta:
        template = "streams/carousel_block.html"
        icon = "image"
        label = "Image Carousel"

class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock(
        max_length=255,
        help_text="The question you'd like to answer."
    )
    answer = blocks.TextBlock(
        help_text="The answer to the provided question."
    )

    class Meta:
        template = "streams/faq_block.html"
        icon = "snippet"
        label = "FAQ"

class AttractionBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="Main Image for the attraction"
    )
    title = blocks.CharBlock(
        max_length=60,
        help_text="Title of the attraction."
    )
    text = blocks.TextBlock(
        help_text="Desciption of the attraction."
    )
    link = blocks.CharBlock(
        blank=True, 
        max_length=250,
        help_text="Link to learn more about the attraction."
    )

    class Meta:
        template = "streams/attraction_block.html"
        icon = "snippet"
        label = "Attraction"

class AmenityBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="Image displayed on the side for the amenity."
    )
    title = blocks.CharBlock(
        max_length=60,
        help_text="Title of the amenity."
    )
    text = blocks.TextBlock(
        help_text="Desciption of the amenity."
    )

    class Meta:
        template = "streams/amenity_block.html"
        icon = "snippet"
        label = "Amenity"

class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="A full width image with a title.",
    )
    title = blocks.CharBlock(max_length=60)

    class Meta:
        template="streams/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"

class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="A full width image.",
    )

    class Meta:
        template="streams/image_block.html"
        icon = "image"
        label = "Image"

class RichtextBlock(blocks.RichTextBlock):
    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full Richtext Editor"
        help_text = "A richtext editor for writing content."

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text='Text to display',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "title"
        label = "Title"
        help_text =  "Centered Text to display on the page"

class ParagraphBlock(blocks.StructBlock):
    text = blocks.TextBlock(
        required=True,
        help_text="Paragraph to display text"
    )

    class Meta:
        template = "streams/paragraph_block.html"
        icon = "pilcrow"
        label = "Paragraph"
        help_text =  "Left aligned text to be displayed on the page."

class BlockquoteBlock(blocks.StructBlock):
    text = blocks.TextBlock(
        required=True,
        help_text="Quote to be display on the page."
    )

    attribution = blocks.CharBlock(
        max_length=100,
        help_text="Attribution",
    )

    class Meta:
        template = "streams/blockquote_block.html"
        icon = "openquote"
        label = "Blockquote"
        help_text =  "A full width quote to display on the page."