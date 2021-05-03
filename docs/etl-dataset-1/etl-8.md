# ETL-8

### Characters

* Kanji: 881
* Hiragana: 75
* Total: 956

### Format

The ETL-8 dataset consists of 152,960 logical records distributed over 33 physical files. Each file has some hiragana data, so we must process them all. There are 160 subsets of data consisting of 881 kanji and 75 hiragana characters each. Each subset was penned by a different author. There are 12,000 total hiragana records present. However, 640 of these records are smaller versions of hiragana known as sutegana \(捨て仮名\). 

In Japanese writing, sutegana is combined with normal-sized characters to create [diphthongs](https://www.google.com/search?q=diphthongs&oq=diphthongs&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8), among other things. Since our focus is to recognize characters in isolation, as opposed to a string of characters, there is no benefit to including Sutegana characters when creating our model. Therefore, the documentation will reference only the 71 hiragana listed in the Japanese syllabary. Sutegana aside, there are only 11,360 hiragana records left to build the model.

The format of each record in the dataset is summarized in the table below. Note that only the relevant metadata is listed in the table. Some metadata, such as the age and occupation of the writer, is not listed here but can be found in the ETL [official documentation](http://etlcdb.db.aist.go.jp/specification-of-etl-8). Each record is 8199 bytes in size.



| Byte Position | Number of Bytes | Type | Contents |
| :---: | :---: | :---: | :---: |
| 1-2 | 2 | Integer | Serial Sheet Number |
| 3-4 | 1 | Binary | JIS X 0208 Code |
| 5-12 | 8 | ASCII | Typical Reading |
| 13-16 | 4 | Integer | Serial Data Number |
| ... | ... | ... | ... |
| 61-8188 | 8128 | Packed | Image Data |
| 8189-8199 | 11 | Padding | N/A |



