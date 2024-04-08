
# Проект Achievements

---

## Описание проекта

---

Проект позволяет хранить и присваивать достижения пользователям. В проекте есть 
следующие функции:
- Предоставление информации о пользователе
- Предоставление информации о выданных пользователю достижениях на выбранном пользователем языке
- Предоставление информации обо всех доступных достижениях
- Добавление достижений
- Присваивание достижений пользователям с сохранением даты выдачи
- Предоставление статистических данных системы:
  - пользователь с максимальным количеством достижений
  - пользователь с максимальным количеством очков достижений
  - пользователь с максимальной разностью очков достижений
  - пользователь с минимальной разностью очков достижений
  - пользователи, которым достижения выдавались 7 дней подряд

## Запуск проекта с помощью Docker

---

Для запуска проекта необходим [Docker](https://www.docker.com/)

Также в директории `/backend` необходимо создать файл `.env`, в котором должны 
быть указаны:
- POSTGRES_DB - Название БД
- POSTGRES_USER - Пользователя для подключения к БД
- POSTGRES_PASSWORD - Пароль пользователя
- DB_HOST - Хост, на котором будет БД
- DB_PORT - Порт БД

Пример находится в файле `/backend/example.env`

```dotenv
POSTGRES_DB=achievements
POSTGRES_USER=achievements_admin
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```

После этого в корневой директории проекта `/achievements` в терминале необходимо перейти в директорию `/infra` и
 выполнить команду:
```commandline
docker-compose up --build
```

После запуска проекта в корневой директории выполнить команду:
```commandline
docker exec app alembic upgrade head
```

Импортировать данные можно из корневой директории командой:
```commandline
docker exec -i db psql -d achievements -U achievements_admin < backend/achievements.back
```

#### Проект будет доступен по адресу [http://127.0.0.1/](http://127.0.0.1/)


## API Эндпоинты

---

### Пользователи:

- #### GET /api/v1/users/{user_id}/ - Получение информации о пользователе

Пример ответа:
```json
{
  "id": 1,
  "username": "DenisEpic",
  "language": "ru",
  "achievements": [
    {
      "name": "Nostalgy",
      "points": 10,
      "description_ru": "Скачать игру дества и перепройти её",
      "description_en": "Download the childhood game and replay it",
      "id": 1,
      "timestamp": "2024-03-17T00:00:00"
    }
  ]
}
```

- #### GET /api/v1/users/{user_id}/achievements/ - Получение информации о выданных пользователю достижениях на выбранном пользователем языке

Пример ответа:
```json
[
  {
    "name": "Nostalgy",
    "points": 10,
    "id": 1,
    "description": "Скачать игру дества и перепройти её",
    "timestamp": "2024-03-17T00:00:00"
  }
]
```

---

### Достижения:

- #### GET /api/v1/achievements/ - Предоставление информации обо всех доступных достижениях

Пример ответа:
```json
[
  {
    "name": "Nostalgy",
    "points": 10,
    "description_ru": "Скачать игру дества и перепройти её",
    "description_en": "Download the childhood game and replay it",
    "id": 1
  }
]
```

- #### POST /api/v1/achievements/ - Добавление достижения

Тело запроса:
```json
{
  "name": "New achievement",
  "points": 20,
  "description_ru": "Русское описание",
  "description_en": "English description"
}
```
Пример ответа:
```json
{
  "name": "New achievement",
  "points": 20,
  "description_ru": "Русское описание",
  "description_en": "English description",
  "id": 8
}
```

- #### POST /api/v1/achievements/set/ - Выдача достижения пользователю

Тело запроса:
```json
{
  "user_id": 2,
  "achievement_id": 8
}
```
Пример ответа:
```json
{
  "id": 2,
  "username": "IvanGuru",
  "language": "ru",
  "achievements": [
    {
      "name": "New achievement",
      "points": 20,
      "description_ru": "Русское описание",
      "description_en": "English description",
      "id": 8,
      "timestamp": "2024-03-17T00:00:00"
    }
  ]
}
```

---

### Статистика:

- #### GET /api/v1/statistics/max-achievements-count/ - Получение пользователя с максимальным количеством достижений
- #### GET /api/v1/statistics/max-achievements-points/ - Получение пользователя с максимальным количеством очков достижений
- #### GET /api/v1/statistics/max-difference-points/ - Получение пользователя с максимальной разницей очков достижений
- #### GET /api/v1/statistics/min-difference-points/ - Получение пользователя с минимальной разницей очков достижений

Пример ответов на данные эндпоинты:
```json
{
  "id": 1,
  "username": "DenisEpic",
  "language": "ru",
  "achievements": [
    {
      "name": "Nostalgy",
      "points": 10,
      "description_ru": "Скачать игру дества и перепройти её",
      "description_en": "Download the childhood game and replay it",
      "id": 1,
      "timestamp": "2024-03-17T00:00:00"
    }
  ]
}
```

- #### GET /api/v1/statistics/achievements-week-for-a-row/ - Получение пользователей, которым достижения выдавались 7 дней подряд

Пример ответа:
```json
[
  {
    "id": 1,
    "username": "DenisEpic",
    "language": "ru",
    "achievements": [
      {
        "name": "Nostalgy",
        "points": 10,
        "description_ru": "Скачать игру дества и перепройти её",
        "description_en": "Download the childhood game and replay it",
        "id": 1,
        "timestamp": "2024-03-17T00:00:00"
      },
      {
        "name": "Jeweler",
        "points": 25,
        "description_ru": "Открыл баночку йода, не обработав окружающие объекты",
        "description_en": "Opened a jar of iodine without treating surrounding objects",
        "id": 2,
        "timestamp": "2024-03-16T00:00:00"
      },
      {
        "name": "Cat Ninja",
        "points": 40,
        "description_ru": "Вылез из под одеяла, на котором лежит кот, не потревожив его",
        "description_en": "Crawled out from under the blanket on which the cat",
        "id": 3,
        "timestamp": "2024-03-15T00:00:00"
      },
      {
        "name": "Archaeologist",
        "points": 37,
        "description_ru": "Установить ICQ",
        "description_en": "Install ICQ",
        "id": 4,
        "timestamp": "2024-03-12T00:00:00"
      },
      {
        "name": "Drozdov",
        "points": 30,
        "description_ru": "Пересчитать всех жуков во дворе",
        "description_en": "Count all the bugs in the yard",
        "id": 5,
        "timestamp": "2024-03-13T00:00:00"
      },
      {
        "name": "Veni Vidi Vici",
        "points": 35,
        "description_ru": "Сдать экзамен без подготовки",
        "description_en": "Pass the exam without preparation",
        "id": 6,
        "timestamp": "2024-03-14T00:00:00"
      },
      {
        "name": "Flat Earth Believer",
        "points": 40,
        "description_ru": "Доказать, что Земля плоская",
        "description_en": "Prove that the Earth is flat",
        "id": 7,
        "timestamp": "2024-03-11T00:00:00"
      }
    ]
  }
]
```

После запуска проекта документация API также будет доступна по адресам [http://127.0.0.1/docs](http://127.0.0.1/docs)
и [http://127.0.0.1/redoc](http://127.0.0.1/redoc)


## Технологии

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="python" alt="python" width="40" height="40"/>&nbsp
  <img src="https://github.com/devicons/devicon/blob/master/icons/fastapi/fastapi-plain.svg" title="fastapi" alt="fastapi" width="40" height="40"/>&nbsp
  <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original.svg" title="postgresql" alt="postgresql" width="40" height="40"/>&nbsp
  <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="docker" alt="docker" width="40" height="40"/>&nbsp
</div>

В проекте используются следующие технологии:
- Python 3.11
- FastAPI
- Alembic
- SQLAlchemy
- PostgreSQL
- Docker
- Nginx


## Автор

[Степаненко Станислав](https://t.me/tme_zoom)

[![Telegram Badge](https://img.shields.io/badge/StepanenkoStanislav-blue?logo=telegram&logoColor=white)](https://t.me/tme_zoom) [![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat&logo=Gmail&logoColor=white)](mailto:stepanenko.s.a.dev@gmail.com)
