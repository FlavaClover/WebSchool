from django.core.exceptions import ValidationError



def validate_day(value: int):
    if not 1 <= value <= 7:
        raise ValidationError(f"{value} is not number of day")


def validate_phone(value: str):
    valid = True
    if len(value) - 1 != 11:
        valid = False

    if value[0] != '+':
        valid = False

    if not valid:
        raise ValidationError(f"{value} is not telephone number")

    value = value[1:len(value)]
    for i in value:
        if not str.isdigit(i):
            raise ValidationError(f"{value} is not telephone number")

