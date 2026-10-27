from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext 
from keybords import *
from states import router as state_router
from service import *
from connection import *


import os
import asyncio


load_dotenv()

token_bot = os.getenv("BOT_TOKEN")

bot = Bot(token=token_bot)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_bot(message: Message):
    if await  get_user_by_id(message.from_user.id):
        await message.answer(f"Hello @{message.from_user.username}", reply_markup=main_kb)
    else:
        user = message.from_user
        await create_user(user.username, user.full_name, user.id)
        await message.answer(f"Hello @{message.from_user.username}", reply_markup=main_kb)
        
        


@dp.message(F.text == "Get task")
@dp.message(Command("get_task"))
async def start_bot(message: Message):
    tasks = await get_task(message.from_user.id)
    text = ""
    for task in tasks:
        text+= f"""
Id: {task['task_id']}  
Title: {task['title']}  
Caption: {task['caption']}
Dueration date: {task['due_date']}
Status: {task['status']}

Created at: {task['created_at']}


                             """
    await message.answer(text)
        








async def  main():
    print("Bot started!")
    dp.include_router(state_router)
    await create_table()
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())

