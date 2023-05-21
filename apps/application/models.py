from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.application.choices import PersonalityOption
from apps.common.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField


class HearingUs(BaseModel):
    title = models.CharField(_("Title"), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Hearing Us")
        verbose_name_plural = _("Hearing Us")


class BookStand(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    company_name = models.CharField(_("Company name"), max_length=255)
    country = models.ForeignKey('common.Country', verbose_name=_("Country"), on_delete=models.CASCADE)
    phone = PhoneNumberField(_("Phone"), null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=255)
    hear_us = models.ForeignKey(HearingUs, on_delete=models.CASCADE, verbose_name=_("Hearing us"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Book Stand")
        verbose_name_plural = _("Book Stands")


class ChoiceOfService(BaseModel):
    title = models.CharField(_("First name"), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Choice Of Service")
        verbose_name_plural = _("Choice Of Services")


class ActivityOfYourCompany(BaseModel):
    title = models.CharField(_("First name"), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Activity Of Your Company")
        verbose_name_plural = _("Activity Of Your Companies")


class Visitor(BaseModel):
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    country = models.ForeignKey('common.Country', verbose_name=_("Country"), on_delete=models.CASCADE)
    region = models.ForeignKey('common.Region', verbose_name=_("Region"), on_delete=models.CASCADE)
    personality = models.CharField(verbose_name=_("Personality"), max_length=10, choices=PersonalityOption.choices,
                                   default=PersonalityOption.PHYSICAL)
    company_name = models.CharField(_("Company name"), max_length=100, null=True, blank=True)
    job_title = models.CharField(_("Job title"), max_length=100, null=True, blank=True)
    website = models.URLField(_("Website"), null=True, blank=True)
    phone = PhoneNumberField(_("Phone"))
    email = models.EmailField(_("Email"), max_length=255)
    service = models.ManyToManyField(ChoiceOfService, verbose_name=_("Services"))
    activity = models.ManyToManyField(ActivityOfYourCompany, verbose_name=_("Activities"))
    feedback = models.TextField(_("Feedback"), null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Visitor")
        verbose_name_plural = _("Visitors")
