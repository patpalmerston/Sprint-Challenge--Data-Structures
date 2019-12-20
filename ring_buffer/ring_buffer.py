from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if capacity is true
        if self.capacity:
            # check to see if the length of storage is less than capacity and once it is full hit the elif
            if self.storage.length < self.capacity:
                # load up the que through the tail
                self.storage.add_to_tail(item)
                # keep track of the tail item making it the current item
                self.current = self.storage.tail
            # now that storage has hit capacity we need to remove from the head to allow new items in
            elif self.current is self.storage.tail:
                # we are full lets remove oldest
                self.storage.remove_from_head()
                # next item moves to the head
                self.storage.add_to_head(item)
                # new current becomes head
                self.current = self.storage.head
            else:
                # current does not have access to the doubly linked list so must use singly linked list
                # insert the item as a node after the current value 
                self.current.insert_after(item)
                # increment the length of storage with the new node
                self.storage.length += 1
                # move current through the list, new item becomes the current value
                self.current = self.current.next
                # as item moves to the end of storage delete
                self.storage.delete(self.current.next)
            # print('current2', self.current.value)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr_item = self.storage.head
        # while curr item is true
        while curr_item:
            # add value of item to the list
            list_buffer_contents.append(curr_item.value)
            curr_item = curr_item.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
