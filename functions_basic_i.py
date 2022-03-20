#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# 5 will be the result.

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# Potential error due to number_of_days_in_a_week_silicon_or_triangle_sides being undefined.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# The result will range between 5 and 10.

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# The result will be 5.

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# The result will be 5 great lakes.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# The result will be between 3 and 5.

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# Potential error in the result.

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# Potential error in the result.

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# Possible error in the result.

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# The result will be 10.

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# 500 will be the result.

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# 500 will be the result.

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# Potential error in the result.

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# This looks like error potential.

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# The result will be between 5 and 10.