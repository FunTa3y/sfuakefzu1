from random import randint
from vkbottle.user import Blueprint, Message

from utils.edit_msg import edit_msg
from filters import ForEveryoneRule

from vkbottle import Bot
from vkbottle.api import API
import time, math

bp = Blueprint("rassilka")


@bp.on.message(ForEveryoneRule("userinforassilka"), text="<prefix>/юзеры <!>")
async def random_case(message: Message):
    users = []
    conversations = await bp.api.messages.get_conversations(count=200)
    for i in range(conversations.count):
        if conversations.items[i].conversation.peer.type == 'user' and conversations.items[i].conversation.can_write.allowed:
            users.append(conversations.items[i].conversation.peer.id)
    await message(f"Всего юзеров: {conversations.count}\nРазрешили писать в лс: {len(users)}")

@bp.on.message(ForEveryoneRule("rassilka"), text="<prefix>/разослать <!>")
async def lsmsg(ans: Message, txt):
    start_time = time.time()
    conversations = await bp.api.messages.get_conversations(count=200)
    for i in range(conversations.count):
        if conversations.items[i].conversation.peer.type == 'user' and conversations.items[i].conversation.can_write.allowed:
            await bp.api.messages.send(peer_id=conversations.items[i].conversation.peer.id, random_id=0, message=txt)
    end_time = time.time()
    await ans(f'Рассылка завершена за {round(end_time-start_time, 1)} сек.')

bp.run_polling()