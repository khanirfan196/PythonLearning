
from utils.exception_utility import divide_numbers

numbers_dict = {
    10 : 2,
    15 : 3,
    16 : 4,
    7 : 0,
    8 : 2,
    20 : 10
}


for k, v in numbers_dict.items():
    try:
        result = divide_numbers(k, v)
        #print(result)
    except Exception as e:
        print(f"Raised Exception. Error message: {e}")
        continue

    print(f"Division results of {k} and {v} are: {result}")