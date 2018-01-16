# isMatch(“aa”,”a”) → false
# isMatch(“aa”,”aa”) → true
# isMatch(“aaa”,”aa”) → false
# isMatch(“aa”, “a*”) → true
# isMatch(“aa”, “.*”) → true
# isMatch(“ab”, “.*”) → true
# isMatch(“aab”, “c*a*b”) → true

# ‘.’ Matches any single character.
# ‘*’ Matches zero or more of the preceding element.

def isMatch(string, test)
  s_idx = 0
  t_idx = 0
  while s_idx < string.length || t_idx < test.length
    print "s: "
    puts string[s_idx]
    print "t: "
    puts test[t_idx]
    if test[t_idx+1] == '*'
      if test[t_idx] == '.'
        temp = string[s_idx]
        while string[s_idx] == temp
          s_idx += 1
        end
      else
        while string[s_idx] == test[t_idx]
          s_idx += 1
        end
      end
      t_idx += 2
    else
      if test[t_idx] != string[s_idx] && test[t_idx] != '.'
        return false
      else
        s_idx += 1
        t_idx += 1
      end
    end
  end
  puts s_idx
  puts t_idx
  s_idx == string.length && t_idx == test.length
end

print("aa -> a: ")
puts isMatch("aa","a")# → false
print("aa -> aa: ")
puts isMatch("aa","aa")# → true
print("aaa -> aa: ")
puts isMatch("aaa","aa")# → false
print("aa -> a*: ")
puts isMatch("aa", "a*")# → true
print("aa -> .*: ")
puts isMatch("aa", ".*")# → true
print("ab -> .*: ")
puts isMatch("ab", ".*")# → true
print("aab -> c*a*b: ")
puts isMatch("aab", "c*a*b")# → true