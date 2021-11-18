# Картинки космоса там вроде

Выкладывание изображений космоса в телеграм канал при помощи бота

### Как установить

Для того чтобы программа работала нужно:
1. Получить API токен на [https://api.nasa.gov](https://api.nasa.gov)
2. Создать публичный телеграм канал
3. Создать телеграм бота при помощи [@BotFather](https://telegram.me/BotFather) в телеграм

Далее нужно будет создать в корневой папке программы файл ".env" и добавить в него:
```
NASA_TOKEN=ваш токен nasa
TELEGRAM_TOKEN=токен вашего телеграм бота
TELEGRAM_CHAT_ID=chat id вашего телеграм канала
TELEGRAM_POSTING_DELAY=задержка между постами в секундах
```

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Примеры запуска

Откройте cmd, войдите в корневую папку программы и введите команды:
```
cd "путь к корневой папке программы"
python main.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).