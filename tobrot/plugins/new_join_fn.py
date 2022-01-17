from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tobrot import AUTH_CHANNEL


async def start_fn(client, message):
    if message.chat.type == 'private':
        name = message.from_user.first_name
        msg = f"Ola {name}!\n"
        msg += "Apenas meu dono pode me usar <3"
        msg += "\n\nObrigado 😊"
        await message.reply_text(
            msg,
            parse_mode="html",
            quote=True
        )
    elif message.from_user.id in AUTH_CHANNEL:
        await message.reply_text(f"Ola {message.from_user.first_name}!")

        
