# https://leetcode.com/problems/longest-common-prefix/
# https://leetcode.com/submissions/detail/1121419703/
strs = ["dog", "racecar", "car"]

answer = ""
sortedStrs = sorted(strs)
for i in range(min(len(sortedStrs[0]), len(sortedStrs[-1]))):
    if sortedStrs[0][i] == sortedStrs[-1][i]:
        answer += sortedStrs[0][i]
        continue
    break
print(answer)
