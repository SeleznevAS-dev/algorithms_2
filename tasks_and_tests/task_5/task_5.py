def GenerateBBSTArrayRecursive(
    a: list[int], result: list[int], index: int
) -> list[int]:
    if a == []:
        return result

    middle_index = len(a) // 2
    result[index] = a[middle_index]

    left_part = a[:middle_index]
    right_part = a[middle_index + 1 :]

    result = GenerateBBSTArrayRecursive(left_part, result, 2 * index + 1)
    result = GenerateBBSTArrayRecursive(right_part, result, 2 * index + 2)

    return result


def GenerateBBSTArray(a: list[int]) -> list[int]:
    a.sort()
    result = [0] * len(a)
    return GenerateBBSTArrayRecursive(a, result, 0)


# 2.
# По сути, поиск так же получается за O(log N), эффективность такая же.
