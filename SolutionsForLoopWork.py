#create a box with the letter X


'''
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
X X X X X X X X X
'''
row = "X X X X X X X X X"
for x in range(9):
  print(row)



#make a box
'''
 ____________________
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|____________________|
'''
# you may use the following variables to help you
top = " ____________________"
middle = "|                    |"
bottom = "|____________________|"

print()

for x in range(9):
  if x == 0:
    print(top)
  elif x == 8:
    print(bottom)
  else:
    print(middle)




#create a triangle with smaller triangles!
#you'll need this
triangle = "▲"
'''
▲
▲▲
▲▲▲
▲▲▲▲
▲▲▲▲▲
▲▲▲▲▲▲
▲▲▲▲▲▲▲
▲▲▲▲▲▲▲▲
▲▲▲▲▲▲▲▲▲
▲▲▲▲▲▲▲▲▲▲
'''
triangle = "▲"

triLine = ""
for x in range(10):
  triLine = triLine + triangle
  print(triLine)




#make the triangle alternate between Xs and Os
'''
0
01
012
0123
01234
012345
0123456
01234567
012345678
0123456789
'''
numbersLine = ""
for x in range(10):
  numbersLine = numbersLine + str(x)
  print(numbersLine)




#make a heart box with a line through it
'''
 ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
♥   ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
♥ ♥   ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
♥ ♥ ♥   ♥ ♥ ♥ ♥ ♥ ♥ 
♥ ♥ ♥ ♥   ♥ ♥ ♥ ♥ ♥ 
♥ ♥ ♥ ♥ ♥   ♥ ♥ ♥ ♥ 
♥ ♥ ♥ ♥ ♥ ♥   ♥ ♥ ♥ 
♥ ♥ ♥ ♥ ♥ ♥ ♥   ♥ ♥ 
♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥   ♥ 
♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥   
'''
#you may use the following variables
line = ""
heart = "♥ "
space = "  "

for x in range(10):
  for y in range(10):
    if x == y:
      line = line + space
    elif (x == 10 - y):
      line = line + space
    else:
      line = line + heart
  print(line)
  line = ""




#make the line go the other way (using the same variables from before)
'''
♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥   
♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥   ♥ 
♥ ♥ ♥ ♥ ♥ ♥ ♥   ♥ ♥ 
♥ ♥ ♥ ♥ ♥ ♥   ♥ ♥ ♥ 
♥ ♥ ♥ ♥ ♥   ♥ ♥ ♥ ♥ 
♥ ♥ ♥ ♥   ♥ ♥ ♥ ♥ ♥ 
♥ ♥ ♥   ♥ ♥ ♥ ♥ ♥ ♥ 
♥ ♥   ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
♥   ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
  ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
'''

#now make the lines go both ways!
'''
  ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥   
♥   ♥ ♥ ♥ ♥ ♥ ♥ ♥   ♥ 
♥ ♥   ♥ ♥ ♥ ♥ ♥   ♥ ♥ 
♥ ♥ ♥   ♥ ♥ ♥   ♥ ♥ ♥ 
♥ ♥ ♥ ♥   ♥   ♥ ♥ ♥ ♥ 
♥ ♥ ♥ ♥ ♥   ♥ ♥ ♥ ♥ ♥ 
♥ ♥ ♥ ♥   ♥   ♥ ♥ ♥ ♥ 
♥ ♥ ♥   ♥ ♥ ♥   ♥ ♥ ♥ 
♥ ♥   ♥ ♥ ♥ ♥ ♥   ♥ ♥ 
♥   ♥ ♥ ♥ ♥ ♥ ♥ ♥   ♥ 
  ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥  
'''

