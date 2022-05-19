from datetime import datetime


# Utils for saving words register
def get_word_register(word: str) -> str:
    if word.isupper():
        return "all_upper"
    elif word.istitle():
        return "title"
    return "lower"


def apply_word_register(word: str, register_data: str) -> str:
    if register_data == "all_upper":
        return word.upper()
    elif register_data == "title":
        return word.title()
    return word


# Months replacing
def get_ukrainian_date(date: datetime) -> str:
    months_data: dict = {
        "January": "Січень",
        "February": "Лютий",
        "March": "Березень",
        "April": "Квітень",
        "May": "Травень",
        "June": "Червень",
        "July": "Липень",
        "August": "Серпень",
        "September": "Вересень",
        "October": "Жовтень",
        "November": "Листопад",
        "December": "Грудень",
    }
    date_string = date.strftime("%d %B %Y")
    for english_month in months_data:
        if english_month not in date_string:
            continue
        ukrainian_date = date_string.replace(english_month, months_data[english_month])
        return ukrainian_date
