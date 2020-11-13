import argparse
import yomikatawa as yomi

def create_parser():
    parser = argparse.ArgumentParser(description="A command line interface for https://yomikatawa.com.")
    parser.add_argument("-c", "--category", type=str, default="kanji", help="print possible choices on error")
    parser.add_argument("-r", "--romaji", action="store_true", dest="print_romaji", help="output romaji")
    parser.add_argument("-s", "--same-reading", action="store_true", dest="print_same_reading_words", help="output words with same reading")
    parser.add_argument("input_word", type=str)
    return parser

def main():
    args = create_parser().parse_args()
    result = yomi.search(args.input_word, category=args.category)
    print("Hiragana: " + result.hiragana)
    if args.print_romaji:
        print("Romaji: " + result.romaji)
    if args.print_same_reading_words:
        print("Same reading: " + str(result.same_reading_words))

if __name__ == "__main__":
    main()
