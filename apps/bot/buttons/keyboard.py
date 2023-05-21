from telegram import KeyboardButton, ReplyKeyboardMarkup


def get_phone_number_button():
    con_keyboard = KeyboardButton(text="send_contact", request_contact=True)
    return ReplyKeyboardMarkup([[con_keyboard]],resize_keyboard=True,one_time_keyboard=True)
