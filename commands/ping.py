"""
Команда, которая показывает, что бот работает
"""
from time import time
import json
import platform
import psutil
from random import randint
from datetime import datetime
import sys

from vkbottle.bot import Blueprint, Message
from utils.edit_msg import edit_msg
from filters import ForEveryoneRule


bp = Blueprint("Ping-pong command")

quote = ['Я не волшебник, я всего лишь учусь','Это не баг — это незадокументированная фича.','Удаленный код — отлаженный код.','Чтобы понять рекурсию, нужно сперва понять рекурсию.', 'Самая сложная часть в дизайне… держаться подальше от фич.', 'Если сразу не получилось хорошо, назовите это версией 1.0.', 'format c: - лучший антивирус', 'Куплюклавиатурусработающимпробелом', 'Чудеса случаются.', 'Предположим, что у тебя есть 1000 рублей... Ну, для круглого счета возьмем 1024...', '99% ошибок компьютера сидит в полуметре от монитора.', 'Невозможно победить того, кто не сдается', 'Моё "люблю" очень дорогого стоит. Говорю это редко и мало кому.', 'Миллионы людей не заменят тебя. Никогда.', 'Ничего в этой жизни не дается легко']
text = quote[randint(0, (len(quote)-1))]
 
datanow = datetime.now()




@bp.on.message(ForEveryoneRule("ping"), text="<prefix>пинг")
async def ping_handler(message: Message):
    """
    > !пинг

    > 🏓 | Понг!
    > ⏱ | Ответ за 0.05 секунд

    (если включен режим debug)
    > 🏓 | Понг!
    > ⏱ | Ответ за 0.05 секунд (debug)
    > 💻 | ОС: Microsoft Windows 11
    > 🔧 | Процессор: 21.2%
    > ⚙ | Работает 97 часов (4 дней)
    > ❤ | [id322615766|VK+]
    """
    start = time()
    with open("config.json", "r", encoding="utf-8") as file:
        content = json.load(file)

    if content["debug"] is not True:
        end = time()
        result = round(end - start, 4)
        await edit_msg(
            bp.api,
            message,
            f"&#127955; | Понг!\n&#9201; | Ответ за {result} секунд (debug-Off)\n"
            f"&#128343; | Время: %c\n"
            f"&#128187; | ОС: {system} \n"
            f"&#128295; | Процессор: {cpu}\n"
            f"&#9881; | Бот работает {work_hours} часов, это({work_days} дней)\n"
            f"&#128214; | Цитата дня: random.choiceпинг{quote}\n"
            f"&#10084; | [vk.com/public210991551|Создатель]\n"
            f"&#128100; | [id314119670|Кодер/Тех-Админ]"
        )
    else:
        try:
            cpu = str(psutil.cpu_percent()) + "%"
        except PermissionError:
            cpu = "не известно (android?)"

        system_name = platform.system()

        """
        Если бот запущен на ОС Windows 11, то platform.release()
        вернет 10, что бы этого избежать, можно сделать проверку
        на версию системы:
        """
        if system_name == "Windows":
            if int(platform.version().split(".")[2]) > 20000:
                system_version = "11"
            else:
                system_version = platform.release()
        else:
            system_version = platform.release()

        system = system_name + " " + system_version
        with open("time_started.txt", "r", encoding="utf-8") as file:
            work_hours = round((round(time()) - int(file.read())) / 3600, 4)
        work_days = work_hours // 24
        end = time()
        result = round(end - start, 4)
        await edit_msg(
            bp.api, message,
            f"&#127955; | Понг!\n&#9201; | Ответ за {result} секунд (debug-Off)\n"
            f"&#128343; | Время: {datanow} \n"
            f"&#128187; | ОС: {system} \n"
            f"&#128295; | Процессор: {cpu}\n"
            f"&#9881; | Бот работает {work_hours} часов, это({work_days} дней)\n"
            f"&#128214; | Цитата запуска: {text}\n \n"
            f"&#10084; | [vk.com/public210991551|Создатель]\n"
            f"&#128100; | [id314119670|Кодер/Тех-Админ]"
        )
