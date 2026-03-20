FOOTER_ADDRESS_SCRIPT = """
    var span = arguments[0];
    var br = span.querySelector('br');
    if (br && br.nextSibling) {
        return br.nextSibling.textContent.trim();
    }
    return '';
"""
UNFOCUS_ELEMENT_SCRIPT = """
    var element = document.querySelector(arguments[0]);
    if (!element) {
        return ['Элемент не найден.', false];
    }
    if (element === document.activeElement) {
        element.blur();
        return ['Убран фокус с элемента.', true];
    } else {
        return ['Нет фокуса на элементе.'];
    }
"""
HAS_VERTICAL_SCROLL_SCRIPT = """
        return document.documentElement.scrollHeight >
            document.documentElement.clientHeight;
"""
