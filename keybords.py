from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Тестовая кнопка')],
    [KeyboardButton(text='Тестовая кнопка 2'), KeyboardButton(text='Тестовая кнопка 3')]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео', url='https://rutube.ru/video/9a8bcdd408ef3eeb6328e94a373a7833/?r=wd')]
])

test = ['кнопка1','кнопка2','кнопка3','кнопка4']

async def test_keyboard():
    keyboard = ReplyKeyboardBuilder()
    for key in test:
        keyboard.add(KeyboardButton(text=key))
    return keyboard.adjust(2).as_markup()