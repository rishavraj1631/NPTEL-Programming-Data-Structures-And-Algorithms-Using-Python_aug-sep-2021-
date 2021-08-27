# NPTEL-Programming-Data-Structures-And-Algorithms-Using-Python_aug-sep-2021-
code part of the code assignment is available here



Week 3 Programming Assignment


Due on 2021-08-26, 23:59 IST


Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
You may define additional auxiliary functions as needed.
In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
For each function, there are normally some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases. There are 12 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
Ignore warnings about "Presentation errors".


1.Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly increases.

Here are some examples of how your function should work.

  >>> expanding([1,3,7,2,9])
  True
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 9-2 = 7.

  >>> expanding([1,3,7,2,-3]) 
  False
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 2-(-3) = 5, so not strictly increasing.

  >>> expanding([1,3,7,10])
  False
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 10-7 = 3, so not increasing.






2.Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.

Here are some examples to show how your function should work.

>>> sumsquare([1,3,5])
[35, 0]

>>> sumsquare([2,4,6])
[0, 56]

>>> sumsquare([-1,-2,3,7])
[59, 4]




3.A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

1  2  3  4
5  6  7  8
would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].

The transpose of a matrix converts each row into a column. The transpose of the matrix above is:

1  5
2  6
3  7
4  8
which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].

Write a Python function transpose(m) that takes as input a two dimensional matrix m and returns the transpose of m. The argument m should remain undisturbed by the function.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

>>> transpose([[1,2,3],[4,5,6]])
[[1, 4], [2, 5], [3, 6]]

>>> transpose([[1],[2],[3]])
[[1, 2, 3]]

>>> transpose([[3]])
[[3]]


