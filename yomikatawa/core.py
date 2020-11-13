import enum
import lxml.etree
import requests
import typing
import urllib.parse
import functools

__all__ = [
        "Result",
        "Category",
        "search",
        ]

class Result(typing.NamedTuple):
    input_word: str
    hiragana: str
    romaji: str
    same_reading_words: list[str]
    random_words: list[str]

    def __str__(self):
        # use repr for quoting
        return f"{repr(self.input_word)} {repr(self.hiragana)} {repr(self.romaji)} {self.same_reading_words} {self.random_words}"

def parse_links_section(section):
    return section.xpath('./p/wbr/a/text()')

def at_may(index, list_like):
    return None if len(list_like) <= index else list_like[index]

head_may = functools.partial(at_may, 0)

class NotFoundError(Exception):
    pass

class NotKanjiError(Exception):
    pass

class UnknownCategoryName(Exception):
    def __init__(self, string, mapping):
        self.string = string
        self.mapping = mapping
        super().__init__(f"{string}, mapping: {mapping}")

def parse_root(root):
    section = root.xpath('/html/body/section[@id="content"]')[0]
    input_word = section.xpath("./*[self::h1 or self::h2]/strong/text()")[0]
    hiragana = section.xpath("./p[1]/text()")[0]
    if hiragana == "検索結果: 見つかりませんでした。":
        raise NotFoundError(input_word)
    elif hiragana.startswith("漢字を含めてください。"):
        raise NotKanjiError(input_word)

    romaji = head_may(section.xpath("./p[2]/text()"))

    same_reading_words_section = head_may(section.xpath('./section[@id="sameReadingWords"]'))
    same_reading_words = [] if same_reading_words_section == None else parse_links_section(same_reading_words_section)

    random_words = parse_links_section(section.xpath('./section[@id="randomWords"]')[0])

    return Result(
            input_word=input_word,
            hiragana=hiragana,
            romaji=romaji,
            same_reading_words=same_reading_words,
            random_words=random_words
            )

class Category(enum.Enum):
    KANJI = "kanji"
    SEI = "sei"
    MEI = "mei"

def as_category(category_like):
    if isinstance(category_like, str):
        mapping = {
                "first_name": Category.MEI,
                "firstname": Category.MEI,
                "last_name": Category.SEI,
                "lastname": Category.SEI,
                **{c.value: c for c in list(Category)}
                }
        if category_like in mapping:
            return mapping[category_like]
        else:
            raise UnknownCategoryName(category_like, mapping)
    elif isinstance(category_like, Category):
        return category_like
    else:
        raise NotImplementedError(f"Unknown category-like type: {type(category_like)} {category_like}")

def search(word, category=Category.KANJI):
    category = as_category(category)
    url = f"https://yomikatawa.com/{category.value}/{urllib.parse.quote(word)}" # idk why ?search=<number> is used when searching
    r = requests.get(url)
    return parse_root(lxml.etree.HTML(r.content))
