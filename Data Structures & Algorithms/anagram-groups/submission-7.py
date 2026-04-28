class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agList = {}

        resList = []
        for string in strs:
            tempCpy = "".join(sorted(string))
            if tempCpy in agList:
                agList[tempCpy].append(string)
            else:
                # create a new kv pair
                agList[tempCpy] = [string]
        

        # at the end, we will take all lists in agList values
        # return them as one list of lists
        for val in agList.values():
            resList.append(val)
        return resList