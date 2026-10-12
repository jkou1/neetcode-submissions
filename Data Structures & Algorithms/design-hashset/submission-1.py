# define our list_node class, with key and next values
class list_node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [list_node(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        # find the linked list at the index modulo 10k, matching that 
        # on our key value
        # then iterate through that linked list till we find:
        # either we can add to a list node with next = none,
        # OR we might find that this item is already in the linked list, 
        # and we cannot add it to the hashset! 
        key_list = self.set[key % 10**4]
        while key_list.next:
            if key_list.next.key == key:
                return
            key_list = key_list.next
            
        key_list.next = list_node(key)
        

    def remove(self, key: int) -> None:
        key_list = self.set[key % 10**4]
        # if we can find the key in the key_list, then assign it's prev.next
        # to be it's next
        while key_list.next:
            if key_list.next.key == key:
                # remove it
                key_list.next = key_list.next.next
                return
            key_list = key_list.next


    def contains(self, key: int) -> bool:
        key_list = self.set[key % 10**4]
        while key_list.next:
            if key_list.next.key == key:
                return True
            key_list = key_list.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)