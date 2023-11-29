import sys


class Elem:
    def __init__(self, d, n=None):
        self.data = d  # data container in current node
        self.next = n  # next node in linked list


list_length = 750
prev = Elem("Iam the 1st node Iam Head", None)


def addnode(i):
    print(f"root element: {prev.data}; created")
    if i < list_length:
        current = Elem(f"new instance number {i} created", None)
        prev.next = current
        print(f"item: {current.data} |  created: ")
        i = i + 1
        addnode(i)
    else:
        sys.exit(0)


def main():
    print(f"Attempt ro generate linked list with {list_length} items")
    addnode(1)


main()
