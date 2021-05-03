# ETL-1

### Characters

* Numeric: 10 \(0-9\)
* Capital Roman alphabet: 26 \(A-Z\)
* Special: 12 \(\+-\*/=\(\)・,?’\)
* Katakana: 51 \(ア-ン\)
* Total: 99

### Format

The ETL-1 dataset consists of 141,319 logical records spread out over 13 physical files. Files 1-6 contain Arabic numerals, English letters, and miscellaneous symbols not relevant to this project's scope. Files 7-13 contain data for the Japanese syllabary known as katakana. It should be assumed that any reference to ETL-1 from this point on is made concerning files 7-13 only. 

There are 51 subsets of data, each consisting solely of one character written by multiple authors. With 1411 authors, we should expect 71961 total katakana records. In actuality, there are 71959 records due to missing data.

{% hint style="info" %}
The characters ウ and ネ are each missing one record worth of data
{% endhint %}

The format of each record in the dataset is summarized in the table below. Note that only the relevant metadata is listed in the table. Some metadata, such as the age and occupation of the writer, is not listed here but can be found in the ETL [official documentation](http://etlcdb.db.aist.go.jp/specification-of-etl-1). Each record is 2052 bytes in size.

| Byte Position | Number of Bytes | Type | Content |
| :---: | :---: | :---: | :---: |
| 1-2 | 2 | Integer | Data Number |
| 3-4 | 2 | ASCII | Character Code |
| 5-6 | 2 | Integer | Serial Sheet Number |
| 7 | 1 | Binary | JIS X 0201 Code |
| … | … | … | … |
| 33-2048 | 2016 | Packed | 64x63 Image Data |
| 2049-2052 | 4 | Padding | N/A |

{% hint style="info" %}
The characters ヰ and ヱ are obsolete and are processed, but not used when training the neural networks.
{% endhint %}

{% hint style="info" %}
Three characters イ,  ウ,  and エ each appear as duplicates.
{% endhint %}

