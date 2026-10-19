import random
import sys

sys.setrecursionlimit(200_000)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def partition(array, low, high, ascending):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        should_swap = (array[j] <= pivot) if ascending else (array[j] >= pivot)
        if should_swap:
            i += 1
            swap(array, i, j)
    swap(array, i + 1, high)
    return i + 1


def quick_sort_recursive(array, low, high, ascending):
    if low < high:
        pivot_index = partition(array, low, high, ascending)
        quick_sort_recursive(array, low, pivot_index - 1, ascending)
        quick_sort_recursive(array, pivot_index + 1, high, ascending)


def quick_sort(array, ascending=True):
    if len(array) <= 1:
        return
    quick_sort_recursive(array, 0, len(array) - 1, ascending)


def is_sorted(array, ascending=True):
    if len(array) <= 1:
        return True
    for i in range(len(array) - 1):
        if ascending and array[i] > array[i + 1]:
            return False
        if not ascending and array[i] < array[i + 1]:
            return False
    return True


sizes = [1_000, 10_000, 100_000]

for size in sizes:
    original = [random.uniform(0.0, 1000.0) for _ in range(size)]

    arr_asc = original.copy()
    quick_sort(arr_asc, ascending=True)
    print(
        f"Розмір: {size:<6} | Зростання | Впорядковано: {is_sorted(arr_asc, True)}"
    )

    arr_desc = original.copy()
    quick_sort(arr_desc, ascending=False)
    print(
        f"Розмір: {size:<6} | Спадання  | Впорядковано: {is_sorted(arr_desc, False)}"
    )
    print("-" * 55)

