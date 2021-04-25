def merge(self, arr1, arr2, n, m): 
        j=0
        i=n-1
        while j<m:
            if arr2[j]<arr1[i]:
                arr2[j],arr1[i]=arr1[i],arr2[j]
                i-=1
            j+=1
        arr1.sort()
        arr2.sort()
