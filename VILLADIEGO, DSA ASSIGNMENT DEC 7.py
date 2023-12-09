class node:
    def __init__ (self, value = 0, next = None):
        if -100<= value <= 100:
            self.value = value
            self.next = next
            
def merge(list1, list2):
    dummy = node()
    current = dummy
    
    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
            
        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next
        
    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2
        
    return dummy.next


list1 = node(1, node(2, node(4)))
list2 = node(1, node(3, node(4)))

output = merge(list1, list2)

while output:
    print(output.value, end='')
    if output.next:
        print(" -> ", end='')
    output = output.next

            
            
            
            
            
            
            
                