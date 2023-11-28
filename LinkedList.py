class Elem:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

    def __str__(self):
        return str(self.data)

def print_list(root: Elem):
    """Распечатывает элементы переданного списка. Последовательно, по одному на строку. """

def init_list(data) -> Elem:
    """Инициализирует новый связный список на основе данных хранящихся в списке data. """

def reverse_list(root: Elem) -> Elem:
    """Разворачивает переданный связный список """