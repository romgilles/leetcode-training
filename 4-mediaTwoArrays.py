class Solution:
    def findMedianSortedArrays(self, nums1,nums2) -> float:
        
        lenA = len(nums1)
        lenB = len(nums2)
        
        #find the longest table
        #a is the smaller 
        if lenA <= lenB:
            a = nums1
            b = nums2
        else: 
            a = nums2
            b = nums1
            lenA = len(nums2)
            lenB = len(nums1)

        #On traite le cas ou un des deux tableaux est vide         
        if lenA == 0:
            if lenB%2==0:
                return (b[int(lenB/2)]+b[int((lenB/2))-1]) / 2.0
            else:
                return b[int(lenB/2)]
        
        elif lenB==0:
            if lenA%2==0:
                return (a[lenA/2]+a[(lenA/2)+1])/2
            else:
                return a[int(lenA/2)]
            
        # on traite le cas commun 
        minIndex = 0
        maxIndex = lenA
        median = 0

        while(minIndex<=maxIndex):
            i = int((minIndex + maxIndex) / 2)
            j = int(((lenA + lenB + 1) / 2) - i)
            print("index",i,j)
            print("min-max",minIndex,maxIndex)
            #considérer i comme "les i premiers éléments du tableau A dans la partition gauche"
            #On teste si le premier élément du tableau droite B est supérieur au dernier du tableau gauche A
            if (i < lenA and j > 0 and b[j - 1] > a[i]):
                minIndex = i + 1
            #On teste si le dernier élément du tableau gauche A est inférieur au premier élément du tableau droite A
            #considérer j comme "les i premiers éléments du deuxième tableau dans la partition 2"
            elif (i > 0 and j < lenB and b[j] < a[i - 1]):
                maxIndex = i - 1
            
            #quand les conditions sont remplies 
            else:
                #aucun élément de A dans la partition gauche
                if (i == 0):
                    median = b[j - 1]
                #aucun élément de B dans la partition gauche
                elif (j == 0):
                    median = a[i - 1]
                else:
                    median = max(a[i - 1], b[j - 1])
                break
        if (lenA+lenB)%2 == 1:
            return median
        
        if i == lenA:
            return ((median+b[j]) / 2.0)
        if j == lenB:
            return ((median+a[i]) / 2.0)
        
        return ((median+ min(a[i],b[j])) / 2.0)
            

soluce = Solution()
print(soluce.findMedianSortedArrays([1,2,3],[4,5,6]))  
