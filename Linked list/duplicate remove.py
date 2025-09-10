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

    # Case 1: Remove duplicates from sorted list
    def remove_duplicates_sorted(self):
        temp = self.head
        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next

    # Case 2: Remove duplicates from unsorted list
    def remove_duplicates_unsorted(self):
        if not self.head:
            return

        seen = set()
        temp = self.head
        seen.add(temp.data)

        while temp.next:
            if temp.next.data in seen:
                temp.next = temp.next.next
            else:
                seen.add(temp.next.data)
                temp = temp.next


# Example 
if __name__ == "__main__":
    # Example 1: Sorted list
    sll1 = SinglyLinkedList()
    for val in [10, 20, 20, 30, 30, 30, 40]:
        sll1.add_at_tail(val)

    print("Original Sorted List:")
    sll1.display()
    sll1.remove_duplicates_sorted()
    print("After Removing Duplicates (Sorted):")
    sll1.display()

    # Example 2: Unsorted list
    sll2 = SinglyLinkedList()
    for val in [10, 30, 20, 10, 40, 30, 50]:
        sll2.add_at_tail(val)

    print("\nOriginal Unsorted List:")
    sll2.display()
    sll2.remove_duplicates_unsorted()
    print("After Removing Duplicates (Unsorted):")
    sll2.display()
