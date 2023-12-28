def count_negatives(grid):
    count = 0
    for row in grid:
        m = -1
        while True:
            if abs(m) <= len(row) and row[m] < 0:
                m -= 1
                count += 1
            else:
                break
    return count


print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
