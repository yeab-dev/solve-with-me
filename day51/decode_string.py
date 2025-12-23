class Solution:
        
    def decodeString(self, s: str)-> str:
        def helper(i):
            result = ""
            num = 0

            while(i < len(s)):
                char = s[i]
                if char.isdigit():
                    num = num * 10 + int(s[i])
                elif char == '[':
                    decoded, i = helper(i+1)
                    result += decoded * num
                    num = 0
                elif char == ']':
                    return result, i
                else:
                    result += char

                i += 1
            return result,i
        decoded, _ = helper(0)
        return decoded