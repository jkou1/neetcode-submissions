class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(len(temperatures)-1):
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
                else:
                    j += 1



        return result