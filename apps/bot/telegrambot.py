import logging
from django.conf import settings
from telegram import Update, Bot
from telegram.ext import CallbackContext
from django.utils.translation import gettext_lazy as _, activate
from apps.bot import models
from utils.decarators import get_member
from .buttons.function import delete_chat, delete_chat_data
from .buttons.inline import *
from .buttons.keyboard import get_phone_number_button
from .state import state


logger = logging.getLogger(__name__)
bot = Bot(token=settings.BOT_TOKEN)


@get_member
def start(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    """Send a message when the command /start is issued."""
    update.message.delete()
    update.message.reply_text(str(_("Salom|Privet|Hello")), reply_markup=get_language_button())

    return state.GET_LANGUAGE


@get_member
def get_language(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    query.answer()
    tg_user.language = query.data
    context.user_data['language'] = query.data
    tg_user.save()
    activate(tg_user.language)
    query.edit_message_text(str(_("who are you?")), reply_markup=get_position_button())

    return state.GET_USER_TYPE


@get_member
def get_user_type_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    query.answer()
    #save user type
    context.user_data['user_type'] = query.data
    #send message
    message = query.edit_message_text(str(_("Ism,Familya,Ochistvangizni kiriting:")))
    delete_chat_data(context,message)
    return state.GET_FULL_NAME_EXIBITOR


@get_member
def get_full_name_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    # save full name
    context.user_data['full_name'] = update.message.text
    # delete message
    update.message.delete()
    delete_chat(context)
    # send message
    message = update.message.reply_text(
        text=str(_("company name:")),
    )
    delete_chat_data(context,message)
    return state.GET_COMPANY_NAME_EXIBITOR


@get_member
def get_company_name(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    # save company name
    context.user_data['company_name'] = update.message.text
    # delete message
    update.message.delete()
    delete_chat(context)
    # send message
    update.message.reply_text(text=str(_("Country:")), reply_markup=get_country_button())
    return state.GET_COUNTRY_NAME_EXIBITOR


@get_member
def get_country_name_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    query.answer()
    # save country name
    context.user_data['country_name'] = query.data
    # delete message
    query.delete_message()
    # get phone number
    message = context.bot.send_message(chat_id=update.effective_chat.id,text=str(_("Phone number:")), reply_markup=get_phone_number_button())
    delete_chat_data(context,message)
    return state.GET_PHONE_NUMBER_NAME_EXIBITOR


@get_member
def get_phone_number_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    #save phone number
    context.user_data['phone_number'] = update.message.contact.phone_number
    # delete message
    update.message.delete()
    delete_chat(context)
    #send message
    message = update.message.reply_text(text=str(_("Email:")), )
    delete_chat_data(context,message)
    return state.GET_EMAIL_EXIBITOR


@get_member
def get_email_exibitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    # save email
    context.user_data['email'] = update.message.text
    # delete message
    update.message.delete()
    delete_chat(context)
    update.message.reply_text("thanks for registration  foydali malumotlar uchun kanalimizga azo boling",reply_markup=invite_to_channel_link())
    print(context.user_data)
    update.message.reply_text(context.user_data)



#________________________________ visitor registration___________________________________________________________________________________________________________________________



@get_member
def get_user_type_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    query.answer()
    # save user type
    context.user_data['user_type'] = query.data
    message = query.edit_message_text(str(_("Fistname:")))
    delete_chat_data(context, message)
    return state.GET_NAME_VISITOR




@get_member
def get_name_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    # save fist name
    context.user_data['name'] = update.message.text
    # delete message
    update.message.delete()
    delete_chat(context)
    # send message
    message = update.message.reply_text(str(_("Lastname:")))
    delete_chat_data(context, message)
    return state.GET_SURNAME_VISITOR

@get_member
def get_surname_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    # save last name
    context.user_data['surname'] = update.message.text
    # delete message
    update.message.delete()
    delete_chat(context)
    # send message
    update.message.reply_text(str(_("Country:")), reply_markup=get_country_button())
    return state.GET_COUNTRY_VISITOR

@get_member
def get_country_name_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    query.answer()
    # save country name
    context.user_data['country_name'] = query.data
    query.edit_message_text(str(_("Region:")), reply_markup=get_region_button(query.data))
    return state.GET_REGION_VISITOR

@get_member
def get_region_name_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    query.answer()
    # save region name
    context.user_data['region_name'] = query.data
    query.edit_message_text(str(_("Personality type:")), reply_markup=get_personality_type_button())
    return state.PERSONALITY_TYPE_VISITOR

@get_member
def personality_type_visitors(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    query = update.callback_query
    query.answer()
    # save personality type
    context.user_data['personality_type'] = query.data
    # delete message
    query.delete_message()
    # send message
    message = context.bot.send_message(chat_id=update.effective_chat.id,text=str(_("Phone number:")), reply_markup=get_phone_number_button())
    delete_chat_data(context,message)
    return state.GET_PHONE_NUMBER_VISITOR

@get_member
def get_phone_number_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    # save phone number
    context.user_data['phone_number'] = update.message.contact.phone_number

    # delete message
    update.message.delete()
    delete_chat(context)
    #send message
    message = update.message.reply_text(text=str(_("Email:")), )
    delete_chat_data(context,message)
    return state.GET_EMAIL_VISITOR


@get_member
def get_email_visitor(update: Update, context: CallbackContext, tg_user: models.TelegramProfile):
    # save email
    context.user_data['email'] = update.message.text

    # delete message
    update.message.delete()
    delete_chat(context)

    update.message.reply_text("thanks for registration  foydali malumotlar uchun kanalimizga azo boling",
                              reply_markup=invite_to_channel_link())
    print(context.user_data)
    update.message.reply_text(context.user_data)
