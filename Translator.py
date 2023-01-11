import requests
import sys
from bs4 import BeautifulSoup

def user_input():
    global LANGUAGES
    LANGUAGES = {1: "Arabic", 2: "German", 3: "English", 4: "Spanish", 5: "French", 6: "Hebrew", 7: "Japanese",
                 8: "Dutch", 9: "Polish", 10: "Portuguese", 11: "Romanian", 12: "Russian", 13: "Turkish"}
    print("Hello, welcome to the translator. Translator supports:\n")
    for i, language in LANGUAGES.items():
        print(f'{i}. {language}')
    first_language = int(input("\nType the number of your language: "))
    second_language = int(input("Type the number of language you want to translate to: "))
    word = input("Type the word you want to translate: ")
    return first_language, second_language, word

def create_url(first_language, second_language, word):
    from_lang = str.lower(LANGUAGES[first_language])
    to_lang = str.lower(LANGUAGES[second_language])
    url = f'https://context.reverso.net/translation/{from_lang}-{to_lang}/{word}'
    return url

def get_content(to_lang, from_lang, user_word):
    global headers
    url = create_url(to_lang, from_lang, user_word)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}
    response = requests.get(url, headers=headers)
    return response

def parse_page(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    translations = soup.find_all('a', class_=lambda value: value and value.startswith("translation"))
    translation_list = [word.get_text().strip() for word in translations]
    examples = soup.select('#examples-content span.text')
    example_list = [phrase.get_text().strip() for phrase in examples]
    return translation_list[3:8], example_list[:10]

def print_results(translation_list, example_list, second_language):
    print_lang = LANGUAGES[second_language]
    print(f'\n{print_lang} Translations:')
    for word in translation_list:
        print(word)
    print(f'\n{print_lang} Examples:')
    pairs = []
    for phrase in example_list:
        if example_list.index(phrase) < len(example_list) - 1 and example_list.index(phrase) % 2 == 0:
            pairs.append((example_list[example_list.index(phrase)], example_list[example_list.index(phrase) + 1]))
    for pair in pairs:
        print(f'{pair[0]}:\n{pair[1]}\n')


def main():
    language_in, language_out, word = user_input()
    page = get_content(language_in, language_out, word)
    translations, examples = parse_page(page)
    print_results(translations, examples, language_out)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(e)
