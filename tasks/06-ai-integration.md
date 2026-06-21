# Задача 6: Интеграция с AI (Claude API)

## Цель
Заменить простой анализатор на настоящий AI-анализ с помощью Claude API.

## Что нужно узнать

**Claude API** — это сервис от Anthropic, который позволяет отправлять текст и получать умный ответ. Мы отправим резюме и вакансию, а Claude проанализирует их и вернёт структурированный результат.

**API ключ** — это секретный код для доступа к сервису. Его нельзя хранить в коде — он хранится в файле `.env`.

**Промпт (prompt)** — это инструкция для AI. Чем точнее промпт, тем лучше результат.

## Что нужно сделать

### 1. Обновить `requirements.txt`:
Добавить:
```
anthropic==0.40.0
python-dotenv==1.0.1
```

### 2. Создать файл `.env` (НЕ коммитить!):
```
ANTHROPIC_API_KEY=your-api-key-here
```

### 3. Создать файл `app/ai_analyzer.py`:

- Импортировать `anthropic` и `os`
- Загрузить API ключ из переменной окружения
- Создать функцию `analyze_cv_with_ai(cv_text: str, job_description: str) -> dict`
- Функция должна:
  1. Составить промпт для Claude, который просит:
     - Сравнить резюме с вакансией
     - Вернуть JSON с полями: score, matching_skills, missing_skills, suggestions
  2. Отправить запрос к Claude API
  3. Распарсить JSON из ответа
  4. Вернуть результат как словарь

### 4. Обновить `app/api.py`:
- Добавить новый эндпоинт `POST /analyze/ai` который использует `analyze_cv_with_ai`
- Старый эндпоинт `POST /analyze` оставить (как fallback без AI)

## Пример промпта для Claude

```
Ты — эксперт по подбору персонала. Сравни резюме кандидата с описанием вакансии.

Резюме:
{cv_text}

Вакансия:
{job_description}

Верни результат строго в формате JSON:
{
  "score": <число от 0 до 100>,
  "matching_skills": [<список совпавших навыков>],
  "missing_skills": [<список недостающих навыков>],
  "suggestions": [<список рекомендаций по улучшению резюме>]
}

Верни ТОЛЬКО JSON, без дополнительного текста.
```

## Как проверить

1. Убедись, что в `.env` указан настоящий API ключ
2. Запусти сервер: `python main.py`
3. Открой http://localhost:8000/docs
4. Протестируй эндпоинт `/analyze/ai`

## Критерии приёмки

- [ ] `requirements.txt` обновлён
- [ ] Файл `app/ai_analyzer.py` создан
- [ ] Функция отправляет запрос к Claude API
- [ ] Промпт чёткий и возвращает JSON
- [ ] Новый эндпоинт `/analyze/ai` работает
- [ ] `.env` добавлен в `.gitignore` (уже должен быть!)
- [ ] API ключ НЕ закоммичен

## Подсказки

- `anthropic.Anthropic()` — создаёт клиент (автоматически берёт ключ из переменной окружения)
- `client.messages.create(model="claude-sonnet-4-20250514", ...)` — отправляет запрос
- `json.loads()` — парсит JSON-строку в словарь Python
- `from dotenv import load_dotenv; load_dotenv()` — загружает переменные из `.env`

## Git

```bash
git checkout -b task-06-ai
git add app/ai_analyzer.py app/api.py requirements.txt
# НЕ добавляй .env!
git commit -m "task-06: integrate Claude API for AI-powered analysis"
git push origin task-06-ai
```
