"""
You are given a non-empty list of words.

Write a function that returns the *k* most frequent elements.

The list that you return should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical
order should come first.

Example 1:

```plaintext
Input:
words = ["lambda", "school", "rules", "lambda", "school", "rocks"]
k = 2

Output:
["lambda", "school"]

Explanation:
"lambda" and "school" are the two most frequent words.
```

Example 2:

```plaintext
Input:
words = ["the", "sky", "is", "cloudy", "the", "the", "the", "cloudy", "is", "is"]
k = 4

Output:
["the", "is", "cloudy", "sky"]

Explanation:
"the", "is", "cloudy", and "sky" are the four most frequent words. The words
are sorted from highest frequency to lowest.
```

Notes:

- `k` is always valid: `1 <= k <= number of unique elements.
- words in the input list only contain lowercase letters.
```
"""
def top_k_frequent(words, k):
    """
    Input:
    words -> List[str]
    k -> int

    Output:
    List[str]
    """
    # Your code here
 # UNDERSTAND
    # words only contain lowercase letters, no weird numbers or symbols
    # input: words (list of strings) and k (int)
    # -- we want to return the k most frequent words (so if k = 2, return the top 2 most frequent words)
    # output: list of strings

    # PLAN
    # we could potentially use python's list.count() --> O(n^2)
        # list.count(x) returns the number of times x appears in the list
        # so we would have to iterate through the list, and do list.count on almost every element in the list

    # we want to know the total number of times each word appears
    # use a dictionary to store the words as keys and number of appearances as values
    dictionary = {}
    # iterate through words
    for word in words:
        # if the word is in the dictionary, increment the count
        if word in dictionary:
            dictionary[word] += 1
        # if not, add it and set it to 1
        else:
            dictionary[word] = 1

    print(dictionary)

    # iterate over the values and return the keys for the top k (alphabetically for ties)
    # option 1: sort the keys based on the values
    sorted_keys = sorted(dictionary, key=lambda x: (-dictionary[x], x))
    print(sorted_keys)
    # return sorted(sorted_keys)

    return sorted_keys[:k]

    # counts_to_words = {}
    # for word, count in dictionary.items():
    #     if count in counts_to_words:
    #         counts_to_words[count].append(word)
    #     else:
    #         counts_to_words[count] = [word]
    # print(counts_to_words)
    # sorted_counts = sorted(counts_to_words.keys(), reverse=True)
    # print(sorted_counts)
    # top_k_frequent = []
    # for count in sorted_counts:
    #     sorted_words = sorted(counts_to_words[count])
    #     top_k_frequent.extend(sorted_words)
    #     if len(top_k_frequent) >= k:
    #         return top_k_frequent[0:k]

    # option 2: get max() k times and remove from hash table.

print(top_k_frequent(["the", "sky", "is", "cloudy", "the", "the", "the", "is", "is"], 4))




