from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    icon = models.FileField(verbose_name=_("Icon"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'common_country'
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ('name',)


class Region(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions', verbose_name=_("Country"))
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'common_region'
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
        ordering = ('name',)

