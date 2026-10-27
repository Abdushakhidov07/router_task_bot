from aiogram import  Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext 
from service import *


main_kb = ReplyKeyboardMarkup(
   keyboard=[
       [KeyboardButton(text="Add Task")]
       ], resize_keyboard=True,
    
)

router = Router()

class AddTask(StatesGroup):
    get_title = State()
    get_caption = State()
    get_due_date = State()
    
class DeleteTask(StatesGroup):
    get_id = State()
    
class UpdateTask(StatesGroup):
    get_id = State()
    get_title = State()
    get_caption = State()
    
@router.message(F.text == "Add Task")    
@router.message(Command("add"))
async def add_task(message: Message, state : FSMContext):
    await message.answer("Введите имя таска: ")
    await state.set_state(AddTask.get_title)
    
    
    
    
    
@router.message(AddTask.get_title)
async def get_title(message: Message, state : FSMContext):
    await state.update_data(title = message.text)
    await message.answer("Введите описания таска: ")
    await state.set_state(AddTask.get_caption)
    
    
    
@router.message(AddTask.get_caption)
async def get_caption(message: Message, state : FSMContext):
    await state.update_data(caption = message.text)
    await message.answer("Введите дату таска: ")
    await state.set_state(AddTask.get_due_date)
    
    
@router.message(AddTask.get_due_date)
async def get_due_date(message: Message, state : FSMContext):
    await state.update_data(due_date = message.text)
    data = await state.get_data()
    await create_task(data["title"], data["caption"], data["due_date"], message.from_user.id)
    await message.answer("Таск создан!")
