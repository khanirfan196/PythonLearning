
# 'raise' keyword 
# This is use to trigger or raise an exception. This is mostly for debugging purpose.


def test_raise(x: int):
    try:
        if x < 0:
            raise Exception("x is less than 0.")
        else:
            return x
    except Exception as e:
        # print("in except block")
        # 'except' block catches the raised exception
        return e

print(test_raise(-1))
    