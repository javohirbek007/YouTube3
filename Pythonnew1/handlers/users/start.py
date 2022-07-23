from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from Pythonnew1.loader import dp

from Pythonnew1.keyboards.inline.tugma import til

@dp.message_handler(commands='start')
async def bot_echo(message: types.Message):
    await message.answer(f"- Tilni tanlang! (Uz🇺🇿)\n\n"
                         f"- Выберите язык! (Ru🇷🇺)\n\n"
                         f"- Select a language! (En🇺🇸)"
                         ,reply_markup=til)
