
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # a. Add at head
    def add_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # b. Add at tail
    def add_at_tail(self, data):
        new_node = Node(data)
        if not self.head:   
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # c. Delete at head
    def delete_at_head(self):
        if self.head:
            self.head = self.head.next

    # d. Delete at tail
    def delete_at_tail(self):
        if not self.head:  
            return
        if not self.head.next:  
            self.head = None
            return
        temp = self.head
        while temp.next.next:  
            temp = temp.next
        temp.next = None

    # e. Add after given data
    def add_after(self, target, data):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"{target} not found in list.")

    # f. Delete after given data
    def delete_after(self, target):
        temp = self.head
        while temp and temp.next:
            if temp.data == target:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"No node found after {target}.")

    # g. Search an element
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    # Utility function: Display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example 
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.add_at_head(10)
    sll.add_at_tail(20)
    sll.add_at_tail(30)
    sll.display()   

    sll.add_after(20, 25)
    sll.display()   

    sll.delete_after(20)
    sll.display()   

    sll.delete_at_head()
    sll.display()   

    sll.delete_at_tail()
    sll.display()   

    print(sll.search(20)) 
    print(sll.search(50))  
