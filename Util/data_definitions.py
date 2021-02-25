import types
# ETL1 dataset layout
# File name | Kinds      |The number | Sheet      |The number|The number
#           | of         |of         | numbers    | of sheets|of records
#           | categories |categories | contained  |
#
# etl1c-01  | ０１２３４５６７ |   8 | 1001--2960 |     1445 |     11560
# etl1c-02  | ８９ＡＢＣＤＥＦ |   8 | 1001--2960 |     1445 |     11560
# etl1c-03  | ＧＨＩＪＫＬＭＮ |   8 | 1001--2960 |     1445 |     11560
# etl1c-04  | ＯＰＱＲＳＴＵＶ |   8 | 1001--2960 |     1445 |     11560
# etl1c-05  | ＷＸＹＺ￥＋－＊ |   8 | 1001--2960 |     1445 |     11560
# etl1c-06  | ／＝（）・，　’ |   8 | 1001--2960 |     1445 |     11560
# etl1c-07  | アイウエオカキク |   8 | 1001--2960 |     1411 |     11288
# etl1c-08  | ケコサシスセソタ |   8 | 1001--2960 |     1411 |     11288
# etl1c-09  | チツテトナニヌネ |   8 | 1001--2960 |     1411 |     11287
# etl1c-10  | ノハヒフヘホマミ |   8 | 1001--2960 |     1411 |     11288
# etl1c-11  | ムメモヤイユエヨ |   8 | 1001--2960 |     1411 |     11288
# etl1c-12  | ラリルレロワヰウ |   8 | 1001--2960 |     1411 |     11287
# etl1c-13  | ヱヲン           |   3 | 1001--2960 |     1411 |      4233
#           |         missing a record in sheet-number=2672 of category=NA(ナ)
#           |         missing a record in sheet-number=2708 of category=RI(リ)
katakana_definition = types.SimpleNamespace()
katakana_definition.name = "katakana"
katakana_definition.resolution = (64, 63)
katakana_definition.buffer = 2052
katakana_definition.format = ">H2sH6BI4H4B4x2016s4x"
katakana_definition.jis_code_index = 3
katakana_definition.image_data_index = 18
katakana_definition.depth = 4
katakana_definition.char_set = "JIS_X_0201"
katakana_definition.class_count = 49
katakana_definition.dataset_count = 1411

# ETL8G dataset layout
#  --------------------------------------------------------------------------------------------
# |  File    |  Number | No. of |  Number  |           | Number |                              |
# |    Name  |    of   | Categ- |    of    |  Data Set |   of   |                              |
# |          | Records |  ories | Data Sets|   Number  | Sheets |                              |
# |============================================================================================|
# | ETL8G-01 |   4780  |   956  |     5    |   1 -   5 |   50   |                              |
# | ETL8G-02 |   4780  |   956  |     5    |   6 -  10 |   50   |                              |
# |    :     |     :   |    :   |     :    |     :     |    :   |                              |
# | ETL8G-32 |   4780  |   956  |     5    | 156 - 160 |   50   |                              |
# | ETL8G-33 |    956  |   956  |     1    | uncertain |   10   |                              |
#  --------------------------------------------------------------------------------------------
hiragana_definition = types.SimpleNamespace()
hiragana_definition.name = "hiragana"
hiragana_definition.resolution = (128, 127)
hiragana_definition.buffer = 8199
hiragana_definition.format = ">2H8sI4B4H2B30x8128s11x"
hiragana_definition.jis_code_index = 1
hiragana_definition.image_data_index = 14
hiragana_definition.depth = 4
hiragana_definition.char_set = "JIS_X_0208"
hiragana_definition.class_count = 71
hiragana_definition.total_classes = 956
hiragana_definition.dataset_count = 160
hiragana_definition.sheets_per_dataset = 50
hiragana_definition.dataset_per_physical_file = 5

# ETL9G dataset layout
#  --------------------------------------------------------------------------------------------
# |  File    |  Number | No. of |  Number  |           | Number |                              |
# |    Name  |    of   | Categ- |    of    |  Data Set |   of   |                              |
# |          | Records |  ories | Data Sets|   Number  | Sheets |                              |
# |============================================================================================|
# | ETL9G-01 |  12144  |  3036  |     4    |   1 -   4 |   80   |                              |
# | ETL9G-02 |  12144  |  3036  |     4    |   5 -   8 |   80   |                              |
# |    :     |    :    |    :   |     :    |     :     |    :   |                              |
# | ETL9G-50 |  12144  |  3036  |     4    | 197 - 200 |   80   |                              |
#  --------------------------------------------------------------------------------------------
kanji_definition = types.SimpleNamespace()
kanji_definition.name = "kanji"
kanji_definition.resolution = (128, 127)
kanji_definition.buffer = 8199
kanji_definition.format = ">2H8sI4B4H2B34x8128s7x"
kanji_definition.jis_code_index = 1
kanji_definition.image_data_index = 14
kanji_definition.depth = 4
kanji_definition.char_set = "JIS_X_0208"
kanji_definition.class_count = 2965
kanji_definition.dataset_count = 80
kanji_definition.sheets_per_dataset = 20
kanji_definition.dataset_per_physical_file = 4

k9B_definition = types.SimpleNamespace()
k9B_definition.name = "kanji"
k9B_definition.resolution = (64, 63)
k9B_definition.buffer = 576
k9B_definition.format = ">2H4s504s64x"
k9B_definition.jis_code_index = 1
k9B_definition.image_data_index = 3
k9B_definition.depth = 1
k9B_definition.char_set = "JIS_X_0208"
k9B_definition.class_count = 2965
k9B_definition.dataset_count = 200
k9B_definition.sheets_per_dataset = 800
k9B_definition.dataset_per_physical_file = 40

kanji_set = {"A"}
hiragana_false_positives = {'AI', 'HEI', 'MAI', 'SEN', 'KON', 'KAI', 'KEI'}


