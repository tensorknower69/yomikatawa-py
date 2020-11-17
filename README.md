# yomikatawa
A python cli for https://yomikatawa.com

This is just an incomplete python copy of https://github.com/tensorknower69/yomikatawa,

I wrote it just for comparsion with the [Haskell version](https://github.com/tensorknower69/yomikatawa), not all features are included or WILL EVER BE IMPLEMENTED.

So, if you want to help with the project, please take a look at https://github.com/tensorknower69/yomikatawa.

## Usage

### Querying the reading of a word:
```bash
$ yomikataw-pya 読み方
Hiragana: よみかた
```

### Querying more information:
```bash
$ yomikatawa-py --romaji --same-reading 再
Hiragana: さい
Romaji: sai
Same reading: ['蔡', '砕', '栽', '細', '斉', '債', '猜', '才', '濟', '犀', '碎', '采', '差異', '佐為', '佐井', '偲', '埣', '寨', '差違', '摧', '樶', '洒', '淬', '灑', '犲', '綵', '縡', '
纔', '賽']
```

### Search for other categories:
```bash
$ yomikatawa-py --category <category> ...
```

Currently, you can search for kanji(漢字), sei(姓) or mei(名).

```bash
$ yomikatawa-py --category sei 藤原
Hiragana: ふじわらの
$ yomikatawa-py --category kanji 藤原
Hiragana: ふじわら
```

## Installation

```bash
$ git clone https://github.com/tensorknower69/yomikatawa
$ cd yomikatawa
$ pip install .
```
