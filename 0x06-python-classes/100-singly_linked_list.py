#!/usr/bin/python3
"""Defines a node class """


class Node:
    """Defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """Initialises __data variable. """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns __data val """

        return self.__data

    @data.setter
    def data(self, value):
        """Sets __data with value"""

        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Returns __next_node val """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
         """Sets __next_node with value """

         if value is None or isinstance(value, Node):
             self.__next_node = value
         else:
             raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    def __init__(self):
        """Initialises the list """

        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node into the sorted list """

        if self.__head is None or self.__head.data > value:
            self.__head = Node(value, self.__head)
            return

        current = self.__head
        save_ptr = None

        while current.next_node and current.data < value:
            current = current.next_node

        current.next_node = Node(value, current.next_node)

    def __str__(self):
        """Returns a str format to print """
        rep = ""
        current = self.__head

        while current:
            if current is self.__head:
                rep += str(current.data)
            else:
                rep += "\n" + str(current.data)
            current = current.next_node
        return rep
