import tinycss2
import csscompressor


def load_css(filename):
    """Загружаем CSS-файл и парсим его в список правил."""
    with open(filename, 'r', encoding='utf-8') as file:
        return tinycss2.parse_stylesheet(file.read(), skip_whitespace=True)


def extract_selectors(css_rules):
    """Извлекаем селекторы из CSS-правил."""
    selectors = set()
    for rule in css_rules:
        if rule.type == 'qualified-rule':
            selector_text = tinycss2.serialize(rule.prelude).strip()
            selectors.add(selector_text)
    return selectors


def remove_duplicates(base_file, compare_file, output_file):
    """Удаляем дубликаты селекторов из второго файла, оставляя только уникальные и минимизируем итоговый CSS."""
    base_css = load_css(base_file)
    compare_css = load_css(compare_file)

    base_selectors = extract_selectors(base_css)
    unique_rules = [rule for rule in compare_css if
                    rule.type != 'qualified-rule' or tinycss2.serialize(rule.prelude).strip() not in base_selectors]

    merged_css = tinycss2.serialize(unique_rules)
    minified_css = csscompressor.compress(merged_css)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(minified_css)
    print(f'Минимизированный CSS сохранен в {output_file}')


# Использование
remove_duplicates('start-style.css', 'end-style.css', 'final-style.css')