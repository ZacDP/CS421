#!/usr/bin/env python
import math
import time

def max_subarray_brute_force(in_list):
    max_sum = -1
    for i in range(1, len(in_list) + 1):
        for j in range(0, len(in_list)):
            if j + i > len(in_list):
                break
            sum = 0;
            for k in range(j, j + i):
                sum += in_list[k]
                max_sum = max(max_sum, sum)
    return max_sum


def max_subarray_brute_force_refined(in_list):
    max_sum = -1
    for i in range(len(in_list)):
        sub_sum = 0
        for j in range(i, len(in_list)):
            sub_sum += in_list[j]
            if sub_sum > max_sum:
                max_sum  = sub_sum
    return max_sum


def max_subarray_cross(in_list, begin, mid, end):

    neg = -10000000000
    max_sum = 0
    for i in range(mid, begin - 1, -1):
        max_sum = max_sum + in_list[i]
        if max_sum > neg:
            neg = max_sum
            left_sum = i
    left = neg
    neg = -10000000000
    max_sum = 0

    for j in range(mid+1, end+1):
        max_sum = max_sum + in_list[j]
        if max_sum > neg:
            neg = max_sum
            right_sum = j
    right = neg

    return(left_sum, right_sum, left + right)

def max_subarray_recursive(in_list, begin, end):

    if end == begin:
        return begin, end, in_list[begin]

    else:

        mid = (begin+end)//2

        left_begin, left_end, left_sum = max_subarray_recursive(in_list, begin, mid)
        right_begin, right_end, right_sum = max_subarray_recursive(in_list, mid + 1, end)    
        cross_begin, cross_end, cross_sum = max_subarray_cross(in_list, begin, mid, end)         

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_begin, left_end, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_begin, right_end, right_sum
        else:
            return cross_begin, cross_end, cross_sum
        

def max_subarray_linear(in_list):
    begin = -1
    end = -1
    max_sum = 0
    begin_current = -1
    current_sum = 0
    for i in(in_list):
        if((current_sum + i)>0):
            if(current_sum == 0):
                begin_current = i
            current_sum = current_sum + i
        else:
            current_sum = 0
        if(current_sum > max_sum):
            max_sum = current_sum
            begin = in_list[0]
            end = i
    return(begin, end, max_sum)


test_array = [-1, -1, -1, -1, -1, -1, -1, 42]
test_array2 = [4, 2, 7, 1, 18, 42]

array1 = []
for i in range(0, 499):
    array1.append(-1)
array1.append(42)

array2 = []
for i in range(0, 999):
    array2.append(-1)
array2.append(42)

array3 = []
for i in range(0, 1999):
    array3.append(-1)
array3.append(42)

#print max_subarray_brute_force_refined(test_array)
#print max_subarray_linear(test_array)
#print max_subarray_recursive(test_array, 0, 7)
#print max_subarray_brute_force(test_array)
start = time.time()
print max_subarray_brute_force_refined(array1)
done = time.time()
print done - start
#max_subarray_brute_force(array2)
#max_subarray_brute_force(array3)
#max_subarray_linear(test_array)
