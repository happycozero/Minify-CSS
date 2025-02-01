# Minify-CSS (Минификация CSS)

Скрипт на Python предназначен для обработки CSS-файлов: он удаляет дублирующиеся селекторы из второго файла (сравниваемого), оставляя только уникальные и минимизируя итоговый CSS.

## Описание работы кода:

### Загрузка и парсинг CSS:
- Скрипт загружает два CSS-файла — исходный и сравниваемый.
- Используются библиотеки `tinycss2` для парсинга CSS и `csscompressor` для минимизации итогового CSS.

### Извлечение уникальных селекторов:
- Из исходного CSS-файла извлекаются все селекторы.
- Эти селекторы используются для сравнения с селекторами второго файла, чтобы удалить дубли.

### Удаление дубликатов и минимизация CSS:
- Сравниваются селекторы двух файлов, и все дублирующиеся селекторы из второго файла удаляются.
- Полученный уникальный CSS код затем минимизируется с помощью библиотеки `csscompressor`, чтобы уменьшить его размер.

### Запись в новый файл:
- Минимизированный и очищенный от дубликатов CSS сохраняется в новый файл.

## Как это работает:

1. Загружается исходный файл CSS (например, `start-style.css`).
2. Загружается файл для сравнения (например, `end-style.css`).
3. Из второго файла удаляются все селекторы, которые уже присутствуют в первом файле.
4. Минимизируется итоговый CSS-код.
5. Сохранение минимизированного кода в новый файл (например, `final-style.css`).

## Преимущества:

- Убираются дублирующиеся стили, что помогает избежать лишнего кода и уменьшить размер итогового CSS.
- Минимизация итогового CSS снижает время загрузки страницы.

## Требования:

Установленные библиотеки:

- `tinycss2`: Для парсинга CSS.
- `csscompressor`: Для минимизации CSS.

```bash
pip install tinycss2 csscompressor
