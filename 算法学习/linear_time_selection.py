import random


def randomized_partition(arr, low, high):
    """随机划分函数，返回划分点索引"""
    # 随机选择基准元素
    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_select(arr, low, high, k):
    """
    随机选择算法
    :param arr: 输入数组
    :param low: 当前子数组起始索引
    :param high: 当前子数组结束索引
    :param k: 要查找的第k小元素（从1开始计数）
    :return: 第k小的元素
    """
    if low == high:
        return arr[low]

    # 进行随机划分
    pivot_index = randomized_partition(arr, low, high)

    # 计算左半部分元素个数（包含基准）
    left_length = pivot_index - low + 1

    if k <= left_length:
        # 第k小元素在左半部分
        return randomized_select(arr, low, pivot_index, k)
    else:
        # 第k小元素在右半部分
        return randomized_select(arr, pivot_index + 1, high, k - left_length)


# 测试代码
if __name__ == "__main__":
    data = [12, 3, 5, 7, 4, 19, 26, 1, 8, 15, 10, 21]
    k = 6  # 查找第6小的元素

    # 注意：k是从1开始计数的
    result = randomized_select(data, 0, len(data) - 1, k)
    print(f"原始数组: {data}")
    print(f"排序后数组: {sorted(data)}")
    print(f"第{k}小的元素是: {result}")