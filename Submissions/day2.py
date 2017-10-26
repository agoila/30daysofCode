def get_total_cost_of_meal():
    # original meal price
    meal_cost = float(input())
    # tip percentage
    tip_percent = int(input())
    # tax percentage
    tax_percent = int(input())

    # Write your calculation code here
    tip = (tip_percent / 100) * meal_cost # calculate tip
    tax = (tax_percent / 100) * meal_cost # caclulate tax

    # cast the result of the rounding operation to an int and save it as total_cost 
    total_cost = int(round(meal_cost + tip + tax))
    
    return str(total_cost)

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")