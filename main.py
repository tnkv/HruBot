import hashlib
import logging

import config
import hru

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет, это хрю-хрю бот. Напиши любое сообщение сюда и оно будет хрюифицированно!\nЛибо воспользуйся <code>@hruhruubot сообщение</code> в любом чате.\n\nby @alpine & @tnkv_trolling")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(await hru.mainHru(message.text))


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    hruificated = await hru.mainHru(text)
    item = InlineQueryResultArticle(
        id=result_id,
        title=f'Отправить {hruificated}',
        input_message_content=types.InputTextMessageContent(
            message_text=hruificated)
    )
    await bot.answer_inline_query(inline_query.id, results=[item], cache_time=300)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
