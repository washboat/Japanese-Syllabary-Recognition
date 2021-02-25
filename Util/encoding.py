from Util import JIS_X_0208


def jis_0201_to_uni(jis_code):
    unicode = jis_code + 0xFEC0
    return unicode


def jis_0201_to_char(jis_code):
    unicode = jis_0201_to_uni(jis_code)
    character = chr(unicode)
    return character


def jis_0208_to_uni(jis_code):
    jis = hex(jis_code)
    jis = jis[:2] + jis[2:].upper()
    unicode = JIS_X_0208.jis_uni_map.get(jis)
    return unicode


def jis_0208_to_kuten(jis_code):
    kuten = jis_code - 0x2020
    ku, ten = divmod(kuten, 0x100)
    return (ku, ten)


def jis_0208_to_char(unicode):
    chr(int(jis_0208_to_uni(unicode), 16))


def kuten_to_jis_0208(ku, ten):
    kuten = ku << 8 | ten
    jis_code = kuten + 0x2020
    return jis_code


def char_to_kuten(character):
    unicode = hex(ord(character))
    unicode = unicode[:2] + unicode[2:].upper()
    uni_to_jis_x_0208 = {value: key for key, value in JIS_X_0208.jis_uni_map.items()}
    jis = uni_to_jis_x_0208.get(unicode)
    return jis_0208_to_kuten(int(jis, 16))


def uni_to_kuten(unicode):
    uni = hex(unicode)
    uni = uni[:2] + uni[2:].upper()
    uni_to_jis_x_0208 = {value: key for key, value in JIS_X_0208.jis_uni_map.items()}
    jis = uni_to_jis_x_0208.get(uni)
    return jis_0208_to_kuten(int(jis, 16))


