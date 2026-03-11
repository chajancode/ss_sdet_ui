FOOTER_ADDRESS_SCRIPT = """
    var span = arguments[0];
    var br = span.querySelector('br');
    if (br && br.nextSibling) {
        return br.nextSibling.textContent.trim();
    }
    return '';
"""
