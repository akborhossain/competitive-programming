class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def marge(arr,l,m,h):
            left=arr[l:m+1]
            right=arr[m+1:h+1]
            i,j,k=l,0,0
            while j<len(left) and k<len(right):
                if left[j]<=right[k]:
                    arr[i]=left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                arr[i]=left[j]
                j+=1
                i+=1
            while k<len(right):
                arr[i]=right[k]
                k+=1
                i+=1
            

        def MargeSort(arr,L,H):
            if L==H:
                return arr
            mid=(L+H)//2
            MargeSort(arr,L,mid)
            MargeSort(arr,mid+1,H)
            marge(arr,L,mid,H)
            return arr
        return MargeSort(nums,0,len(nums)-1)
        