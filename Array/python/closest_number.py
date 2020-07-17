def closest_number(sorted_arr, tar):
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if tar == sorted_arr[mid]:
            return sorted_arr[mid]
        elif tar < sorted_arr[mid]:
            right = mid - 1
        elif tar > sorted_arr[mid]:
            left = mid + 1
    if right >= 0 and left < len(sorted_arr):
        if abs(sorted_arr[right] - tar) < abs(sorted_arr[left] - tar):
            return sorted_arr[right]
        else:
            return sorted_arr[left]
    elif right >= 0:
        return sorted_arr[right]
    else:
        return sorted_arr[left]


arr = [4]
print(closest_number(arr, 3))
