from wagtail.core import blocks


class HeaderBlock(blocks.StructBlock):
    sub_title = blocks.CharBlock(required=True)
    page = blocks.PageChooserBlock(required=False)
    url = blocks.URLBlock(required=False)

    dropdown_item = blocks.ListBlock(
        blocks.StructBlock([
            ("text", blocks.CharBlock(required=False)),
            ("page", blocks.PageChooserBlock(required=False)),
            ("page_url", blocks.URLBlock(required=False, max_length=60)),
        ])
    )

    class Meta:
        template = "header/header_block.html"
        icon = "plus"
        label = "Header Items"
