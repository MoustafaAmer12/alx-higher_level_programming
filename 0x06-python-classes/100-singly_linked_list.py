#!/usr/bin/python3
"""A Module that handles creating Singly Linked Lists"""


class Node:
    """A node that has a data and a pointer to the next node"""
    def __init__(self, data, next_node=None):
        """Initializes a node class
        Attributes:
            data: data carried by the node
            next_node: node pointed to by the current one"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("next_node must be a Node object")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value == None or type(value) is type(self):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """A List of Nodes joined together"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        string = ""
        while current != None:
            string += str(current.data)
            if current.next_node != None:
                string += "\n"
            current = current.next_node
        return string

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head == None:
            self.__head = new
        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node != None:
                if current.next_node.data > new.data:
                    new.next_node = current.next_node
                    current.next_node = new
                    break
                current = current.next_node
            if current.next_node == None:
                current.next_node = new
