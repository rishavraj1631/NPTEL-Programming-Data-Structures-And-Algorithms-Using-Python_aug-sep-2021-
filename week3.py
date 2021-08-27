# NPTEL-Programming-Data-Structures-And-Algorithms-Using-Python_aug-sep-2021-
code part of the code assignment is available here

code...............................................

def expanding(l):
    a=0
    for i in range(1,len(l)):
        if a >= abs(l[i]-l[i-1]):
            return False
        a=abs(l[i]-l[i-1])
    else:
        return True
      

def sumsquare(l):
  odd=0
  even=0
  length=len(l)
  for i in range(length):
    if l[i]%2==0:
      even=even+l[i]*l[i]
    else:
      odd=odd+l[i]*l[i]
  l=[odd,even]
  return(l)     
  
 
 def transpose(l1):
  l2=[]
  for i in range(len(l1[0])):
    row=[]
    for item in l1:
      row.append(item[i])
    l2.append(row)
  return l2
  
