import string
from random import randint
from asyncio import sleep
import handlers


async def player_takes(message):
    taken = message.text
    if not handlers.count:
        if handlers.total > 0:
            if taken.isdigit():
                if 0 < int(taken) <= handlers.j:
                    handlers.total -= int(taken)
                    handlers.count = True
                else:
                    await message.answer('Неправильное колличество!')
                    await message.answer(f'Введи кол-во конфет от 1 до {handlers.j}:\n')

            else:
                await message.answer('Это не число!')
                await message.answer(f'Введи кол-во конфет от 1 до {handlers.j}:\n')
            if not handlers.total:
                handlers.user_list.append("Победил")
                with open('log.txt', 'a', encoding='UTF-8') as data:
                    data.write(' | '.join(list(map(str, handlers.user_list))) + '\n')
                await message.answer('Ты победил!')
                await message.answer('Для начала игры нажми\n'
                                     '/start')
        else:
            await message.answer('Для начала игры нажми\n'
                                 '/start')


async def bot_takes(message):
    if handlers.total > 0:
        if handlers.count:
            if not handlers.total % (handlers.j + 1):
                taken = randint(1, handlers.j)
            else:
                taken = handlers.total % (handlers.j + 1)
            handlers.total -= taken
            await message.answer(f'Бот взял:\n{taken}')
            handlers.count = False
            if not handlers.total:
                handlers.user_list.append("Проиграл")
                with open('log.txt', 'a', encoding='UTF-8') as data:
                    data.write(' | '.join(list(map(str, handlers.user_list))) + '\n')
                await message.answer('Ты проиграл :(')
                await message.answer('Для начала игры нажми\n'
                                     '/start')
            else:
                await message.answer(f'Остаток конфет равен:\n{handlers.total}')
                await message.answer(f'Введи кол-во конфет от 1 до {handlers.j}:\n')


# async def countdown(message):
#     await message.answer('У тебя 10 секунд на обдумывание хода...')
#     await sleep(6)
#     await message.answer('3...')
#     await sleep(1)
#     await message.answer('2...')
#     await sleep(1)
#     await message.answer('1...')
#     await sleep(1)
#     await message.answer('Переход хода')
#     handlers.count = True


