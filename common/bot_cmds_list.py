from aiogram.types import BotCommand

private = [
    BotCommand(command="start", description='Команда /start'),
    BotCommand(command="menu", description='Посмотреть меню'),
    BotCommand(command="about", description='Информация о магазине'),
    BotCommand(command="payment", description='Варианты оплаты'),
    BotCommand(command="shipping", description='Способы доставки'),
]