from django.utils.translation import gettext_lazy as _

from django.db import models

from apps.common.models import UUIDModel


class Docs(UUIDModel):
    class Meta:
        verbose_name = _('Incoming document')
        verbose_name_plural = _('Incoming documents')

    class DocType(models.TextChoices):
        INCOMING = "IN", _("Incoming")
        OUTPUT = "OUT", _("Output")

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    type = models.CharField(max_length=10, choices=DocType.choices, verbose_name=_('Type'))
    number = models.IntegerField(verbose_name=_('Identifier'))
    date = models.DateField(verbose_name=_('Date'))
    reason = models.CharField(max_length=255, verbose_name=_("Reason"))
