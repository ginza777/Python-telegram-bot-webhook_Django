from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

from apps.common.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField


class MainBanner(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    sub_title = models.CharField(_("Sub title"), max_length=255)
    banner = models.ImageField(upload_to="main/banner", verbose_name=_("Banner"))
    arranged_date = models.DateTimeField(_("Arranged date"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Main Banner")
        verbose_name_plural = _("Main Banners")


class AboutProject(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    count = models.PositiveIntegerField(_("Count"))
    order = models.PositiveIntegerField(_("Order"), default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("About Project")
        verbose_name_plural = _("About Projects")


class AboutUs(BaseModel):
    text = RichTextUploadingField()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")


class Participant(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    country = models.ForeignKey('common.Country', verbose_name=_("Country"), on_delete=models.CASCADE)
    image = models.ImageField(upload_to="participant/", verbose_name=_("Image"))
    order = models.PositiveIntegerField(_("Order"), default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Participant")
        verbose_name_plural = _("Participants")


class Exhibitor(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    country = models.ForeignKey('common.Country', verbose_name=_("Country"), on_delete=models.CASCADE)
    image = models.ImageField(upload_to="exhibitor/", verbose_name=_("Image"))
    order = models.PositiveIntegerField(_("Order"), default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Exhibitor")
        verbose_name_plural = _("Exhibitors")


class ProductGroup(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    icon = models.FileField(upload_to="product_group/", verbose_name=_("Icon"))
    order = models.PositiveIntegerField(_("Order"), default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Product Group")
        verbose_name_plural = _("Product Groups")


class Team(BaseModel):
    full_name = models.CharField(_("Full name"), max_length=255)
    position = models.CharField(_("Position"), max_length=255)
    image = models.ImageField(upload_to="team/", verbose_name=_("Image"))
    order = models.PositiveIntegerField(_("Order"), default=1)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")


class BenifitsForVisitor(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    icon = models.FileField(upload_to="product_group/", verbose_name=_("Icon"))
    order = models.PositiveIntegerField(_("Order"), default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Benifits For Visitor")
        verbose_name_plural = _("Benifits For Visitors")


class Partner(BaseModel):
    link = models.URLField(_("Link"), max_length=255)
    image = models.FileField(upload_to="partner/", verbose_name=_("Image"))
    order = models.PositiveIntegerField(_("Order"), default=1)

    def __str__(self):
        return f"Partner {self.id}"

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")


class Contact(BaseModel):
    email = models.EmailField(_("Email"), max_length=255)
    address = models.CharField(_("Address"), max_length=255)
    phone = PhoneNumberField(verbose_name=_("Phone"), null=True, blank=True)
    latitude = models.CharField(_("Latitude"), max_length=50)
    longitude = models.CharField(_("Longitude"), max_length=50)

    def __str__(self):
        return f"Contact {self.id}"

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contact")


class ContactUs(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    country = models.ForeignKey('common.Country', verbose_name=_("Country"), on_delete=models.CASCADE)
    company_name = models.CharField(_("Company name"), max_length=255)
    phone = PhoneNumberField(verbose_name=_("Phone"), null=True, blank=True)
    message = models.TextField(_("Message"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("Contact Us")


class Social(BaseModel):
    telegram = models.URLField(_("Telegram"), max_length=255, null=True, blank=True)
    instagram = models.URLField(_("Instagram"), max_length=255, null=True, blank=True)
    twitter = models.URLField(_("Twitter"), max_length=255, null=True, blank=True)
    youtube = models.URLField(_("Youtube"), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.telegram

    class Meta:
        verbose_name = _("Social")
        verbose_name_plural = _("Socials")
