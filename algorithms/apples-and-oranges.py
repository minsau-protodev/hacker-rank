# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def fill_array(size, filled):
  arr = []
  while (len(arr) < size):
    arr.append(0)

  for element in filled:
    arr[element - 1] = 1

  return arr

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    house = []
    for element in range(s, t + 1):
      house.append(element)

    x_axis = fill_array(b, house)

    apples_counter = 0
    oranges_counter = 0

    for apple in apples:
      pos = a + apple
      if ((pos > 0 and pos < b) and x_axis[pos - 1] == 1):
        apples_counter = apples_counter + 1

    for orange in oranges:
      pos = b + orange
      if ((pos > 0 and pos < b) and x_axis[pos - 1] == 1):
        oranges_counter = oranges_counter + 1
    print(x_axis)
    return (apples_counter, oranges_counter)

result = countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
print(result)

result = countApplesAndOranges(2, 3, 1, 5, [2], [-2])
print(result)
