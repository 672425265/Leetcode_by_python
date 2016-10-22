# coding: utf-8

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dummyNode = Node(-1, -1)
        self.tail = self.dummyNode
        self.entryFinder = {}

    def renew(self, entry):
        if self.tail != entry:
            entry.prev.next = entry.next
            entry.next.prev = entry.prev
            entry.next = None
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry

    def get(self, key):
        entry = self.entryFinder.get(key)
        if entry is None:
            return -1
        else:
            self.renew(entry)
            return entry.val

    def set(self, key, value):
        entry = self.entryFinder.get(key)
        if entry is None:
            entry = Node(key, value)
            self.entryFinder[key] = entry
            self.tail.next = entry
            entry.prev = self.tail
            self.tail = entry
            if self.size < self.capacity:
                self.size += 1
            else:
                headNode = self.dummyNode.next
                self.dummyNode.next = headNode.next
                headNode.next.prev = self.dummyNode
                del self.entryFinder[headNode.key]
        else:
            entry.val = value
            self.renew(entry)