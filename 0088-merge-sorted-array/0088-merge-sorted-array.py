class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                m += 1
            else:
                i += 1
        if j < n:
            nums1[m:] = nums2[j:]
