from collections import defaultdict
from collections import Counter
import re




def stringCount(input):

    input.sort() #Sort the list alphabetically

    print(len(input))
    #CountElements = Counter(input) #Count elements && remove duplicates

    #for k, v in CountElements.items(): #iterates for each key(name) and value(#) to print
    #    print(k, v)           




def isFloat(inValues):
     
    testRe = re.findall(r'^[+-]?[0-9]*\.[0-9]+$', inValues)
    
    if(testRe):
        #print("True")
        return (bool(testRe)) 
        
    else:
        return (bool(testRe))
        #print("False")



class node:
    """The node class a general example learned from tutorialspoint and WC3 schools"""
    def __init__(self, data = None):
        self.data = data
        self.next = None

     
class LinkedList:
    """ Linked List  """
    def __init__(self):
        
        self.head = None

    def insert(self, data):
        new_node = node(data)
        
        new_node.next = self.head
        self.head = new_node
        

    def printLL(self):        
        cur_node = self.head
        values = ''

        while (cur_node.next != None):             
            values += str(cur_node.data) + ' '
            
            cur_node = cur_node.next            
            
        if (not cur_node.next != None):
            
            values += str(cur_node.data)
        print(values)
        
    def delete(self, location):
        cur_del = self.head

        if(cur_del != None):
            if(cur_del.data == location):
                self.head = cur_del.next
                cur_del = None
                return

        while(cur_del != None):
            if(cur_del.data == location):
                break
            temp = cur_del
            cur_del = cur_del.next

        
        temp.next = cur_del.next

        cur_del = None

    def search(self, number):
        cur_search = self.head

        while(cur_search != None):

            if (cur_search.data == number):
                #print("Value " + str(number) + " found")    # I didnt read the directions!!
                return (bool (True)) 
            cur_search = cur_search.next
        #print("Value " + str(number) + " not found")
    
            
    def size(self):
        cur_size = self.head
        count = 0

        while (cur_size != None):
            count+= 1
            cur_size = cur_size.next
        return count






            





#ll = LinkedList()
#ll.insert(1)
#ll.insert(2)
#ll.printLL()
#ll.delete(2)
#ll.printLL()
#if (ll.search(2)):
#    print("Value 2 found")
#else:
#    print("Value 2 not found")
#if (ll.search(1)):
#    print("Value 1 found")
#else:
#    print("Value 1 not found")
#ll.insert(4)
#ll.printLL()
#print(str(ll.size()))


 

    



aList = defaultdict(list)
aList = ["Manny", "May", "Clark", "Abby", "Zen", "May", "Clark"]
#bList = ["Hello", "Hello", "Bob", "hello", "Bob", "Lucky", 'Bob', 'BOB']

#bList.sort()

#clist = [] # I dont understand how the testing works and string count wont complile without an arugment

stringCount(aList) 


#paraTest = "-1.4546"
#paraTest1 = "--2.5"
#paraTest2 = "ABC"
#paraTest3 = "+45.88"
#paraTest4 = "-.4406 06"
#print(isFloat(paraTest))
#print(isFloat(paraTest1))
#print(isFloat(paraTest2))
#print(isFloat(paraTest3))
#print(isFloat(paraTest4))


