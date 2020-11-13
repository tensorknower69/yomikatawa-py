# yomikatawa
A python cli for https://yomikatawa.com

## Usage

### Querying the reading of a word:
```bash
$ yomikatawa 読み方
Hiragana: よみかた
```

### Querying more information:
```bash
$ yomikatawa --romaji --same-reading 再
Hiragana: さい
Romaji: sai
Same reading: ['蔡', '砕', '栽', '細', '斉', '債', '猜', '才', '濟', '犀', '碎', '采', '差異', '佐為', '佐井', '偲', '埣', '寨', '差違', '摧', '樶', '洒', '淬', '灑', '犲', '綵', '縡', '
纔', '賽']
```

### Search for other categories:
```bash
$ yomikatawa --category <category> ...
```

Currently, you can search for kanji(漢字), sei(姓) or mei(名).

```bash
$ yomikatawa --category sei 藤原
Hiragana: ふじわらの
$ yomikatawa --category kanji 藤原
Hiragana: ふじわら
```

## Installation

```bash
$ git clone https://github.com/tensorknower69/yomikatawa
$ cd yomikatawa
$ pip install .
```
