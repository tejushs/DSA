# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
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

    # Function to create intersection list
    @staticmethod
    def intersection(list1, list2):
        result = SinglyLinkedList()
        elements = set()  

        # store all data from list1 into a set
        temp1 = list1.head
        while temp1:
            elements.add(temp1.data)
            temp1 = temp1.next

        # check for common elements in list2
        temp2 = list2.head
        while temp2:
            if temp2.data in elements:
                result.add_at_tail(temp2.data)
            temp2 = temp2.next

        return result


# Example 
if __name__ == "__main__":
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()

    
    list1.add_at_tail(10)
    list1.add_at_tail(20)
    list1.add_at_tail(30)
    list1.add_at_tail(40)

    
    list2.add_at_tail(15)
    list2.add_at_tail(20)
    list2.add_at_tail(25)
    list2.add_at_tail(30)
    list2.add_at_tail(50)

    print("List 1:")
    list1.display()

    print("List 2:")
    list2.display()

    # Find intersection
    result = SinglyLinkedList.intersection(list1, list2)
    print("Intersection List:")
    result.display()
