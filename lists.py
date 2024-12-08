import os

abs_path = f"{os.getcwd()}/image/"
check_list = ["USD", "EUR", "RUB", "CNY"]

helps = [
    "/actual - текущий статус"
    "/image - сохранённая графика"
]

list_url = [
    "https://myfin.by/currency/torgi-na-bvfb/kurs-dollara",
    "https://myfin.by/currency/torgi-na-bvfb/kurs-euro",
    "https://myfin.by/currency/torgi-na-bvfb/kurs-rublya",
    "https://myfin.by/currency/torgi-na-bvfb/kurs-cny"
]

id_user = os.getenv("id_user")

