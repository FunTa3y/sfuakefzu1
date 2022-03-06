from vkbottle.user import Blueprint, Message

from utils.edit_msg import edit_msg
from filters import ForEveryoneRule


bp = Blueprint("help")


@bp.on.message(ForEveryoneRule("help"), text="<prefix>хелп")
async def config(message: Message):
    await edit_msg(
        bp.api,
        message,
        f'!инфо упоминание\n'
        f'!рандом Любое слово\n'
        f'!пинг\n'
        f'!ачивка текст1|текст2\n'
        f'!me то что вы сделали\n'
        f'!Бонкнуть упоминание\n'
        f'!Бросить кактус упоминание\n'
        f'!бомба ваше сообщение\n'
        f'!цитата ответ на то сообщение что будет цитатой\n'
        f'\n'
        f'!дем текст1|текст2\n'
        f'!дем текст1\n'
        f'!дем |текст2\n'
        f'\n'
        f'!Подробнее команда soon\n'
        '!погода город soon \n'
    )