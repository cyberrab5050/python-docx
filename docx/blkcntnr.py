# encoding: utf-8

"""
Block item container, used by body, cell, header, etc. Block level items are
things like paragraph and table, although there are a few other specialized
ones like structured document tags.
"""

from __future__ import absolute_import, print_function

from .shared import Parented
from .text import Paragraph


class BlockItemContainer(Parented):
    """
    Base class for proxy objects that can contain block items, such as _Body,
    _Cell, header, footer, footnote, endnote, comment, and text box objects.
    Provides the shared functionality to add a block item like a paragraph or
    table.
    """
    def __init__(self, element, parent):
        super(BlockItemContainer, self).__init__(parent)
        self._element = element

    def add_paragraph(self, text='', style=None):
        """
        Return a paragraph newly added to the end of the content in this
        container, having *text* in a single run if present, and having
        paragraph style *style*. If *style* is |None|, no paragraph style is
        applied, which has the same effect as applying the 'Normal' style.
        """
        p = self._element.add_p()
        paragraph = Paragraph(p, self)
        if text:
            paragraph.add_run(text)
        if style is not None:
            paragraph.style = style
        return paragraph