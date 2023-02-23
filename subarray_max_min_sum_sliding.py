#https://www.tutorialcup.com/interview/queue/sum-of-minimum-and-maximum-elements-of-all-subarrays-of-size-k.htm
#https://www.educative.io/courses/grokking-the-coding-interview/7D5NNZWQ8Wr


from re import sub


def get_subarr(arr,k):
    win_start = 0
    win_end = 0
    sub_arr = []
    output_sum= 0
    for win_end in range(len(arr)):
        sub_arr.append(arr[win_end])
        if win_end >= k-1:  
            output_sum = output_sum + min(sub_arr)+max(sub_arr)
            sub_arr[win_start] = 0
            win_start = win_start +1
    return output_sum



arr= [2, 5, -1, 7, -3, -1, -2]
k = 4

print(get_subarr(arr,k))
