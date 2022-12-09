import numpy as np
import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       con = np.hstack((nums1, nums2))
       con.sort()
       n=len(con)
       mod=np.median(con)
       return mod