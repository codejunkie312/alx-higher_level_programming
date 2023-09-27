#!/usr/bin/python3
"""
This module contains a class that defines a singly linked list and a node
"""


class Node:
    """
    Node Class is defined by:
    * Private instance attribute: data and next_node
    * a setter and getter for both data and next_node
    """
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        elif not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class is defined by:
    * Private instance attribute: head (no setter or getter)
    * Public instance method: def sorted_insert(self, value):
        that inserts a new Node into the correct sorted
        position in the list (increasing order)
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        if self.__head is None:
            self.__head = node
        elif self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            temp = self.__head
            while (temp.next_node is not None
                   and temp.next_node.data < value):
                temp = temp.next_node
            node.next_node = temp.next_node
            temp.next_node = node

    def __str__(self):
        data = []
        temp = self.__head
        while temp is not None:
            data.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(data)
