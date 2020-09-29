# Author: Laith Hayajneh lbh5303@psu.edu
# Collaborator: Saeed Alshebli saa6016@psu.edu
# collaborator: Yamin Zhang ykx5402@psu.edu
# collaborator: Kyle Kroboth kjk5884@psu.edu
# Section: 2
# Breakout: 5

def is_palindrom1(s):
  beg == 0
  end== -1
  while (s[beg] == s[end]):
    beg = beg + 1
    end = end - 1
  
 """
 This function returns True 
 if s is a palindrome, i.e., if s read the same backward as forward, returns False otherwise.
 You must implement this with a while loop that 
 compares characters in s one by one going forward vs. going backward 
 """

 beg = 0
 end = -1
 while (beg <= len(s)/2):
   if s[beg] != s[end]:
     return False
   beg = beg + 1
   end = end - 1
 return True

def is_palindrome2(s):
  """
 This function returns True if s is a palindrome, i.e.,
 if s reads the same backward as forward, returns False otherwise.
 You must implement this function with recursion. A string is a 
 palindrom only of its first character and its last 
 character are the same AND the middle (smaller) part is a palindrome.
 Use negative index to get the last character and use 
 slicing to get the middle of the string.
 """
 
   if s[0] != s[-1]:
     return False
    else:
      s = s[1:len(s)-1]
      is_palindrome2(s)
    if len(s) == 0
 return True 
def palindrom3(s):
  """
  This function returns True if s is a palindrome, ie.,
  if a reads the same backward as forward, returns False otherwise.
  You must implement this function with a one-liner.
  Use slicing (with step being -1) to get the reverse of a
  string, and a string is a palindrome if it is equivalent to its reverse
  """