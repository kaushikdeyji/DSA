class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ordered_string = sorted(strs)
        if ordered_string[0] == "":
            return ""
        j = ordered_string[len(strs) - 1]
        i = ordered_string[0]
        temp =  [""]
        print(i,j)

        if len(i) >= len(j):
            for val in range(0,len(j)):
                if j[val] == i[val]:
                    temp.append(j[val])
                else:
                    return "".join(temp) 
        else:
            for val in range(0,len(i)):
                if j[val] == i[val]:
                    temp.append(j[val])
                else:
                    return "".join(temp) 
                   
        return "".join(temp)





         


        