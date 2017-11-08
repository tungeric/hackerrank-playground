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

if n > m
  puts "No"
else
  trigger = false
  counter_ran.each do |k, v|
    if counter_mag[k] < v
      puts "No"
      trigger = true
      break
    end
  end
  puts "Yes" if trigger == false
end