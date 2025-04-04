def test_merge_sort(arr):
    """
    Sorts a list in ascending order using Merge Sort algorithm
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists
    Combine: Merge the sorted sublists
    """
    
    if len(arr) <= 1:
        return arr
    
    # Divide phase
    left_half, right_half = test_split(arr)
    
    # Conquer phase (recursion)
    left = test_merge_sort(left_half)
    right = test_merge_sort(right_half)
    
    # Combine phase
    return test_merge(left, right)

def test_split(arr):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return left, right

def test_merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """
    l = []
    i = 0  # left list index
    j = 0  # right list index
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    # When one list is longer than the other
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j += 1
        
    return l

# Test the implementation
if __name__ == "__main__":
    test_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]
    sorted_list = test_merge_sort(test_list)
    print("Original:", test_list)
    print("Sorted:", sorted_list)
