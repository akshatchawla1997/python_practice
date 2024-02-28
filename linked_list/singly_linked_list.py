class Node:
    def __init__(self, data=None, next = None) -> None:
        self.data = data
        self.next = next

class SingleLinkList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)



    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print('\n')

if __name__ == '__main__':
    l1 = SingleLinkList()
    l1.insert_at_beginning(10)
    # l1.display()
    l1.insert_at_beginning(20)
    l1.insert_at_beginning(40)
    l1.insert_at_end(50)
    l1.insert_at_end(60)
    l1.display()