from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Зробити замовлення"), KeyboardButton(text="ℹ️ Мої замовлення")],
        [KeyboardButton(text="ℹ️ Наші контакти")],
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)
