hiragana_literals = [
    'あ', 'い', 'う', 'え', 'お',
    'か', 'が', 'き', 'ぎ', 'く',
    'ぐ', 'け', 'げ', 'こ', 'ご',
    'さ', 'ざ', 'し', 'じ', 'す',
    'ず', 'せ', 'ぜ', 'そ', 'ぞ',
    'た', 'だ', 'ち', 'ぢ', 'つ',
    'づ', 'て', 'で', 'と', 'ど',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ば', 'ぱ', 'ひ', 'び',
    'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ',
    'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ', 'ら', 'り',
    'る', 'れ', 'ろ', 'わ', 'を',
    'ん']

romanji = [
    "A", "I", "U", "E", "O",
    "Ka", "Ga", "Ki", "Gi", "Ku",
    "Gu", "Ke", "Ge", "Ko", "Go",
    "Sa", "Za", "Shi", "Ji", "Su",
    "Zu", "Se", "Ze", "So", "Zo",
    "Ta", "Da", "Chi", "Di", "Tsu",
    "Du", "Te", "De", "To", "Do",
    "Na", "Ni", "Nu", "Ne", "No",
    "Ha", "Ba", "Pa", "Hi", "Bi",
    "Pi", "Fu", "Bu", "Pu", "He",
    "Be", "Pe", "Ho", "Bo", "Po",
    "Ma", "Mi", "Mu", "Me", "Mo",
    "Ya", "Yu", "Yo", "Ra", "Ri",
    "Ru", "Re", "Ro", "Wa", "Wo",
    "N"]

romanji_to_class = dict(zip(romanji, range(len(romanji))))
romanji_to_class.setdefault("NA", -1)
