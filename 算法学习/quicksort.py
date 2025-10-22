def swap(arr, i, j):
    """交换数组中的两个元素"""
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, p, r):
    x = arr[p]  # 选第一个元素当"组长"（基准值）
    i = p  # 左指针（从左边开始）
    j = r + 1  # 右指针（从右边开始）

    while True:
        # 左指针向右移动：找比组长大的糖果
        i += 1
        while i <= r and arr[i] < x:  # 跳过比组长小的
            i += 1

        # 右指针向左移动：找比组长小的糖果
        j -= 1
        while j >= p and arr[j] > x:  # 跳过比组长大的
            j -= 1

        # 检查是否完成分区
        if i >= j:  # 指针相遇或交叉
            break  # 分区完成

        # 交换位置不对的糖果
        swap(arr, i, j)  # 把大的换到右边，小的换到左边

    # 把组长放到正确位置
    swap(arr, p, j)  # j位置是组长的最终位置
    return j  # 返回组长位置


def quick_sort(arr, p, r):
    if p < r:  # 还有糖果需要排序
        q = partition(arr, p, r)  # 分区，q是组长位置
        quick_sort(arr, p, q - 1)  # 排序左边小糖果
        quick_sort(arr, q + 1, r)  # 排序右边大糖果


# 使用示例
if __name__ == "__main__":
    data = [3, 6, 8, 10, 1, 2, 1]
    print("原始数组:", data)
    quick_sort(data, 0, len(data) - 1)
    print("排序后数组:", data)


