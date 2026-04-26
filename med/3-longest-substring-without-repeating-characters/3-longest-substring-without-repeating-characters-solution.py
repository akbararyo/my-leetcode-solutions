class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a="" #word bank
        b=[] #collection of words

        #testing logic -> find
        # e=[s[1:]]
        # c=s.find("a")
        # print(f"e={e}, c={s[c+1:]}")

        for i in range(len(s)):
            if len(a) == 0:
                a = s[i]
                b.append(a)
            else:
                if s[i] not in  a:
                    a += s[i]
                    b.append(a)
                else:
                    b.append(a)
                    same_index = a.find(s[i])
                    a = a[same_index+1:] + s[i] #what index is the same letter in word bank and then remake the word bank from after that same letter also dont forget to add the current letter -> s[i]
                    # print(f"a in else before if = {a}")
        
        max=0 #longest substring
        for i in b:
            if len(i) > max:
                max = len(i)
        # print(f"b={b}")
        # print(f"max={max}")
        return max

# for the first word just directly add it to word bank. Check if the current index already in a or not: a. if no, add to the word bank then ad it to collections just in case it is already the longest substring. b. if yes,  directly add to the collections bcs it is the longest substring for now, then we need to look for the index of that same letter, then update the word bank begin from the after that same letter + add current index letter. That's all, so the collections is complete.
#look for the longest substring from collections using variable max, then return it.
