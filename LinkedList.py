class Elem:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

def init_list(arg):
    list_length = len(arg)
    print(f"Inbound value: {arg}")
    print(f"Argument length: {list_length}")

    root_node = Elem(arg[0], None)  # 1st Root element of linked list
    print(f'root node created with number: {root_node.data}')
    previous = root_node

    i = 1  # continue creation from 'index' = 2 because the root node with number 1 is already created
    while i < list_length:
        current = Elem(arg[i], None)
        print(f'New node created with Serial number: {arg[i]}')
        previous.next = current
        previous = current
        i += 1

    print("Linked list initialization done.")
    return root_node

def print_list(node, reverse=False):
    if not reverse:
        while node is not None:
            print(node.data)
            node = node.next
    else:
        if node is not None:
            print_list(node.next, reverse=True)
            print(node.data)

def main():
    root = init_list(range(1, 5))
    print("Original Linked List:")
    print_list(root)
    print("---")
    print("Reversed Linked List:")
    print_list(root, reverse=True)

if __name__ == '__main__':
    main()
