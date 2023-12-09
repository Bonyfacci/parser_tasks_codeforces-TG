# Задача - ВВ4 - Парсер задач

---

<h3>Описание задачи:</h3>

На сайте codeforces есть большая подборка задач.<br>
Нужно создать парсер на каждую тему задач и выводить их в телеграм.

---

<h3>Стек технологий:</h3>

 - aiogram==3.2.0  
 - asyncpg==0.29.0
 - celery==5.3.6
 - coverage==7.3.2
 - Django==4.2.7
 - django-celery-beat==2.5.0
 - djangorestframework==3.14.0
 - eventlet==0.33.3
 - Pillow==10.1.0
 - psycopg2==2.9.9
 - pydantic==2.5.2
 - python-dotenv==1.0.0
 - redis==5.0.1
 - requests==2.31.0

---

<h3>Для запуска необходимо:</h3>

 - Клонировать проект на собственный диск в новом каталоге
 - Создать виртуальное окружение
 - Установить зависимости командой: pip install -r requirements.txt
 - Прописать переменные окружения в файле .env.sample
 - Создать базу данных (в данной работе используется PostgreSQL)
<br> psql -U postgres
<br> create database codeforces;
<br> \q
 - В терминале выполнить команды:
<br> python manage.py migrate
<br> python manage.py fill_db

---

<h3>Работа с Телеграм:</h3>

 - Для создания Telegram-бота найдите в чате самого главного бота: BotFather - https://t.me/BotFather.
 - Далее следуйте инструкциям и по завершении создания бота вам будет выдан токен. 
Его необходимо перенести в файл .env в поле TELEGRAM_API_TOKEN. 
Токен будет использован ботом для обращения к API Telegram-сервисов.
 - Для получения Вашего id Telegram найдите в чате бота: Get My ID - https://t.me/getmyid_bot. <br>
Его необходимо перенести в файл .env в поле TELEGRAM_ID.
 - В терминале выполнить команду:
<br> python manage.py tg_bot

Чтобы получить задачи по определенной теме с определенной сложностью напишите в чате:
 - flows/900
 - math/1500
 - games/2200

---

<h3>Работа с проектом:</h3>

 - Запустить Redis (в другом окне терминала под Ubuntu)
<br> sudo service redis-server start
 - Запустить celery (в другом окне терминала)
<br> celery -A config worker -l INFO -P eventlet
 - Запустить tasks (в другом окне терминала)
<br> celery -A config beat -l info -S django
 - Запустить сервер
<br> python manage.py runserver

---

<h3>Завершение работы:</h3>

 - Остановить Redis (терминала под Ubuntu)
<br> sudo service redis-server stop
 - Остановить сервер и celery
<br> Ctrl+C

---

<h3>Работа с проектом с использованием Docker выполняется с помощью последовательности команд</h3>

- docker-compose build - происходит сборка образа контейнера согласно инструкции в файле Dockerfile
- docker-compose up - происходит последовательный запуск всех контейнеров согласно инструкции в файле docker-compose.yaml

<h3>Завершение работы:</h3>

 - Остановить работу Docker
<br> Ctrl+C

---

<h3>Просмотр документации:</h3>

 - Выполнена документация API с помощью swagger и redoc.
