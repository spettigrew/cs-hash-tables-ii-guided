 """
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

```plaintext
Input:
"free"

Output:
"eefr"

Explanation:
'e' appears twice while 'f' and 'r' appear once.
So 'e' must appear before 'f' and 'r'. Therefore, "eerf" is also a valid answer.
```

Example 2:

```plaintext
Input:
"dddbbb"

Output:
"dddbbb"

Explanation:
Both 'd' and 'b' appear three times, so "bbbddd" is also a valid answer.
Note that "dbdbdb" is incorrect, as the same characters must be together.
```

Example 3:

```plaintext
Input:
"Bbcc"

Output:
"ccBb"

Explanation:
"ccbB" is also a valid answer, but "Bbcc" is incorrect.
Note that 'B' and 'b' are treated as two different characters.
```
"""
def frequency_sort(s: str) -> str:
    """
    Inputs:
    s -> str

    Output:
    str
    """
    # Your code here

# Plan:
    # use a dictionary to store characters --> count
    # iterate through the string, adding the differents / incrementing the count
    dictionary = {}
    for char in s:  # O(n)
        if char not in dictionary:
            dictionary[char] = 1
        else:
            count = dictionary[char]
            dictionary[char] = count + 1

    # sort the keys in descending order (of the value)
    sorted_keys = sorted(dictionary, key=dictionary.get, reverse=True)  # O(n log n)
    print(sorted_keys)
    # create a collector string
    collector_string = []
    # iterating through the sorted keys
    for char in sorted_keys:  # O(n)
    #   add that val number of chars to the string
        count = dictionary[char]
    #   for example, if you had {"c": 3}, add "ccc" to the string
    #     for i in range(count):
    #         new_string += char
        print(char * count)
        chars = char * count  # if char = c, and count = 3, "ccc"
        collector_string.append(chars)  # add chars to the end of the list
        print(collector_string)

    # return the collector string
    return "".join(collector_string)

print(frequency_sort("free"))

    