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

    # Function to find sum of last n nodes in one traversal
    def sum_of_last_n_nodes(self, n):
        if not self.head:
            return 0

        first = self.head
        second = self.head

        # Step 1: Move first pointer n steps ahead
        for _ in range(n):
            if first is None:
                return 0  
            first = first.next

        # Step 2: Move both until first reaches end
        while first:
            first = first.next
            second = second.next

        # Step 3: Sum from second to end
        total = 0
        while second:
            total += second.data
            second = second.next

        return total


# Example 
if __name__ == "__main__":
    sll = SinglyLinkedList()
    for val in [10, 20, 30, 40, 50]:
        sll.add_at_tail(val)

    sll.display()  

    print("Sum of last 3 nodes:", sll.sum_of_last_n_nodes(3))  
    print("Sum of last 2 nodes:", sll.sum_of_last_n_nodes(2))  
