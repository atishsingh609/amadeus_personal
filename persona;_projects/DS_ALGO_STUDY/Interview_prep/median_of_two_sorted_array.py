def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    merged_arr = self.merge_array(nums1, nums2)
    mid = len(merged_arr) // 2
    res = (merged_arr[mid] + merged_arr[~mid]) / 2

    return res


def merge_array(self, arr1, arr2):
    ans = []
    k = 0
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i = i + 1
            k = k + 1
        else:
            ans.append(arr2[j])
            j = j + 1
            k = k + 1

    while j < len(arr2):
        ans.append(arr2[j])
        k = k + 1
        j = j + 1
    while i < len(arr1):
        ans.append(arr1[i])
        i = i + 1
    return ans