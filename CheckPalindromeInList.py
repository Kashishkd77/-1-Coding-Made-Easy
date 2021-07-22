# Palindrome: Implement a function to check if a linked list is a palindrome.

# WE have used doubly linked list.

class LinkedList:
    head = None

    class Node:
        data = None
        left = None
        right = None

    # ("1- INSERT ELEMENT AT BEGINNING")
    def insert_begin(self,value):
        node = self.Node()
        node.data = value
        node.left = None
        node.right = None
        if (self.head == None):
            self.head = node
        else:
            node.right = self.head
            self.head.left = node
            self.head=node

    # ("2- CHECK LIST IS PALINDROME OR NOT")
    def palindrome(self):
            if (self.head == None):
                print("List is empty")
            else:
                temp1 = self.head
                while temp1.right!=None:
                    temp1=temp1.right

                # Counting number of nodes
                count = 0
                temp = self.head
                while temp != None:
                    count = count + 1
                    temp = temp.right
                n = int(count/2)

                # implementing Palindrome logic
                temp = self.head
                flag=0
                for i in range(n):
                    if temp.data==temp1.data:
                        temp=temp.right
                        temp1=temp1.left
                    else:
                        flag=1
                if flag==0:
                    print("Yes, List is Palindrome")
                else:
                    print("No, List is not Palindrome")


    # ("3- TRAVERSAL IN LIST")
    def traversal(self):
        if (self.head == None):
            print("List is empty")
        else:
            temp = self.head
            while (temp!=None):
                print(temp.data, end=' ')
                temp = temp.right


    # This function helps in execution of the other functions (that perform various Linkedlist operations)
    def perform(self):
        print("1- INSERT ELEMENT AT BEGINNING")
        print("2- CHECK PALINDROME IN LIST")
        print("3- TRAVERSAL IN LIST")
        print("4- EXIT")
        flag=1
        while(flag):
            ch = int(input("Enter the choice of operation : "))
            if ch == 1:
                val=int(input("Enter the element to insert : "))
                self.insert_begin(val)
                flag = 1
            elif ch == 2:
                print("Checking if the given list is Palindrome or not : ",end="")
                self.palindrome()
                flag = 1
            elif ch == 3:
                print("The Linked List is : ",end="")
                self.traversal()
                print()
                flag = 1
            elif ch == 4:
                print("Quiting as per your wish !")
                exit()
            else:
                print("Wrong choice of operation")
                flag=1

# Creating class object
obj = LinkedList()
obj.perform()