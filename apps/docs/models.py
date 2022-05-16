from django.utils.translation import gettext_lazy as _

from django.db import models

from apps.common.models import UUIDModel, TimeStamp
from apps.general.models import ReasonType


class Docs(UUIDModel):
    class Meta:
        verbose_name = _('Output document')
        verbose_name_plural = _('Output documents')

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    number = models.IntegerField(verbose_name=_('Identifier'))
    date = models.DateField(verbose_name=_('Date'))
    reason = models.ForeignKey(ReasonType, on_delete=models.SET_NULL, null=True, verbose_name=_("Reason"))
    file = models.FileField(upload_to="generated_docs/", verbose_name=_('File'))


class DocTemplate(UUIDModel, TimeStamp):
    """Template for generating a document"""
    class Meta:
        verbose_name = _('Incoming document')
        verbose_name_plural = _('Incoming documents')

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    file = models.FileField(upload_to="doc_templates/", verbose_name=_('File'))

    def __str__(self):
        return self.name
