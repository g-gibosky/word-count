import re


class mainService:
    def count_words(self, form_info: dict) -> int:
        result = 0
        if form_info["form_text"] != "" and form_info["form_text"]:
            if form_info["option"] == 0:
                result = self.count_words_regex(form_info["form_text"])
            else:
                result = self.count_words_split(form_info["form_text"])
        return result

    def count_words_regex(self, form_words: str) -> int:
        words = len(re.findall("\w+", form_words))
        return words

    def count_words_split(self, form_words: str) -> int:
        return len(form_words.split(" "))
