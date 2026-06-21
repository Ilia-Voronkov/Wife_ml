# Задача 3: Базовый анализатор (без AI)

## Цель
Написать простую функцию, которая сравнивает текст резюме с текстом вакансии — пока без AI, просто по ключевым словам.

## Что нужно узнать

Прежде чем подключать AI, полезно написать простую версию. Это называется **MVP (Minimum Viable Product)** — минимально работающий продукт.

Наш простой алгоритм:
1. Берём текст вакансии
2. Находим в нём ключевые навыки (Python, SQL, Git и т.д.)
3. Проверяем, какие из них есть в резюме
4. Считаем процент совпадения

## Что нужно сделать

Создать файл `app/analyzer.py` с функцией:

```python
def analyze_cv(cv_text: str, job_description: str) -> dict:
```

Функция должна:

1. Иметь список известных навыков (skills), например:
   ```python
   KNOWN_SKILLS = [
       "python", "javascript", "sql", "git", "docker",
       "fastapi", "react", "html", "css", "linux",
       "aws", "postgresql", "mongodb", "redis", "api",
       "machine learning", "deep learning", "nlp",
       "pandas", "numpy", "scikit-learn", "tensorflow",
       "pytorch", "data analysis", "statistics"
   ]
   ```

2. Привести оба текста к нижнему регистру (`.lower()`)

3. Найти, какие навыки из `KNOWN_SKILLS` упоминаются в вакансии — это `required_skills`

4. Найти, какие из `required_skills` есть в резюме — это `matching_skills`

5. Найти, каких навыков нет в резюме — это `missing_skills`

6. Посчитать score: `len(matching_skills) / len(required_skills) * 100`
   (если `required_skills` пустой — score = 0)

7. Создать список suggestions:
   - Для каждого missing skill добавить: `"Добавьте навык: {skill}"`

8. Вернуть словарь:
   ```python
   {
       "score": score,
       "matching_skills": matching_skills,
       "missing_skills": missing_skills,
       "suggestions": suggestions
   }
   ```

## Как проверить

```bash
python -c "
from app.analyzer import analyze_cv
result = analyze_cv('I know Python and SQL', 'We need Python, SQL and Docker')
print(result)
"
```

Ожидаемый результат (примерно):
```
{'score': 66, 'matching_skills': ['python', 'sql'], 'missing_skills': ['docker'], 'suggestions': ['Добавьте навык: docker']}
```

## Критерии приёмки

- [ ] Файл `app/analyzer.py` создан
- [ ] Функция `analyze_cv` принимает два текста и возвращает словарь
- [ ] Score считается правильно
- [ ] Matching skills определяются правильно
- [ ] Missing skills определяются правильно
- [ ] Suggestions генерируются для каждого missing skill

## Подсказки

- `.lower()` переводит текст в нижний регистр: `"Hello".lower()` → `"hello"`
- `if skill in text` — проверяет, есть ли слово в тексте
- `round()` — округляет число: `round(66.666)` → `67`
- Список можно создать через цикл или list comprehension

## Git

```bash
git checkout -b task-03-analyzer
# ... делаешь задачу ...
git add app/analyzer.py
git commit -m "task-03: add basic CV analyzer with keyword matching"
git push origin task-03-analyzer
```
