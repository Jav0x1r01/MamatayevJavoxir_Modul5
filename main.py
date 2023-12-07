import asyncio
import logging
import sys
from os import getenv
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
from button.reply import reply_button, start_button, women_button, week_button
from db.config import add_user

TOKEN = "6597049491:AAF_355hftAb8emdaWO80bocPNg9OBoHav4"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

class UserState(StatesGroup):
    start = State()
    fitnes = State()
    week= State()




@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    add_user(message.from_user.full_name, message.from_user.id)
    await message.answer_photo("AgACAgQAAxkBAAM0ZXGrRWb1uSAGe6BimyOd6NW09WYAAgOxMRtf5X1Tl2zrhKVIB_ABAAMCAANzAAMzBA","Assalomu alaykum ! \nBu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi",reply_markup=reply_button())



# @dp.message(Command("NewPost"))
# async def New_post_hendl(message:Message):





@dp.message(lambda msg:msg.text=="📍Filial")
async def send_lacation(msg:Message):
    await msg.reply_location(41.304476, 69.253043)

@dp.message(lambda msg:msg.text=="✅Start")
async def send_lacation(msg:types.Message, state: FSMContext):
    await state.set_state(UserState.start)
    await msg.answer("Quydagilardan birontasini tanlang 👇🏿",reply_markup=start_button())

@dp.message(lambda msg:msg.text=="Woman 🧍‍♀️",UserState.start)
async def gender(msg:types.Message, state: FSMContext):
    await state.set_state(UserState.fitnes)
    await msg.answer_photo("AgACAgQAAxkBAAMOZXGmGep6Jb5Q2PkDfijK-R7tegADk7AxG3X1fFMCkr2xXY1d1wEAAwIAA3MAAzME",caption="Quydagilardan birontasini tanlang 👇🏿", reply_markup=women_button())

@dp.message(lambda msg:msg.text=="Men 🧍‍♂️",UserState.start)
async def gender(msg:types.Message, state: FSMContext):
    await state.set_state(UserState.fitnes)
    await msg.answer_photo("AgACAgQAAxkBAAMWZXGoKVo6khxC-QRqAiyQfyHznAcAAm2xMRtYe7VTNP9XZg9XX-gBAAMCAANzAAMzBA",caption="Quydagilardan birontasini tanlang 👇🏿", reply_markup=women_button())


@dp.message(UserState.fitnes)
async def week_hendl(msg:types.Message, state: FSMContext):
    await state.set_state(UserState.week)
    await msg.answer("Hafta kunlaridan birontasini tanlang",reply_markup=week_button())


@dp.message(F.photo)
async def photo_hendl(msg:Message):

    await msg.answer(msg.photo[0].file_id)

@dp.message(lambda msg:msg.text=="👨🏻‍💻Admin")
async def admin_hendl(msg:Message):
    await msg.answer("https://t.me/Absaitov_Dilshod")












async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN)
    # And the run events dispatching
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())