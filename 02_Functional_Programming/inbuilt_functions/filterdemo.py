
# Filter function works same as map, 
# but it does filter values or elements
# based on the condition provided in function which is first parameter.


# syntax 
# x = filter(func, elements) # elements could be a list or set (iterable)

ages = [18, 25, 30, 14, 12, 8, 35, 40]

def validate_age(age):
    if age > 18:
        return True
    else:
        return False


filtered_ages = filter(validate_age, ages)

print(filtered_ages)
print(type(filtered_ages))

for age in filtered_ages:
    print(age)