from aiogram import types, Router, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.handlers.states import Questions
from bot import answers as ANSWERS
from bot.prompts import ONE_PROMPT, FULL_PROMPT
from giga_module import giga
from utils.settings import Settings

router = Router()
bot: Bot

def register_bot(b: Bot):
    global bot
    bot = b

@router.message(Command(commands=["start"]))
async def start(msg: types.Message, state:FSMContext):
    await msg.answer(text = ANSWERS.START_TEXT)
    await msg.answer(text = f"""{ANSWERS.FIRST_QUESTION}""")
    await state.set_state(Questions.FIRST)
    
@router.message(Questions.FIRST)
async def first_question(msg: types.Message, state: FSMContext):
    answer = giga.get_answer(ONE_PROMPT.substitute(situation = ANSWERS.FIRST_QUESTION, answer = msg.text))
    await msg.answer(text = answer)
    await state.update_data(FIRST = msg.text)
    await state.set_state(Questions.SECOND)
    await msg.answer(text = ANSWERS.SECOND_QUESTION)

@router.message(Questions.SECOND)
async def second_question(msg: types.Message, state: FSMContext):
    answer = giga.get_answer(ONE_PROMPT.substitute(situation = ANSWERS.SECOND_QUESTION, answer = msg.text))
    await msg.answer(text = answer)
    await state.update_data(SECOND = msg.text)
    await state.set_state(Questions.THIRD)
    await msg.answer(text = ANSWERS.THIRD_QUESTION)
    
@router.message(Questions.THIRD)
async def third_question(msg: types.Message, state: FSMContext):
    answer = giga.get_answer(ONE_PROMPT.substitute(situation = ANSWERS.THIRD_QUESTION, answer = msg.text))
    await msg.answer(text = answer)
    await state.update_data(THIRD = msg.text)
    await state.set_state(Questions.FOURTH)
    await msg.answer(text = ANSWERS.FOURTH_QUESTION)
    
@router.message(Questions.FOURTH)
async def fourth_question(msg: types.Message, state: FSMContext):
    answer = giga.get_answer(ONE_PROMPT.substitute(situation = ANSWERS.FOURTH_QUESTION, answer = msg.text))
    await msg.answer(text = answer)
    await state.update_data(FOURTH = msg.text)
    await state.set_state(Questions.FIFTH)
    await msg.answer(text = ANSWERS.FIFTH_QUESTION)
    
@router.message(Questions.FIFTH)
async def fifth_question(msg: types.Message, state: FSMContext):
    answer = giga.get_answer(ONE_PROMPT.substitute(situation = ANSWERS.FIFTH_QUESTION, answer = msg.text))
    await msg.answer(text = answer)
    await state.update_data(FIFTH = msg.text)
    await msg.answer(text = ANSWERS.END)
    answers = await state.get_data()
    analis = giga.get_answer(FULL_PROMPT.substitute(
                               situation_1 = ANSWERS.FIRST_QUESTION,
                               answer_1 = answers['FIRST'],
                               situation_2 = ANSWERS.SECOND_QUESTION,
                               answer_2 = answers['SECOND'],
                               situation_3 = ANSWERS.THIRD_QUESTION,
                               answer_3 = answers['THIRD'],
                               situation_4 = ANSWERS.FOURTH_QUESTION,
                               answer_4 = answers['FOURTH'],
                               situation_5 = ANSWERS.FIFTH_QUESTION,
                               answer_5 = answers['FIFTH']
                           ))
    await bot.send_message(chat_id=Settings.get_admin_id(),
                           text = f"Анализ собеседования с пользователем {msg.from_user.username}\n"+ analis)

    