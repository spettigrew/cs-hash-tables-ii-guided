"""
Your task is create your own HashTable without using a built-in library.
​
Your HashTable needs to have the following functions:
​
- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.
​
Example:
​
```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashTable:

    def __init__(self):
        self.num_items = 0
        self.array = [None] * 20

    def put(self, key, value):
        # We need an array to store the values in
        # Need to turn the key to index
        # Hash the key (map it to an integer in a finite space)
        hashed_key = hash(key)
        # Map the hashed key to an index in the array by % len(array)
        index = hashed_key % len(self.array)
        # PLAN for collisions:
        # Check if there’s something at the index
        if self.array[index] is not None:
            # If so, check if the key is at that index. By iterating over the list
            current = self.array[index]
            while current is not None:
                if current.key == key:
                    # If it does, overwrite the value for the node where the key is the same
                    current.value = value
                    return  # We updated the value, so we don't need to do anythign else
                current = current.next
            # Otherwise, add it to the list
            new_node = ListNode(key, value)
            # add it to the front of the list
            new_node.next = self.array[index]
            self.array[index] = new_node  # update the head of the list

        # If there’s nothing at the index:
        else:
        # Set array[index] to point to the new node
            self.array[index] = ListNode(key, value)

    def get(self, key):
        # PLAN: return the value at the index of the key
        # hash the key, map it to the index, and then return the value at that index in the array
        hashed_key = hash(key)
        index = hashed_key % len(self.array)
        if self.array[index] is None:
            return -1
        # PLAN for collisions
        # we need iterate through the list
        current = self.array[index]
        while current is not None:
            # check if the current_node.key == key:
            if current.key == key:
                #   if it is, return the corresponding value
                return current.value
            current = current.next
        # if we get to the end of the list and haven't found a match, return -1 to signal it wasn't there
        return -1

    def remove(self, key):
        hashed_key = hash(key)
        index = hashed_key % len(self.array)

        # iterate through the linked list at index
        previous = None
        current = self.array[index]
        while current is not None:
        # find the node with the matching key
            if current.key == key:
                # remove the node
                # Keep track of prev and cur
                # Prev.next = cur.next
                if previous is not None:
                    previous.next = current.next
                else:
                    # we're at the head
                    self.array[index] = current.next
                # Set cur.next to none
                current.next = None
            previous = current
            current = current.next


hash_table = MyHashTable()
hash_table.put("a", 1)
hash_table.put("b", 2)
print(hash_table.get("a"))  # returns 1
print(hash_table.get("b"))  # returns 2
print(hash_table.get("c"))  # returns - 1(not found)

hash_table.put("b", 1)  # update the existing value
print(hash_table.get("b"))  # returns 1
hash_table.remove("b")  # remove the mapping for 2
print(hash_table.get("b"))  # returns - 1(not found)


hash_table_2 = MyHashTable()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in alphabet:
    hash_table_2.put(char, char)

for char in alphabet:
    print(char, hash_table_2.get(char))
