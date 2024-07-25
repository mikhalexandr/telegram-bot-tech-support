from dotenv import load_dotenv
import os


load_dotenv()


class TelegramConfig:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID"))


class TelegramTexts:
    GREETING = (
        "Здравствуй, дорогой пользователь [имя сервиса]. "
        "Здесь ты можешь задать свой вопрос или оставить отзыв о [имя сервиса]."
    )

    QUESTIONS = {
        "Вопрос1": "Ответ на 1-й вопрос",
        "Вопрос2": "Ответ на 2-й вопрос",
        "Вопрос3": "Ответ на 3-й вопрос",
        "Вопрос4": "Ответ на 4-й вопрос",
    }
