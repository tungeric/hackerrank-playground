# Input:
# 4
# 73
# 67
# 38
# 33

# Output: 
# 75
# 67
# 40
# 33

# https://www.hackerrank.com/challenges/grading/problem

def solve(grades)
    # Complete this function
  result = []
  grades.each do |grade|
    rounded_up = (grade.to_f/5).ceil * 5
    if rounded_up - grade.to_i < 3 && rounded_up >= 40
      result << rounded_up
    else
      result << grade.to_i
    end
  end
  result
end

n = gets.strip.to_i
grades = Array.new(n)
for grades_i in (0..n-1)
    grades[grades_i] = gets.strip.to_i
end
result = solve(grades)
print result.join("\n")


