class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results=[]
        intervals.sort(key = lambda x : x[0])
        for idx, interval in enumerate(intervals):
            print(interval)
            if idx ==0:
                results.append(interval)
            else:
                start = interval[0]
                end = interval[1]
                count = 0
                for i, result in enumerate(results):
                    if start <= result[1] and count == 0:
                        print("first reset with", result, interval)
                        results[i] = [results[i][0], max(results[i][1], end)]
                        reset = i
                        new_end = max(results[i][1], end)
                        count+=1
                    elif count > 0 and  result[0] <= new_end :
                        print(count,"reset with", result, results[reset])
                        results.remove(result)
                        results[reset] = [results[reset][0], max(results[reset][1], result[1])]
                        reset = i
                        new_end = max(results[i][1], end)
                        count+=1
                if count ==0 :
                    results.append(interval)
        print()
        return results