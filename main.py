import hashlib
import logging

import config
import hru

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


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
