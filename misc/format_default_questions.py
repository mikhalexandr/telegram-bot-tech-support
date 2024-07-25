from config import TelegramTexts


def format_default_questions():
    res = ""
    for i, q in enumerate(TelegramTexts.QUESTIONS, start=1):
        s = f"{i}. <b>{q}</b> - <u>{TelegramTexts.QUESTIONS[q]}</u>\n"
        res += s
    return res if res else "В настоящий момент вопросы отсутствуют"
