class Elem:

    def __init__(self, d, n = None):
        self.data = d
        self.next = n

    def __str__(self):
        return str(self.data)


def init_list(arg):
    list_lenght = len(arg)
    print(f"inbound value: {arg}")
    print(f"arg lenght : {list_lenght}")
    previous = Elem(arg[0], None)  # 1st Root element of linked list
    root_node = previous
    i = 1  # continue creation from 'index' = 2 because root node with number 1 is all ready created
    while i <= list_lenght:
        current = Elem(i, None)
        print(f'new node created with Serial number: {i}"')
        previous.next = current
        previous = current
        i += 1
    print(f"linked list initialization done.")
    return root_node


def print_list(node: Elem):
    while (node is not None):
        print(node.data)
        node = node.next


def main(self):
    root = init_list(range(1, 5))
    print("---")
  #  reversed = reverse_list(root)
  #  print_list(reversed)


def main():
    root = init_list(range(1, 5))
    print_list(root)
    print("---")

if __name__ == '__main__':
    main()
