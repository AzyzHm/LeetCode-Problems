# 20.Valid Parentheses
Given a string s containing just the characters <code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
 

### Example 1:

- Input: <code>s = "()"</code>
- Output: <code>true</code>
### Example 2:

- Input: <code>s = "()[]{}"</code>
- Output: <code>true</code>
### Example 3:

- Input: <code>s = "(]"</code>
- Output: <code>false</code>
 

## Constraints:

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.