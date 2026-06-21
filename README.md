# AI CV Match Analyzer

Приложение для сравнения резюме (CV) с описанием вакансии.

## Что делает приложение

- Принимает текст резюме и текст вакансии
- Анализирует совпадение навыков
- Возвращает:
  - **Match Score** — оценка совпадения (0–100%)
  - **Strong Skills** — навыки, которые совпали
  - **Missing Skills** — навыки, которых не хватает
  - **Suggestions** — рекомендации по улучшению резюме

## Технологии

- Python 3.11+
- FastAPI (backend API)
- Claude API (AI-анализ)
- HTML/CSS/JS (frontend)

## Как начать

```bash
# 1. Клонировать репозиторий
git clone <url>
cd ai-cv-match-analyzer

# 2. Создать виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Запустить
python main.py
```

## Структура проекта

```
├── main.py              # Точка входа
├── requirements.txt     # Зависимости Python
├── app/
│   ├── analyzer.py      # Логика анализа CV
│   ├── api.py           # API эндпоинты
│   └── models.py        # Модели данных
├── frontend/
│   ├── index.html       # Главная страница
│   ├── style.css        # Стили
│   └── script.js        # Логика фронтенда
├── tasks/               # Задачи для выполнения
│   ├── 01-setup.md
│   ├── 02-analyzer.md
│   ├── ...
└── tests/               # Тесты
```

## Рабочий процесс

1. Прочитай задачу в папке `tasks/`
2. Создай новую ветку: `git checkout -b task-01-setup`
3. Сделай задачу
4. Закоммить: `git add . && git commit -m "описание"`
5. Запушь: `git push origin task-01-setup`
6. Создай Pull Request на GitHub
7. Пройди ревью
