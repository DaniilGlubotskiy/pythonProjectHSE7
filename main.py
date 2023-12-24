import re
def validate_car_id(car_id):
    pattern = re.compile(r'^[АВЕКМНОРСТУХABEKMHOPCTYX]{1}\d{3}[АВЕКМНОРСТУХABEKMHOPCTYX]{2}\d{2,3}$')

    match = re.match(pattern, car_id)

    if match:
        region = car_id[-2:]
        return f"Номер {car_id[:6]} валиден. Регион: {region}."
    else:
        return "Номер не валиден."


# Ввод с клавиатуры
car_id_input = input("Введите транспортный номер: ")
result = validate_car_id(car_id_input)
print(result)
