
# This function accepts two integers as arguments
def age(birth, current):
    #birth and age act as local variables,
    #they don't need to match the variable names used in the calling code
    my_age = current-birth
    str_age = str(my_age)
    print("I am " + str_age + " years old")


birth_year = 1971
current_year = 2016

#you can call the function by passing variables
age(birth_year, current_year)

#you can call the function by passing values
age(1969, 2016)
