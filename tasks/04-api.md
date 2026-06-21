# Задача 4: API эндпоинт

## Цель
Создать веб-API, чтобы анализатор можно было вызвать через HTTP-запрос (как настоящее приложение).

## Что нужно узнать

**API (Application Programming Interface)** — это способ, которым программы общаются друг с другом. Когда ты открываешь сайт, браузер отправляет запрос на сервер и получает ответ. Мы создадим такой сервер.

**FastAPI** — это фреймворк Python для создания API. Он простой и быстрый.

**Эндпоинт** — это адрес, на который можно отправить запрос. Например: `POST /analyze`

Пример простого API на FastAPI:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}
```

## Что нужно сделать

### 1. Создать файл `app/api.py`:

- Импортировать FastAPI
- Импортировать модели из `app/models.py`
- Импортировать функцию `analyze_cv` из `app/analyzer.py`
- Создать экземпляр FastAPI: `app = FastAPI(title="AI CV Match Analyzer")`
- Создать два эндпоинта:

**GET /** — проверка что сервер работает
```
Возвращает: {"status": "ok", "message": "AI CV Match Analyzer API"}
```

**POST /analyze** — анализ резюме
```
Принимает: AnalysisRequest (cv_text, job_description)
Вызывает: analyze_cv(request.cv_text, request.job_description)
Возвращает: AnalysisResponse с результатом
```

### 2. Обновить `main.py`:
- Импортировать `uvicorn`
- Импортировать `app` из `app.api`
- Запустить сервер: `uvicorn.run(app, host="0.0.0.0", port=8000)`

## Как проверить

1. Запусти сервер:
   ```bash
   python main.py
   ```

2. Открой в браузере: http://localhost:8000
   Должен увидеть: `{"status": "ok", "message": "AI CV Match Analyzer API"}`

3. Открой документацию: http://localhost:8000/docs
   Там можно протестировать API прямо в браузере

## Критерии приёмки

- [ ] Файл `app/api.py` создан
- [ ] GET `/` возвращает статус
- [ ] POST `/analyze` принимает текст CV и вакансии, возвращает результат анализа
- [ ] `main.py` запускает сервер через uvicorn
- [ ] Сервер запускается без ошибок
- [ ] API документация доступна на `/docs`

## Подсказки

- `@app.get("/")` — декоратор для GET-запроса
- `@app.post("/analyze")` — декоратор для POST-запроса
- Функция для POST-эндпоинта принимает параметр с типом модели: `def analyze(request: AnalysisRequest):`
- `uvicorn.run(app, host="0.0.0.0", port=8000)` — запуск сервера

## Git

```bash
git checkout -b task-04-api
git add app/api.py main.py
git commit -m "task-04: add FastAPI endpoints for CV analysis"
git push origin task-04-api
```
