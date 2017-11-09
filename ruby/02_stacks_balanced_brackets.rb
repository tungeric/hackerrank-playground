expressions = ['{[()]}', '{[(])}', '{{[[(())]]}}]']

char_hash = { ']' => '[', '}' => '{', ')' => '(' }
# open_arr = [ '[', '{', '(']
# closed_arr = [ ']', '}', ')']

expressions.each do |expression|
  expression_arr = expression.chars
  first_closed_idx = nil
  char_stack = []
  triggered = false
  expression_arr.each do |char|
    if char_hash.values.include?(char)
      char_stack << char
    else
      if char_stack[-1] == char_hash[char]
        char_stack.pop()
      else
        puts "NO"
        triggered = true
        break
      end
    end
  end
  puts "YES" if triggered == false
  triggered = false
end
  # expression_arr.each_with_index do |char, idx|
  #   if closed_arr.include?(char)
  #     first_closed_idx = idx
  #   end
  #   if first_closed_idx == nil || first_closed_idx == 0
  #     puts "NO"
  #     break
  #   else
  #     open_side = expression_arr[0...first_closed_idx].reverse
  #     closed_side = expression_arr[first_closed_idx..-1]
