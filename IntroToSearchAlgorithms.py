numbers = [7, 3, 21, 8, 79, 4, 5, 6, 23, 1, 2, 5]
# find the number 23 in this list and print it when we find it using a format
for x in range(len(numbers)):
  if numbers[x] == 23:
    print(numbers[x])

# this is called a linear search because we check every element in the sequence that they are in in their list. 

# Define a method for linear searcg that takes in a target and a list
def linearSearch(numbers, target):
  for x in range(len(numbers)):
    if numbers[x] == target:
      print(numbers[x])


# what would be a problem with this method that could arise? 
#efficiency. If we have a million items in our list that means we have to check a million things. 

# We can help this by having a sorted list like this one....
sortedNumbers = [1, 3, 14, 22, 34, 66, 87, 94, 102]
# If we have a list of sorted numbers ( meaning we know that the number to the left of the element we are on 
# is less than the element we are on, and the element to the right of whatever element we are on is greater than the element that we are on) 
# where would be the best place to start looking for our number?
#We will start right in the middle of the list but first let me declare some variables that we will need for the algorithm I am going to lay out
length = len(sortedNumbers)
midIndex = length / 2

def binarySearch(numbers, mid, target):
  if numbers[mid] == target:
    print(numbers[mid])
  elif numbers[mid] > target:
    return binarySearch(numbers, int(mid/2), target)
  else:
    return binarySearch(numbers, int(mid + ((len(numbers)-mid) / 2)), target)

# create another sorted list and try to find another target by calling this method again

binarySearch(sortedNumbers, 4, 34)
