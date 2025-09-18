from googletrans import Translator, LANGUAGES

translator = Translator()


def translate_text(text: str, lang: str) -> str:
    try:
        code = code_lang(lang)
        result = translator.translate(text, dest=code)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"


def lang_detect(txt: str) -> str:
    try:
        result = translator.detect(txt)
        return f"Detected(lang={result.lang}, confidence={result.confidence})"
    except Exception as e:
        return f"Error: {str(e)}"


def code_lang(lang: str) -> str:
    lang = lang.lower()
    # якщо користувач передав код мови
    if lang in LANGUAGES:
        return lang
    # якщо користувач передав назву мови
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    raise ValueError("Language not found")


def main():
    txt = "Доброго дня. Як справи?"
    lang = "english"

    print(txt)
    print(lang_detect(txt))
    print(translate_text(txt, lang))
    print(code_lang("en"))
    print(code_lang("english"))


if __name__ == "__main__":
    main()
