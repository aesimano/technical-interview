

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        for i in range(1, position):
            if current:
                current = current.next
            else:
                return None
        print 'debug: values are {}'.format(self.get_values())
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if not isinstance(position, int):
            raise Exception('Invalid index {}: must be greater than 0.'.format(position))

        if not isinstance(new_element, Element):
            raise Exception('Invalid new_element type {}'.format(type(new_element)))

        current = self.head
        previous = None
        for i in range(1, position):
            if current:
                previous = current
                current = current.next
            else:
                raise Exception('Invalid index {}. Trying to insert past end of linked list'.format(position))

        if previous:
            new_element.next = previous.next
            previous.next = new_element
        else:
            new_element.next = self.head
            self.head = new_element

        print 'debug: values are {}'.format(self.get_values())

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current:
            if current.value == value:
                # remove it
                if previous:
                    previous.next = current.next
                else:
                    if self.head:
                        self.head = current.next
                break
            else:
                previous = current
                current = current.next

        print 'debug: values are {}'.format(self.get_values())

    def get_values(self):
        current = self.head
        values = []
        while current:
            values.append(current.value)
            current = current.next
        return values

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        first_item = self.head
        if self.head:
            self.head = self.head.next

        return first_item

if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print ll.head.next.next.value
    # Should also print 3
    print ll.get_position(3).value

    # Test insert
    ll.insert(e4, 1)
    # Should print 4 now
    print ll.get_position(1).value

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print ll.get_position(1).value
    # Should print 4 now
    print ll.get_position(2).value
    # Should print 3 now
    print ll.get_position(3).value