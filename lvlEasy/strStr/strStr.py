def foo_str(haystack, needle):
    for i in range(0, len(haystack)):
        if haystack[i:len(needle) + i] == needle:
            return i
    return -1


print(foo_str("asadbutsad", "sad"))
