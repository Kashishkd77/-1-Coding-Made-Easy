# Delete middle node using runner technique

# Done using Doubly Linked List

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

    # ("2- DELETING MID NODE USING RUNNER TECHNIQUE")
    def delete_mid(self):
        if (self.head == None):
            print("List is empty, Nothing to delete !")
        else:
            temp = self.head
            count = 0
            while temp != None:
                count = count + 1
                temp = temp.right
            if count ==1 :
                self.head=None
            elif count==2:
                self.head.right=None
            else:
                temp = self.head
                temp1 = self.head
                if count%2 == 0:
                    n = int(count / 2) - 1
                    for i in range(n):
                        temp=temp.right.right
                        temp1=temp1.right
                    temp1.left.right = temp1.right
                    temp1.right.left = temp1.left

                else:
                    temp = self.head
                    temp1 = self.head
                    n = int(count / 2)
                    for i in range(n):
                        temp = temp.right.right
                        temp1 = temp1.right
                    temp1.left.right = temp1.right
                    temp1.right.left = temp1.left

    # ("3- TRAVERSAL IN LIST")
    def traversal(self):
        if (self.head == None):
            print("Empty")
        else:
            temp = self.head
            while (temp!=None):
                print(temp.data, end=' ')
                temp = temp.right
        print()


    # This function helps in execution of the other functions (that perform various Linkedlist operations)
    def perform(self):
        print("1- INSERT ELEMENT AT BEGINNING")
        print("2- DELETE MID NODE USING RUNNER TECHNIQUE")
        print("3- TRAVERSAL IN LIST")
        print("4- EXIT")
        flag=1
        while(flag):
            print()
            ch = int(input("Enter the choice of operation : "))
            if ch == 1:
                val=int(input("Enter the element to insert : "))
                self.insert_begin(val)
                flag = 1
            elif ch == 2:
                self.delete_mid()
                flag = 1
            elif ch == 3:
                print("The Linked List is : ",end="")
                self.traversal()
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