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

    
    def _reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    # Check if palindrome
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True  # 0 or 1 node → palindrome

        # Step 1: Find middle using slow & fast pointers
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second_half = self._reverse(slow)

        # Step 3: Compare first and second halves
        first_half = self.head
        temp_second = second_half
        palindrome = True
        while temp_second:
            if first_half.data != temp_second.data:
                palindrome = False
                break
            first_half = first_half.next
            temp_second = temp_second.next

        
        self._reverse(second_half)

        return palindrome


# Example 
if __name__ == "__main__":
    sll = SinglyLinkedList()
    for val in [10, 20, 30, 20, 10]:
        sll.add_at_tail(val)

    sll.display()  
    print("Is Palindrome?", sll.is_palindrome())  

    sll2 = SinglyLinkedList()
    for val in [10, 20, 30, 20,10]:
        sll2.add_at_tail(val)

    sll2.display() 
    print("Is Palindrome?", sll2.is_palindrome())  
