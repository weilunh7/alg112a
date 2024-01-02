def min_edit_distance_recursive(str1, str2, i, j):
    # 如果有一个字符串为空，返回另一个字符串的剩余长度
    if i == 0:
        return j
    if j == 0:
        return i

    # 如果末尾字符相等，不需要操作
    if str1[i - 1] == str2[j - 1]:
        return min_edit_distance_recursive(str1, str2, i - 1, j - 1)

    # 否则，考虑三种操作：插入、删除、替换
    insert_cost = min_edit_distance_recursive(str1, str2, i, j - 1) + 1
    delete_cost = min_edit_distance_recursive(str1, str2, i - 1, j) + 1
    replace_cost = min_edit_distance_recursive(str1, str2, i - 1, j - 1) + 1

    # 返回最小操作次数
    return min(insert_cost, delete_cost, replace_cost)

# 示例
word1 = "kitten"
word2 = "sitting"
result = min_edit_distance_recursive(word1, word2, len(word1), len(word2))
print(f"最小編輯距離: {result}")

#有使用ChatGPT
#相關資料:https://www.gushiciku.cn/pl/gfpq/zh-tw
