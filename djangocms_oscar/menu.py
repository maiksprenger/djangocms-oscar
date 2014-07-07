# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from oscar.core.loading import get_model

Category = get_model('catalogue', 'category')


class CategoriesMenu(CMSAttachMenu):
    name = _("Categories Menu")

    def get_nodes(self, request):
        nodes = []
        tree = Category.get_tree()
        for node in tree:
            parent = node.get_parent()
            parent_id = parent.slug if parent else None
            nodes.append(NavigationNode(
                node.name,
                node.get_absolute_url(),
                node.slug,
                parent_id
                )
            )
        return nodes


menu_pool.register_menu(CategoriesMenu)