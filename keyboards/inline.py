from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

info_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Наш сайт", url="https://example.com/delivery-site")],
        [InlineKeyboardButton(text="❓ Часті питання (FAQ)", callback_data="faq")],
        [InlineKeyboardButton(text="📝 Умови доставки", callback_data="delivery_terms")]
    ]
)

support_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📞 Зв'язатися з оператором", callback_data="contact_operator")],
        [InlineKeyboardButton(text="⭐ Залишити відгук", callback_data="leave_feedback")]
    ]
)