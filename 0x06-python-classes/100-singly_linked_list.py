#!/usr/bin/python3
"""singly linked list"""


class Node:
    """node"""

    def __init__(self, data, next_node=None):
        """Node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter data"""
        return self.__data

    @data.setter
    def size(self, value):
        """Setter data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter next_node"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """singly linked list"""

    def __init__(self):
        """initialize head"""
        self.__head = None

    def sorted_insert(self, value):
        """insert new node in sorted linked list"""
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and value >= current.next_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """print linked list"""
        tmp = self.__head
        string = ""
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += '\n'
        return string
