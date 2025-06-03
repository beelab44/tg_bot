# handlers/basic.py
from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.reply import main_delivery_keyboard
from keyboards.inline import info_inline_keyboard, support_inline_keyboard

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Вітаємо у боті доставки! Чим можемо допомогти?", reply_markup=main_delivery_keyboard)

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Доступні команди:\n/start - Головне меню\n/menu - Показати меню\n/my_orders - Мої замовлення\n/help - Допомога")

@router.message(Command("menu"))
async def menu_command(message: Message):
    # Тут буде логіка для показу меню (наприклад, категорій товарів)
    await message.answer("Ось наше меню (незабаром!)")

@router.message(Command("my_orders"))
async def my_orders_command(message: Message):
    # Тут буде логіка для показу замовлень користувача
    await message.answer("У вас поки що немає замовлень.")

@router.message(F.text == "🍕 Замовити їжу")
async def order_food_handler(message: Message):
    # Можна перенаправити на команду /menu або почати процес замовлення
    await message.answer("Переходимо до меню...", reply_markup=main_delivery_keyboard) # Можна додати інлайн клаву з категоріями

@router.message(F.text == "🛒 Мої замовлення")
async def my_orders_handler(message: Message):
    await my_orders_command(message) # Викликаємо відповідну команду

@router.message(F.text == "ℹ️ Інформація")
async def information_handler(message: Message):
    await message.answer("Оберіть пункт, який вас цікавить:", reply_markup=info_inline_keyboard)

@router.message(F.text == "📞 Підтримка")
async def support_handler(message: Message):
    await message.answer("Оберіть опцію для зв'язку:", reply_markup=support_inline_keyboard)
