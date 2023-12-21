# https://leetcode.com/problems/longest-common-prefix/
# https://leetcode.com/submissions/detail/1121419703/

def longest_common_prefix(strs):
    answer = ""
    sorted_strs = sorted(strs)
    for i in range(min(len(sorted_strs[0]), len(sorted_strs[-1]))):
        if sorted_strs[0][i] == sorted_strs[-1][i]:
            answer += sorted_strs[0][i]
            continue
        break
    return answer


print(["dog", "racecar", "car"])
