def longestPalindrome(self, s):
  """
  :type s: str
  :rtype: str
  """
  n = len(s)
  if n == 0:
      return ""

  # initialize the dp table
  dp = [[False] * n for _ in range(n)]
  start, max_length = 0, 1  # track the start and length of the longest palindrome

  # base cases: single character palindromes
  for i in range(n):
      dp[i][i] = True

  # base cases: two consecutive characters
  for i in range(n - 1):
      if s[i] == s[i + 1]:
          dp[i][i + 1] = True
          start, max_length = i, 2

  # fill the dp table for substrings of length >= 3
  for length in range(3, n + 1):  # length of the substring
      for i in range(n - length + 1):  # starting index
          j = i + length - 1  # ending index
          if s[i] == s[j] and dp[i + 1][j - 1]:
              dp[i][j] = True
              start, max_length = i, length

  # return the longest palindrome substring
  return s[start:start + max_length]

def longestPalindromeNotDP(s):
  """
  :type s: str
  :rtype: str
  """

  def expand_around_center(left, right):
      # expand as long as the characters match and within bounds
      while left >= 0 and right < len(s) and s[left] == s[right]:
          left -= 1
          right += 1
      # return the palindrome substring
      return s[left + 1:right]

  longest = ""
  for i in range(len(s)):
      # check odd-length palindromes
      odd_pal = expand_around_center(i, i)
      if len(odd_pal) > len(longest):
          longest = odd_pal
      
      # check even-length palindromes
      even_pal = expand_around_center(i, i + 1)
      if len(even_pal) > len(longest):
          longest = even_pal

  return longest