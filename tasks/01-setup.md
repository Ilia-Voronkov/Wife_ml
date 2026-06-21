# Задача 1: Настройка проекта

## Цель
Настроить Python-проект так, чтобы он запускался и выводил сообщение в терминал.

## Что нужно сделать

1. Создать файл `requirements.txt` с содержимым:
   ```
   fastapi==0.115.0
   uvicorn==0.30.0
   ```

2. Создать файл `main.py`, который:
   - Печатает в терминал: `"AI CV Match Analyzer is starting..."`
   - Больше ничего пока не делает

3. Создать файл `app/__init__.py` (пустой файл — нужен, чтобы Python понимал, что `app` — это пакет)

## Как проверить

```bash
python main.py
```

Должно вывести:
```
AI CV Match Analyzer is starting...
```

## Критерии приёмки

- [ ] Файл `requirements.txt` создан с двумя зависимостями
- [ ] Файл `main.py` запускается без ошибок
- [ ] Файл `app/__init__.py` существует
- [ ] При запуске `python main.py` в терминале появляется сообщение

## Подсказки

- `print()` — функция для вывода текста в терминал
- `__init__.py` может быть полностью пустым файлом
- Не нужно пока ничего импортировать и устанавливать

## Git

```bash
git checkout -b task-01-setup
# ... делаешь задачу ...
git add requirements.txt main.py app/__init__.py
git commit -m "task-01: setup project with main.py and requirements"
git push origin task-01-setup
```
