# Grouping Hash
# Input: dishes: [["Salad","Tomato","Cucumber","Salad","Sauce"], 
              #  ["Pizza","Tomato","Sausage","Sauce","Dough"], 
              #  ["Quesadilla","Chicken","Cheese","Sauce"], 
              #  ["Sandwich","Salad","Bread","Tomato","Cheese"]]
# Output: [["Cheese","Quesadilla","Sandwich"], 
        #  ["Salad","Salad","Sandwich"], 
        #  ["Sauce","Pizza","Quesadilla","Salad"], 
        #  ["Tomato","Pizza","Salad","Sandwich"]]

def groupingDishes(dishes)
    ingredients = Hash.new(Array.new())
    dishes.each do |dish|
        i=1
        while i < dish.length
            ingredients[dish[i]] += [dish[0]]
            i += 1
        end
    end
    result = []
    ingredients.select { |ingredient, dishes| dishes.length >= 2 }.each do |ingredient, dishes|
        result << [ingredient, dishes.sort].flatten
    end
    result.sort_by { |ingredient| ingredient[0]}
end

# Following Patterns
# Input: strings: ["cat", 
                #  "dog", 
                #  "dog"]
        # patterns: ["a", 
                #  "b", 
                #  "b"]
# Output: true

def areFollowingPatterns(strings, patterns)
    i=0
    p_tracker = {}
    s_tracker = {}
    while i < strings.length
        if p_tracker[patterns[i]]
            if p_tracker[patterns[i]] != strings[i]
                return false
            end
        else
            p_tracker[patterns[i]] = strings[i]
        end
        if s_tracker[strings[i]]
            if s_tracker[strings[i]] != patterns[i]
                return false
            end
        else
            s_tracker[strings[i]] = patterns[i]
        end
        i += 1
    end
    true
end


