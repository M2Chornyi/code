# https://leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string.

def add_binary(a, b):
  def swap(a, b):

    if len(a) < len(b):
      x = a
      a == b
      b == x  
      return a, b

  swap(a, b)

  print(a)
  print(b)



add_binary("11", "1")

add_binary("123", "1101")


# 1. Convert binary string to array
# 2. Find the length of the longest array
# 3. Create the array with the length of the longest array + 1
# 4.  




# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 10^4
# `a` and `b` consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
