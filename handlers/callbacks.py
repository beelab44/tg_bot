from aiogram import Router, F
from aiogram.types import CallbackQuery

callback_router = Router()

@callback_router.callback_query(F.data == "faq")
async def faq_callback(callback: CallbackQuery):
    await callback.answer() # Acknowledge callback
    await callback.message.answer("Тут будуть відповіді на часті питання. Наприклад:\n- Як замовити?\n- Скільки часу займає доставка?")

@callback_router.callback_query(F.data == "delivery_terms")
async def delivery_terms_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Ознайомтеся з нашими умовами доставки: ... (деталі умов)")

@callback_router.callback_query(F.data == "contact_operator")
async def contact_operator_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Для зв'язку з оператором, зателефонуйте за номером: +380XXXXXXXXX або напишіть @operator_username")

@callback_router.callback_query(F.data == "leave_feedback")
async def leave_feedback_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Дякуємо за ваш відгук! Напишіть ваше повідомлення, і ми його опрацюємо.")