def delete_chat_data(context,message):
    context.user_data['message_id'] = message.message_id
    context.user_data['chat_id'] = message.chat_id
    return context.user_data['message_id'],context.user_data['chat_id']

def delete_chat(context):
    context.bot.delete_message(chat_id=context.user_data['chat_id'], message_id=context.user_data['message_id'])