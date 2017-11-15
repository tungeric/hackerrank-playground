expressions = ['{[()]}', '{[(])}', '{{[[(())]]}}']


# open_arr = [ '[', '{', '(']
# closed_arr = [ ']', '}', ')']

isBalanced?(expression)
  char_hash = { ']' => '[', '}' => '{', ')' => '(' }
  expression_arr = expression.chars
  should_be_open = true
  char_stack = []
  expression_arr.each do |char|
    if char_hash.values.include?(char)
      if should_be_open
        char_stack << char
      else
        return false
      end
    else
      should_be_open = false
      if char_stack[-1] == char_hash[char]
        char_stack.pop()
      else
        return false
      end
    end
  end
  return true
end

