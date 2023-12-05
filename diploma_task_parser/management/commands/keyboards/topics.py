from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Link', url='https://github.com/Bonyfacci')
    keyboard_builder.button(text='Profile', url='tg://user?id=6534158543')

    keyboard_builder.button(text='Показать темы задач', callback_data='topics')
    keyboard_builder.button(text='Топ 5 решённых задач', callback_data='top_5_solved')
    keyboard_builder.button(text='Топ 5 сложных задач', callback_data='top_5_rating')
    keyboard_builder.button(text='Топ 5 задач по баллам', callback_data='top_5_points')

    keyboard_builder.adjust(2, 1)
    return keyboard_builder.as_markup()


def get_inline_keyboard_rating():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_list = [
        '0', '<1000', '<1500',
        '<2000', '<2500', '<3000',
        '>3000'
    ]

    for rating in keyboard_list:
        keyboard_builder.button(text=f'{rating}', callback_data=f'rating_{rating}')

    keyboard_builder.adjust(3, 3, 1)
    return keyboard_builder.as_markup()
