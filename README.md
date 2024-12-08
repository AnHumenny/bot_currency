# Aiogram3 bot Application

Бот снимает курсы с ресурса https://myfin.by/, выводит в графики. Использует MySQL(MariaDB) в качестве базы данных.

Перед тем как начать, убедитесь, что у вас установлены следующие компоненты:

- **Python** (версия 3.11)
- **MariaDB** (версия 10+)
- **pip** 
- **virtualenv** (опционально)

## Установка

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows

## Установите зависимости:
pip install -r requirements.txt

Настройте базу данных:
Создайте базу данных в MariaDB и обновите настройки в settings.py вашего проекта:

API_TOKEN = 'TOKEN'
host='host'
port="port"
user="user"
password="password"
database="database"
tg_adm="tg администратора"
user_id="id пользователей"

##Запуск приложения
Чтобы запустить приложение, выполните следующую команду:
python3 bot.py



