"""
Context Layer Management.

.. note:: Context Layer App.
"""

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContextLayerConfig(AppConfig):
    """Context Layer Config App."""

    name = 'context_layer_management'
    verbose_name = _('Context Layer')