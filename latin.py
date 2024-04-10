'''Создайте файл latin.py напишите класс-декоратор ToLatin,
который работает с функциями, принимающими строковое значение.
Данный декоратор должен проверять если декорируемая функция возвращает строку на кириллице,
то декоратор преобразовывает ее в латиницу,
используя следующий словарь для замены русских букв на соответствующее латинское написание:

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

Также данный декоратор должен сам принимать аргумент is_login. Если is_login=True,
то декорированная функция должна возвращать значение пригодное для использования в качестве логина,
то есть без пробелов, вместо пробелов использовать «_». Если is_login=False,
то декорированная функция должна возвращать преобразованную строку.
Замены делать без учета регистра (исходную строку перевести в нижний регистр – малые буквы).'''


class ToLatin:
    def __init__(self, is_login=False):
        self.is_login = is_login
        self.translation_dict = {
            'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '',
            'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
        }

    def __call__(self, func):
        def wrapper(string):
            translated_string = self.translate_to_latin(string)
            if self.is_login:
                return self.make_login_compatible(translated_string)
            else:
                return translated_string

        return wrapper

    def translate_to_latin(self, string):
        translated_chars = [self.translation_dict.get(char, char) for char in string.lower()]
        return ''.join(translated_chars)

    def make_login_compatible(self, string):
        return string.replace(' ', '_')


to_latin = ToLatin(is_login=False)

@to_latin
def print_login(text):
    return text

login1 = print_login("Иман Турдукеев")
print(login1)  

to_latin_login = ToLatin(is_login=True)

@to_latin_login
def print_login_with_space_buttom(text):
    return text

login2 = print_login_with_space_buttom("Иман Турдукеев")
print(login2) 
