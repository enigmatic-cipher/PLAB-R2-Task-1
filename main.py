"""
Given a list of size n as input. Print the sum of smallest and largest element from this list.
Input-> [1,5,9,7]
Output-> 10
"""

ls =  [1,5,9,7]
min = ls[0]
max = ls[0]
ln = len(ls)
for i in range(0,ln):
  e = ls[i]
  if ls[i]<min:
    min = ls[i]
  elif ls[i]>max:
    max = ls[i]
print(min+max)