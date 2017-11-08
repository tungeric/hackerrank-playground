m = 6
n = 5

magazine = "two times three is not four".split(" ")
ransom = "two times two is four".split(" ")

counter_mag = Hash.new(0)
counter_ran = Hash.new(0)

magazine.each do |word|
  counter_mag[word] += 1
end

ransom.each do |word|
  counter_ran[word] += 1
end

total_words = n

puts counter_mag
puts counter_ran