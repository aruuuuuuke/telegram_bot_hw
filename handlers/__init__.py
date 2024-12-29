from aiogram import Router, F

from .start import start_router
from .menu import menu_router
from .random_meal import random_meal_router
from .other_messages import echo_handlr
from .review_dialog import otzyv_router
from .admin import admin_router

private_router = Router()

private_router.include_router(start_router)
private_router.include_router(admin_router)
private_router.include_router(otzyv_router)
private_router.include_router(menu_router)
private_router.include_router(random_meal_router)
private_router.include_router(echo_handlr)

private_router.message.filter(F.chat.type == 'private')
private_router.callback_query.filter(F.chat.type == 'private')
