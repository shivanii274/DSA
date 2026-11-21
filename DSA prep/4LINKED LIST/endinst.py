
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)

        if head is None:
            return new_node

        temp = head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

        return head


arr = list(map(int, input("Enter linked list elements: ").split()))
x = int(input("Enter value to insert: "))

head = None
temp = None

for value in arr:
    new_node = Node(value)

    if head is None:
        head = new_node
        temp = new_node
    else:
        temp.next = new_node
        temp = new_node

obj = Solution()
head = obj.insertAtEnd(head, x)

temp = head
while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
