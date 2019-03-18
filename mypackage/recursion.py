import random
import numpy as np


def sum_array(array):
    '''
    Given an array of integers, find sum of array elements using recursion

     Parameters
     ----------
     array : integer
        find sum of array elements using recursion.

     Returns
     -------
     sum of all items in array
    '''
    if len(array)== 1:
        return array[0]
    else:
        return array[0]+sum_array(array[1:])


def fibonacci(n):
    '''
    The Fibonacci sequenceis characterized by the fact that every number
    after the first two is the sum of the two preceding ones

     Parameters
     ----------
     n : integer
        Sum the numbers where the first two is the sum of the two preceding ones

     Returns
     -------
     nth term in fibonacci sequence
    '''
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def factorial(n):
    '''
    the Fibonacci sequenceis characterized by the fact that every number
    after the first two is the sum of the two preceding ones

     Parameters
     ----------
     items : list
         The 2nd largest and the the 3rd and so on to the end of the list. Each bubble
         up takes a full sweep through the list.

     Returns
     -------
     n factorial
    '''
    if n == 0:
            return 1
    else:
        return n * factorial(n-1)


def reverse(word):
    '''
    Given a string str, returns reverse all words
     Parameters
     ----------
     word : string
         reverse the string such that the last word becomes the first
         and the first become s the last

     Returns
     -------
     word in reverse'''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
