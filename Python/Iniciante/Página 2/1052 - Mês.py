meses = [
    {"n": 1, "name": "January"},
    {"n": 2, "name": "February"},
    {"n": 3, "name": "March"},
    {"n": 4, "name": "April"},
    {"n": 5, "name": "May"},
    {"n": 6, "name": "June"},
    {"n": 7, "name": "July"},
    {"n": 8, "name": "August"},
    {"n": 9, "name": "September"},
    {"n": 10, "name": "October"},
    {"n": 11, "name": "November"},
    {"n": 12, "name": "December"}
]

entrada = int(input())
for mes in meses:
    if entrada == mes["n"]:
        print(mes["name"])
