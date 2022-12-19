class Solution:
    

    def convertZig2(self,s,numRows):
        tailleDiagonale = numRows - 2
        longueurMotif = tailleDiagonale + numRows  
        finalString = ""

        if numRows == 1:
            return s


        for i in range(numRows):
            line = ""
            index = i
            isDiag = False
            
            #chaque motif 
            while(index<len(s)):
                    if i == 0 or i == numRows - 1:
                        line += s[index]
                        index+= longueurMotif

                    else: 
                        if not isDiag: 
                            line += s[index]
                            index += (longueurMotif - 2*i ) 
                            isDiag = True
                        else: 
                            line += s[index]
                            index+= 2*i
                            isDiag = False
                
            finalString+=line     
            print(line)
        return finalString        

                

soluce = Solution()
print(soluce.convertZig2("AB",2))  