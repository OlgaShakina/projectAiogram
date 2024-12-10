import asyncio
import random

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from googletrans import Translator


from gtts import gTTS
import os

from config import TOKEN
import keybords  as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

ru_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
en_letters = 'abcdefghijklmnopqrstuvwxyz'

@dp.message()
async def echo(message: Message):
    text = message.text
    if text and len(text) > 0:
        translator = Translator()
        translated_text = translator.translate(text, src='ru', dest='en').text
        await message.reply(translated_text)
    else:
        await message.answer("О чем речь?")

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Супер']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('sample.m4a')
    await message.answer_voice(voice)

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile("video.mp4")
    await bot.send_video(message.chat.id, video)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('resume.pdf')
    await bot.send_document(message.chat.id, doc)

@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile("олененок.mp3")
    await bot.send_chat_action(message.chat.id, 'upload_audio')

@dp.message(Command('training'))
async def training(message: Message):
    training_list = [
        "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
        "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
        "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
    ]
    rand_tr = random.choice(training_list)
    await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")

    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.m4a')
    audio = FSInputFile('training.m4a')
    await bot.send_voice(message.chat.id, audio)
    os.remove("training.mp3")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')

@dp.message(CommandStart)
async def start(message: Message):
    await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=await kb.test_keyboard())

@dp.message()
async def start(message: Message):
    if message.text.lower() == "тест":
        await message.answer("тестируем")

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())
