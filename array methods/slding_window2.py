# another way of implementing the sliding window technique

from typing import List


def fixed_solution(arr: List[int], k: int) -> List[int]:
    curr_subarr = sum(arr[:k]) # starts at the beginning of the array and goes up until the kth element and sums up all the elements in there
    result = [curr_subarr] # result list that starts with curr_subarr

    for i in range(1, len(arr) - k + 1):
        curr_subarr = curr_subarr - arr[i - 1]  # substracts the element before the begining of the original 'curr_subarr'
        curr_subarr = curr_subarr + arr[i + k - 1] # adds the element after the end of the original 'curr_subarr'
        result.append(curr_subarr) # appends the results to the 'result' list
    return result # returns list 
