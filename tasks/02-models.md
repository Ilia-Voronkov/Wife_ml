# Задача 2: Модели данных

## Цель
Создать модели данных — описать, какие данные приложение принимает и отдаёт.

## Что нужно узнать

**Pydantic** — это библиотека Python, которая помогает описывать структуру данных. Например, если мы хотим сказать "резюме — это текст, а оценка — это число от 0 до 100", Pydantic поможет это описать и проверить.

Пример:
```python
from pydantic import BaseModel

class Dog(BaseModel):
    name: str
    age: int
```

Это значит: у собаки есть имя (текст) и возраст (число).

## Что нужно сделать

Создать файл `app/models.py` с двумя моделями:

### 1. `AnalysisRequest` — что приложение получает
- `cv_text` (str) — текст резюме
- `job_description` (str) — текст вакансии

### 2. `AnalysisResponse` — что приложение отдаёт
- `score` (int) — оценка совпадения от 0 до 100
- `matching_skills` (list[str]) — список совпавших навыков
- `missing_skills` (list[str]) — список недостающих навыков
- `suggestions` (list[str]) — список рекомендаций

## Как проверить

```bash
python -c "from app.models import AnalysisRequest, AnalysisResponse; print('Models OK')"
```

Должно вывести `Models OK` без ошибок.

## Критерии приёмки

- [ ] Файл `app/models.py` создан
- [ ] Класс `AnalysisRequest` содержит поля `cv_text` и `job_description`
- [ ] Класс `AnalysisResponse` содержит поля `score`, `matching_skills`, `missing_skills`, `suggestions`
- [ ] Оба класса наследуются от `BaseModel`
- [ ] Импорт работает без ошибок

## Подсказки

- `list[str]` означает "список строк", например `["Python", "SQL"]`
- `int` — целое число
- `str` — строка (текст)
- Каждая модель — это класс, который наследуется от `BaseModel`

## Git

```bash
git checkout -b task-02-models
# ... делаешь задачу ...
git add app/models.py
git commit -m "task-02: add request and response models"
git push origin task-02-models
```
