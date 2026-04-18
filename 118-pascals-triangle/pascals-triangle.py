class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            x=2
            arr = [[1],[1,1]]

            p = [1,1]

            while x<numRows:
                i = len(p) - 1
                newp = [None] * (len(p)+1)
                newp[0],newp[-1] = 1,1
                j=0
                while j < i:
                    temp= p[j]+p[j+1]
                    newp[j+1] = temp
                    j=j+1


                p=newp
                x = x + 1
                arr.append(p)
            return arr
        


