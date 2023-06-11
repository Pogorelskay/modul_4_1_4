def isStrPalidrom(s:str):
    """
    функция в цикле от 0 до половины длины строки
    проверяет равенство символа с начала строки по индексу и по обратному индексу (с учетом +1)
    при первом же не совпадении возврашает результат Ложь, не делая дальше проверок
    если цикл до половины слова прошел - и не было ошибок то вернем истину
    при этом нет смысла проверять после середины так как символы эти мы уже сравнивали
    """
    len_str = len(s)
    middle = len_str // 2
    for i in range(0, middle):
        j = i + 1
        if s[i] != s[-j]:
            return False
    return True

if __name__ == '__main__':
    print(isStrPalidrom("лепсспел"))
    print(isStrPalidrom("helloworld"))



