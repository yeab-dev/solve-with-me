from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = defaultdict(int)
        seen = set()
        stack = []

        for char in s:
            count[char] += 1

        for char in s:
            count[char] -= 1

            if char in seen:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)

        return "".join(stack)


# I was working on this for over an our and I couldn't solve
# it but I almost got it. I've managed to pass 275 out of 290
# then I ran to gpt and fixed my little bug. I know fully understand it.