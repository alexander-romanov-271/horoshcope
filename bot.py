from aiogram import Bot, Dispatcher, types
from parser import ParseHoroscope
import os
from dotenv import load_dotenv


load_dotenv()
URL_RAMBLER = 'https://horoscopes.rambler.ru/'


bot = Bot(token=os.environ['API_TOKEN_TELEGRAM_BOT'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['', 'help'])
async def reply_with_list_of_commands(message: types.Message):

    first_command = 'Отправь:\n/, /help - чтобы получить эту справку\n'
    second_command = '/start, /info, /about_bot - чтобы получить информацию об этом боте\n'
    third_command = '/set_birthday - чтобы внести дату рождения\n'
    fourth_command = '/change_birthday - чтобы изменить дату рождения\n'
    fifth_command = '/delete_birthday - чтобы удалить дату рождения\n'
    
    reply = first_command + second_command + third_command + fourth_command + fifth_command
    await message.answer(reply)


@dp.message_handler(commands=['start', 'info', 'about_bot'])
async def reply_with_bot_info(message: types.Message):

    first_line = 'Привет, это бот, присылающий хорошие гороскопы.\n'
    second_line = 'Используя этого бота, ты можешь не сомневаться в \n'
    third_line = 'благоприятности и надежности предсказания.'

    reply = first_line + second_line + third_line

    await message.answer(reply)


@dp.message_handler(commands=['set_birthday'])
async def reply_to_get_user_birthday(message: types.Message):

    reply = "Пожалуйста, введи дату рождения"

    await message.reply(reply)


@dp.message_handler(commands=['change_birthday'])
async def reply_to_change_user_birthday(message: types.Message):

    reply = "Хочешь сменить дату рождения? Не вопрос, вводи другую:"

    await message.reply(reply)


@dp.message_handler(commands=['delete_birthday'])
async def reply_to_change_user_birthday(message: types.Message):

    reply = "Удаляешь дату рождения? Очень жаль, тебя ждали очень хорошие предсказания"

    await message.reply(reply)
