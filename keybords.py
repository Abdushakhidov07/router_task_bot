from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext 


main_kb = ReplyKeyboardMarkup(
   keyboard=[
       [KeyboardButton(text="Add Task")],
       [KeyboardButton(text="Get task")]
       ], resize_keyboard=True,
    
)