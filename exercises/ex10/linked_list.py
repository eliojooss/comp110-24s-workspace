"""Utility functions for working with Linked Lists."""

from __future__ import annotations

__author__ = "730484781"


class Node: 
    """An item in a singly-linked list."""
    data: int
    next: Node | None

    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str: 
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else: 
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return head."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return tail."""
        return self.next
    
    def last(self) -> int:
        """Return last."""
        last = self
        while last.next is not None:
            last = last.next
        return last.data

def value_at(head: Node | None, index: int) -> int:
    """Find value at an index."""
    if head == None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.data
    else: 
        return value_at(head.next, index -1 )
    
def max(head: Node | None) -> int:
    """Find the max."""
    if head == None:
        raise ValueError("Cannot call max with None")
    if head.next == None:
        return head.data
    else: 
        max_val = max(head.next)
        if head.data > max_val:
            return head.data
        else:
            return max_val
        
def linkify(items: list[int]) -> Node | None:
    if items == []:
        return None
    else:
        return Node(items[0], linkify(items[1:]))
    
def scale(head: Node | None, factor: int) -> Node | None:
    if head == None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))
