pizzabase = input('thick,thin')
pizzasize = input('small, medium, large')
basic_sauce = input('tomato, barbecue')
toppings = input('cheese, mushrooms, avocado, pineapple, bacon, chicken, fish')

#Price variables
thick = 10
thin = 5
small = 30
medium = 40
large = 50
tomato = 5
barbecue = 10
cheese = 5
mushrooms = 3
avocado = 7
pineapple = 5
bacon = 7
chicken = 7
fish = 6


if pizzabase == "thick":
    print('thick 10kr')
    pizzabase = 10
elif pizzabase == "thin":
    print('thin 5kr')
    pizzabase = 5
if pizzasize == "small":
    print('small 30kr')
    pizzasize = 30
elif pizzasize == "medium":
    print('medium 40')
    pizzasize = 40
elif pizzasize == "large":
    print('large 50')
    pizzasize = 50
if basic_sauce == "tomato":
    print('tomato 5kr')
    basic_sauce = 5
elif basic_sauce == "barbecue":
    print('barbecue 10kr')
    basic_sauce = 10
if toppings == "cheese":
    print('cheese 5kr')
    toppings = 5
elif toppings == "mushrooms":
    print('mushrooms 3kr')
    toppings = 3
elif toppings == "avocado":
    print('avocado 7kr')
    toppings = 7
elif toppings == "pineapple":
    print('pineapple 5kr')
    toppings = 5
elif toppings == "bacon":
    print('bacon 7kr')
    toppings = 7
elif toppings == "chicken":
    print('chicken 7kr')
    toppings = 7
elif toppings == "fish":
    print('fish 6kr')
    toppings = 6

total = pizzabase + pizzasize + basic_sauce + toppings
print(total, "kr")


