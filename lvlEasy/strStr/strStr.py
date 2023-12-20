# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/4422227/very-simple-and-fast-code-on-python/


def foo_str(haystack, needle):
    for i in range(0, len(haystack)):
        if haystack[i:len(needle) + i] == needle:
            return i
    return -1


print(foo_str("asadbutsad", "sad"))
