from create import dp
from aiogram import types
from random import randint

total = 0  # количество конфет
count = False  # очередность хода
j = 0  # максимальное количество за 1 ход


@dp.message_handler(commands=['start'])
async def mas_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}! Мы будем играть с тобой в конфетки.\n'
                         f'Чтобы посмотреть правила игры, нажми\n/help')


@dp.message_handler(commands=['help'])
async def mas_help(message: types.Message):
    await message.answer('На столе лежат конфеты. Каждый игрок по очереди берет определенное число конфет. '
                         'Выигрывает тот, кто возьмет конфеты последний.\n'
                         'Для выбора начального количества конфет набери команду\n'
                         '/set нужное колличество и максимальное за один ход.')


@dp.message_handler(commands=['set'])
async def mas_total(message: types.Message):
    global total
    global j
    total = int(message.text.split()[1])
    j = int(message.text.split()[2])
    await message.answer(f'Количество конфет установлено - {total}.\n'
                         f'Максимальное количество конфет за 1 ход установлено - {j}.\n'
                         f'Кто ходит первый?\n'
                         f'Игрок - нажими /you\n'
                         f'Бот - нажими /bot\n'
                         f'Жеребьёвка - нажми /0 или /1')


@dp.message_handler(commands=['you'])
async def mas_gamer(message: types.Message):
    await message.answer(f'Введите кол-во конфет от 1 до {j}:\n')


@dp.message_handler(commands=['bot'])
async def mas_bot(message: types.Message):
    global count
    count = True
    await message.answer('Для продолжения введи любое сообщение.')


@dp.message_handler(commands=['0', '1'])
async def mas_cast(message: types.Message):
    global count
    x = int(message.text[1])
    rnd = randint(0, 1)
    if x == rnd:
        await message.answer(f'Выпало число: {rnd}.\nВы угадали, ходите первым!')
        await message.answer(f'Введите кол-во конфет от 1 до {j}:\n')

    else:
        await message.answer(f'Выпало число: {rnd}.\nВы не угадали,первым ходит ваш оппонент.')
        await message.answer('Для продолжения нажми любую кнопку')
        count = True


@dp.message_handler()
async def mas_all(message: types.Message):
    global total
    global count
    taken = message.text
    if not count:
        if total > 0:
            if taken.isdigit():
                if 0 < int(taken) < j + 1 or 0 < int(total) < j + 1:
                    if int(taken) <= total:
                        total -= int(taken)
                        count = True
                    else:
                        await message.answer('На столе осталось меньше конфет!')
                        await message.answer(f'Введите кол-во конфет от 1 до {total}:\n')

                else:
                    await message.answer('Неправильное колличество!')
                    await message.answer(f'Введите кол-во конфет от 1 до {j}:\n')

            else:
                await message.answer('Вы ввели не число!')
                await message.answer(f'Введите кол-во конфет от 1 до {j}:\n')
            if not total:
                await message.answer('Вы победили!')
                await message.answer('Для начала игры нажми\n'
                                     '/start')
        else:
            await message.answer('Для начала игры нажми\n'
                                 '/start')

    if total > 0:
        if count:
            if not total % (j + 1):
                taken = randint(1, 28)
            else:
                taken = total % (j + 1)
            total -= taken
            await message.answer(f'Ваш аппонент взял:\n{taken}')
            count = False
            if not total:
                await message.answer('Вы проиграли :(')
                await message.answer('Для начала игры нажми\n'
                                     '/start')
            else:
                await message.answer(f'Остаток конфет равен:\n{total}')
                await message.answer(f'Введите кол-во конфет от 1 до {j}:\n')
    # else:
    #     await message.answer('Для начала игры нажми\n'
    #                              '/start')
