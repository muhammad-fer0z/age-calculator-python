from datetime import date


def age_calculator(year, month, day):
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age
