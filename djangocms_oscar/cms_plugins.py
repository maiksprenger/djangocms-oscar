from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from . import models


class FeaturedProductPlugin(CMSPluginBase):
    model = models.FeaturedProduct
    name = _("Featured product")
    admin_preview = True
    render_template = 'djangocms_oscar/plugins/product.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(FeaturedProductPlugin)
