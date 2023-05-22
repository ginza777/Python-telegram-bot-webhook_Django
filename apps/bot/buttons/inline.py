from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from django.utils.translation import gettext_lazy as _
from apps.common.models import Country, Region
from core.settings.base import LANGUAGES
def get_language_button():
    buttons = [
        [
            InlineKeyboardButton(str(_("🇺🇿 O'zbekcha")), callback_data='uz'),
            InlineKeyboardButton(str(_("🇷🇺 Русский")), callback_data='ru'),
            InlineKeyboardButton(str(_("🇺🇸 English")), callback_data='en'),
        ]
    ]

    return InlineKeyboardMarkup(buttons)

def get_position_button():
    buttons = [
        [
            InlineKeyboardButton(str(_("Exibitor")), callback_data='exibitor'),
            InlineKeyboardButton(str(_("Visitor")), callback_data='visitor'),
        ]
    ]
    return InlineKeyboardMarkup(buttons)


def get_country_button():
    countrys = Country.objects.all()
    print(countrys)
    list_country_all=[]
    list_test=[]
    for country in countrys:
        print(country.name)
        list_test.append(InlineKeyboardButton(str(_(country.name)), callback_data=country.name))
        if len(list_test)==2:
            list_country_all.append(list_test)
            list_test=[]
        elif len(list_test)==1 and country.name==countrys[len(countrys)-1].name:
            list_country_all.append(list_test)
            list_test=[]

    buttons = list_country_all

    return InlineKeyboardMarkup(buttons)
def invite_to_channel_link():
    buttons = [
        [
            InlineKeyboardButton(str(_("Invite")), url='https://t.me/uicgroup'),
        ]
    ]
    return InlineKeyboardMarkup(buttons)


#visitor

def get_region_button(country:str):
    regions = Region.objects.filter(country__name=country)
    list_region_all=[]
    list_test=[]
    for region in regions:
        list_test.append(InlineKeyboardButton(str(_(region.name)), callback_data=region.name))
        if len(list_test)==2:
            list_region_all.append(list_test)
            list_test=[]
        elif len(list_test)==1 and region.name==regions[len(regions)-1].name:
            list_region_all.append(list_test)
            list_test=[]

    buttons = list_region_all

    return InlineKeyboardMarkup(buttons)

def get_personality_type_button():
    buttons = [
        [
            InlineKeyboardButton(str(_("legal")), callback_data='legal'),
            InlineKeyboardButton(str(_("physical")), callback_data='physical'),
        ]
    ]
    return InlineKeyboardMarkup(buttons)