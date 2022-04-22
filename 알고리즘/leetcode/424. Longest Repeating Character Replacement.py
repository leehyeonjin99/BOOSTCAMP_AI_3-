import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        # sliding window에 있는 원소들을 Count하기 위한 수단
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            print("="*5 + f"left : {left} / right : {right}" + "="*5)
            counts[s[right-1]] += 1
            print("counts : ", counts)
            max_char_n = counts.most_common(1)[0][1]
            print("max_char_n : ", max_char_n)
            
            # s[left:right+1]이 same letter을 포함하는 substring이 되기 위해 바뀌어야하는 character의 수가 k보다 크다면 sliding window의 크기를 줄여야 한다.
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
