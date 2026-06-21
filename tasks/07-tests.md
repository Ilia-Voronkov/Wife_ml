# Задача 7: Тесты

## Цель
Написать тесты, чтобы убедиться, что код работает правильно и не сломается при изменениях.

## Что нужно узнать

**Тесты** — это код, который проверяет другой код. Вместо того чтобы каждый раз вручную проверять "работает ли мой анализатор", мы пишем тест, который делает это автоматически.

**pytest** — популярная библиотека для тестов в Python.

Пример теста:
```python
def test_addition():
    assert 2 + 2 == 4  # Если не равно, тест упадёт
```

## Что нужно сделать

### 1. Обновить `requirements.txt`:
Добавить:
```
pytest==8.3.0
httpx==0.27.0
```

### 2. Создать файл `tests/__init__.py` (пустой)

### 3. Создать файл `tests/test_analyzer.py`:

Написать тесты для функции `analyze_cv`:

**test_perfect_match** — когда все навыки совпадают
- CV: "I know Python and SQL"
- Job: "Need Python and SQL"
- Score должен быть 100

**test_no_match** — когда ни один навык не совпадает
- CV: "I know painting and cooking"
- Job: "Need Python and Docker"
- Score должен быть 0

**test_partial_match** — когда часть навыков совпадает
- CV: "I know Python"
- Job: "Need Python, SQL and Docker"
- Matching: ["python"]
- Missing: ["sql", "docker"]

**test_empty_job** — когда вакансия без навыков
- CV: "I know Python"
- Job: "We need a good person"
- Score должен быть 0

### 4. Создать файл `tests/test_api.py`:

Написать тесты для API:

**test_root** — GET `/` возвращает статус ok

**test_analyze** — POST `/analyze` возвращает правильный результат

Используй `TestClient` из FastAPI:
```python
from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)
```

## Как проверить

```bash
pip install pytest httpx
pytest tests/ -v
```

Все тесты должны пройти (зелёные).

## Критерии приёмки

- [ ] `requirements.txt` обновлён
- [ ] `tests/__init__.py` создан
- [ ] `tests/test_analyzer.py` содержит минимум 4 теста
- [ ] `tests/test_api.py` содержит минимум 2 теста
- [ ] Все тесты проходят: `pytest tests/ -v`

## Подсказки

- `assert result["score"] == 100` — проверяет, что score равен 100
- `assert "python" in result["matching_skills"]` — проверяет, что "python" есть в списке
- `response = client.get("/")` — отправляет GET-запрос
- `response = client.post("/analyze", json={...})` — отправляет POST-запрос
- `response.status_code` — код ответа (200 = ок)
- `response.json()` — тело ответа как словарь

## Git

```bash
git checkout -b task-07-tests
git add tests/ requirements.txt
git commit -m "task-07: add unit tests for analyzer and API"
git push origin task-07-tests
```
