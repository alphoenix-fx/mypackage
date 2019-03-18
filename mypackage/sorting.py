import random
import numpy as np



def bubble_sort(items):
    '''
        Bubble sort is one of the most basic sorting algorithm that is the simplest
         to understand. It’s basic idea is to bubble up the largest(or smallest)

         Parameters
         ----------
         items : list
             The 2nd largest and the the 3rd and so on to the end of the list. Each bubble
             up takes a full sweep through the list.

         Returns
         -------
         list
             list of elements in items in ascending order
    '''
    out = items.copy()
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]

    return out


def merge_sort(items):
    '''Return array of items, sorted in ascending order

    Merge sort works by subdividing the the list into two sub-lists, sorting them using
    Merge sort and then merging them back up.
    Parameters
    ----------
    items : list
        list of unordered numbers as the recursive call is made to subdivide each list into a sublist,
        they will eventually reach the size of 1, which is technically a sorted list.

    Returns
    -------
    list
        list of elements in items in ascending order
    '''
    def merge(A, B):
        new_list = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                new_list.append(A[0])
                A.pop(0)
            else:
                new_list.append(B[0])
                B.pop(0)

        if len(A) == 0:
            new_list = new_list + B
        if len(B) == 0:
            new_list = new_list + A

        return new_list



    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)


def quick_sort(items):
    '''The quick sort algorithm takes in an unsorted list of numbers.
    returns a list in ascending order.

    Parameters
    ----------
    items : list
        list of unordered numbers
    index: int, optional
        index number at which to choose the split value
        default set to the last item in the input list

    Returns
    -------
    list
        list of elements in items in ascending order
    '''
    len_i = len(items)
    index=-1
    if len_i <= 1:
        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
