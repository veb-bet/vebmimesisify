<p align="center">
  <img src="https://github.com/veb-bet/vebfs/raw/ff362f8f30d1a9debc566ff5ed54a5bcca221b43/docs/bat_image.png" alt="vebfs logo" width="150"/>
</p>

# vebmimesisify

**vebmimesisify** — это библиотека для генерации случайных сценариев, диалогов, событийных логов, профилей пользователей, блог-постов, комментариев и веб-событий. Отлично подходит для генерации тестовых данных, случайных описаний и повествований.

## Установка

```bash
pip install vebmimesisify
```

## Использование

```python
from vebmimesisify import (
    generate_scenario,
    generate_dialogue,
    generate_event_log,
    generate_user_profile,
    generate_blog_post,
    generate_comment,
    generate_web_event
)
from mimesis.locales import Locale

# Генерация сценария с выбором жанра и языка
print(generate_scenario(genre="fantasy", locale=Locale.EN))

# Генерация диалога на русском
print(generate_dialogue(locale=Locale.RU))

# Генерация логов событий
print(generate_event_log(3))

# Генерация профиля пользователя
profile = generate_user_profile()
print(profile)

# Генерация блог-поста
post = generate_blog_post()
print(f"Title: {post['title']}\nContent: {post['content']}")

# Генерация комментария
print(generate_comment())

# Генерация веб-события
print(generate_web_event())
```

## Функции

- `generate_scenario(genre="mystery", locale=Locale.EN)`: Генерирует случайный сценарий истории. Жанры: 'mystery', 'fantasy', 'romance', 'sci-fi'.
- `generate_dialogue(locale=Locale.EN)`: Генерирует диалог между двумя людьми.
- `generate_event_log(n=5, locale=Locale.EN)`: Генерирует n записей событийного лога.
- `generate_user_profile(locale=Locale.EN)`: Генерирует профиль пользователя (имя, email, адрес и т.д.).
- `generate_blog_post(locale=Locale.EN)`: Генерирует блог-пост с заголовком и содержимым.
- `generate_comment(locale=Locale.EN)`: Генерирует случайный комментарий.
- `generate_web_event(locale=Locale.EN)`: Генерирует запись веб-события (доступ к странице).

## Тестирование

Для запуска тестов:

```bash
pip install -e .[dev]
pytest
```

## Лицензия

BSD-2-Clause
