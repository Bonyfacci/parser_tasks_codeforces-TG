from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text='Начать работу!')

    keyboard_builder.button(text='Кинуть кубик')
    keyboard_builder.button(text='Боулинг')
    keyboard_builder.button(text='Рулетка')
    keyboard_builder.button(text='Дартс')
    keyboard_builder.button(text='Футбол')
    keyboard_builder.button(text='Баскетбол')

    keyboard_builder.button(text='Отправить геолокацию', request_location=True)
    keyboard_builder.button(text='Отправить свой контакт', request_contact=True)

    keyboard_builder.adjust(1, 3, 3, 2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder='Начни работу или испытай удачу!'
    )
