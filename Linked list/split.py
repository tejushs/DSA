# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Function to split into two lists (alternate nodes)
    def split(self):
        list1 = SinglyLinkedList()
        list2 = SinglyLinkedList()

        temp = self.head
        pos = 1  

        while temp:
            if pos % 2 == 1:  
                list1.add_at_tail(temp.data)
            else:             
                list2.add_at_tail(temp.data)
            temp = temp.next
            pos += 1

        return list1, list2


# Example 
if __name__ == "__main__":
    sll = SinglyLinkedList()
    for val in [10, 20, 30, 40, 50]:
        sll.add_at_tail(val)

    print("Original List:")
    sll.display()

    l1, l2 = sll.split()
    print("List 1 (odd positions):")
    l1.display()
    print("List 2 (even positions):")
    l2.display()
