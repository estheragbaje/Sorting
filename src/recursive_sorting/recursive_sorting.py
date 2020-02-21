# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )

    # merged_arr = [0] * elements
    # TO-DO
    #set merged array to empty list
    merged_arr = []
    i, j = 0, 0
   
    #check which array should come first
    while len(arrA) and len(arrB) != 0 and len(merged_arr) < elements :  
    

      if arrA[i] < arrB[j]:
        merged_arr.append(arrA[i]) 
        i += 1
      else:
        merged_arr.append(arrB[j])
        i += 1

      # if j == len(arrB):
      #   merged_arr += arrA[i:]
      #   break
      # elif i == len(arrA):
      #   merged_arr += arrB[j:]

    return merged_arr

# c= []
# a = [2, 3, 4, 5]
# b= [6, 7, 8, 9, 10, 11, 12]



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
