def round_grade(x):
  next_five_value = (x - (x % 5)) + 5
  if x >= 38 and (next_five_value - x) < 3:
    return next_five_value
  return x

def gradingStudents(grades):
    # Write your code here
    return list(map(lambda grade: round_grade(grade), grades))

print(gradingStudents([73, 67, 38, 33]))