from create import dp
from aiogram import types
from random import randint
from keybords import kb_main_menu
from datetime import datetime
import functions


total = 0  # количество конфет
count = False  # очередность хода
j = 0  # максимальное количество за 1 ход
user_list =[]



@dp.message_handler(commands=['start'])
async def mas_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}! Мы будем играть с тобой в конфетки.\n'
                         f'Чтобы посмотреть правила игры, нажми\n/help\n'
                         f'Для начала игры\n/new_game',
                         reply_markup=kb_main_menu)
    await message.delete()


@dp.message_handler(commands=['help'])
async def mas_help(message: types.Message):
    await message.answer('На столе лежат конфеты. Каждый игрок по очереди берет определенное число конфет.\n'
                         'Выигрывает тот, кто возьмет конфеты последний.')
    await message.delete()


@dp.message_handler(commands=['new_game'])
async def mas_help(message: types.Message):
    await message.answer('Выбери начальное количество конфет от 10шт. командой:\n'
                         '/set и через пробел колличество.\n')
    await message.delete()
    global user_list
    user_list = [datetime.now().strftime('%d-%b-%y %H:%M:%S'), message.from_user.full_name, message.from_user.username]



@dp.message_handler(commands=['set'])
async def mas_total(message: types.Message):
    global total
    global j
    if not message.text[-1].isdigit():
        await message.answer('Для выбора начального количества конфет набери команду:\n'
                             '/set и через пробел колличество от 10шт.\n')
    else:
        if message.text.split()[1].isdigit():
            total = int(message.text.split()[1])
            if total >= 10:
                j = randint(2, total // 2 - 2)
                await message.answer(f'Общее количество конфет установлено: {total}.\n'
                                     f'\nУстанови максимальное количество,которое можно взять за 1 ход командой:\n'
                                     f'/max и через пробел колличество от 2шт. до {total // 2 - 2}шт,\n'
                                     f'либо сразу выбирай кто ходит первый:\n\n'
                                     f'Игрок - нажими /you\n'
                                     f'Бот - нажими /bot\n'
                                     f'Жеребьёвка - нажми /0 или /1')
            else:
                await message.answer('Задай значение от 10шт.!\n\n'
                                     'Набери команду:\n'
                                     '/set и через пробел колличество от 10шт.\n')
        else:
            await message.answer('Для выбора начального количества конфет набери команду:\n'
                                 '/set и через пробел колличество от 10шт.\n')
    await message.delete()


@dp.message_handler(commands=['max'])
async def mas_total(message: types.Message):
    global j
    if not message.text[-1].isdigit():
        await message.answer('Для выбора максимального количества за ход набери команду:\n'
                             f'/max и через пробел колличество от 2 до {total // 2 - 2}.\n')
    else:
        if message.text.split()[1].isdigit():
            j = int(message.text.split()[1])
            if 1 < j <= total//2 - 2:
                await message.answer(f'Максимальное количество конфет за 1 ход установлено: {j}.\n'
                                     f'Кто ходит первый?\n'
                                     f'Игрок - нажими /you\n'
                                     f'Бот - нажими /bot\n'
                                     f'Жеребьёвка - нажми /0 или /1')
            else:
                await message.answer(f'Задай значение от 2 до {total // 2 - 2}!\n\n'
                                     'Набери команду:\n'
                                     f'/max и через пробел колличество от 2 до {total//2 - 2}\n')
        else:
            await message.answer('Для выбора максимального количества за ход набери команду\n'
                                 f'/max и через пробел колличество от 2 до {total // 2 - 2}.\n')
    await message.delete()



@dp.message_handler(commands=['you'])
async def mas_gamer(message: types.Message):
    await message.answer(f'Введи кол-во конфет от 1 до {j}:\n')
    await message.delete()


@dp.message_handler(commands=['bot'])
async def mas_bot(message: types.Message):
    global count
    count = True
    await message.answer('Для продолжения введи любое сообщение.')
    await message.delete()
    await message.delete()

@dp.message_handler(commands=['0', '1'])
async def mas_cast(message: types.Message):
    global count
    x = int(message.text[1])
    rnd = randint(0, 1)
    if x == rnd:
        await message.answer(f'Выпало число: {rnd}.\nУгадал, ходи первым!')
        await message.answer(f'Введите кол-во конфет от 1 до {j}:\n')

    else:
        await message.answer(f'Выпало число: {rnd}.\nНе угадал,первым ходит бот.')
        await message.answer('Для продолжения введи любое сообщение.')
        count = True


@dp.message_handler()
async def mas_all(message: types.Message):
    await functions.player_takes(message)
    await functions.bot_takes(message)
    # if total > 0:
    #     await functions.countdown(message)
