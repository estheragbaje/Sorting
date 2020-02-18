# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )

    # merged_arr = [0] * elements
    # TO-DO
    #set merged array to empty list
    merged_arr = []
   
    #check which array should come first
    while len(arrA) and len(arrB) != 0:  
      if arrA[0] > arrB[0]:
        merged_arr.append(arrA)
      else:
        merged_arr.append(arrB)


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

"""
Divide the original array in half till only subarrays of 1 are left, index 0, base case
if arr[0] < arr[0], stay same and merge, else swap and merge, recursive call
repeat the same process till all have been merged


"""

def merge_sort( arr ):
    # TO-DO
    #base case, when only one item should be in the array
    if len(arr) < 2:
      return arr
    else:
      #divide the array into halves
      arr_half = len(arr)//2
      left_arr = arr[:arr_half]
      right_arr = arr[arr_half:len(arr)]

      #using the merge function above to combine the 2 arrays
      return merge(left_arr, right_arr)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
