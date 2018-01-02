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
