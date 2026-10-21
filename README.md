# Лабораторная работа № 9: автотесты в GitHub Actions

Автоматический запуск 21 модульной проверки класса `Calculator` из лабораторной работы № 6 курса «Тестирование программного обеспечения».

Проверяются сложение, деление, исключение при делении на ноль и определение простого числа. Исходные приложение и тесты перенесены без изменений.

## Локальный запуск

Требуется Python 3.13. Из корня репозитория:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

В Windows вместо `source` выполнить `.venv\Scripts\activate`.

Зависимость зафиксирована в `requirements.txt`. Установка требует доступа к PyPI; сами тесты выполняются без сети.

## Автоматический запуск

Workflow `.github/workflows/run-tests.yml` запускается при каждом `push`, при открытии и обновлении pull request в `main`, а также вручную: **Actions → Run tests → Run workflow**.

Задача на `ubuntu-latest` получает код, настраивает Python 3.13, устанавливает зависимости и запускает `python -m pytest -v`. Ненулевой код завершения pytest приводит к ошибке задачи. Ожидаемый результат — **21 passed**, итоговый статус **Success**.

## Материалы

- `calculator.py` — класс Calculator;
- `test_calculator.py` — 21 параметризованная проверка;
- `requirements.txt` — зависимость pytest;
- `results/` — фактические результаты;
- [отчёт.md](отчёт.md) — отчёт по работе;
- `скриншоты/` — подтверждения успешного запуска GitHub Actions.

Подтверждённый запуск: [Run tests № 1 — Success](https://github.com/despyzz/tpo-lab09/actions/runs/39639389142), **21 passed**.
