#!/usr/bin/env python

def max_subarray_brute_force(in_list):
    maximum = float('-inf')
    for i in range(1, len(in_list)):
        for j in range(i, len(in_list)):
            current_sum = 0
            for k in range(i, j):
                current_sum += in_list[k]
            maximum = max(maximum, current_sum)
    #print maximum
    return maximum


def max_subarray_brute_force_refined(in_list):
    max_sum = 0
    for i in range(len(in_list)):
        sub_sum = 0
        for j in range(i, len(in_list)):
            sub_sum += in_list[j]
            if sub_sum > max_sum:
                max_sum  = sub_sum
    return max_sum


def max_subarray_recursive(in_list, begin, end):
    if(begin == end):
        return(begin, end, in_list[begin])
    else:
        mid = floor((begin+end)/2)
        (left_begin, left_end, left_sum) = max_subarray_recursive(in_list, begin, end)
        (right_begin, right_end, right_sum) = max_subarray_recursive(in_list, mid+1, end)
        (cross_begin, cross_end, cross_sum) = max_subarray_cross(in_list, begin, mid, end)
        
    if(left_sum >= right_sum and left_sum >= cross_sum):
        return(left_low, left_high, left_sum)
    elif(right_sum >= left_sum and right_sum >= cross_sum):
        return(right_low, right_high, right_sum)
    else:
        return(cross_low, cross_high, cross_sum)

def max_subarray_cross(in_list, begin, mid, end):
    left_sum = 0
    current_sum = 0
    for i in range(mid, begin, -1):
        current_sum = current_sum + in_list[i]
        if(current_sum > left_sum):
            left_sum = current_sum
            maximum_left = i
    right_sum = 0
    current_sum = 0
    for j in range(mid+1, end, 1):
        current_sum = current_sum + in_list[j]
        if(current_sum > right_sum):
            right_sum = current_sum
            maximum_right = j
    return(maximum_left, maximum_right, left_sum,+right_sum)


def max_subarray_linear(in_list):
    
test_array = [-1, -1, -1, -1, -1, -1, -1, 42]

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

max_subarray_brute_force(array1)
#max_subarray_brute_force(array2)
#max_subarray_brute_force(array3)
