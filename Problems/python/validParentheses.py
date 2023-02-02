#!/usr/bin/env python3
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pop_switch = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in pop_switch.values():
                stack.append(char)
            elif char in pop_switch.keys():
                if stack == [] or pop_switch[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
s = Solution()
print(s.isValid("()"))
print(s.isValid("(]"))
print(s.isValid("(){}[]"))
