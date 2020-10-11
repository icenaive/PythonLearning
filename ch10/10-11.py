import json

file_name = "10-11names.json"

def get_stored_username():
    try:
        with open(file_name) as file1:
            nums = json.load(file1)
    except FileNotFoundError:
        return None
    else:
        return nums

def get_new_username():
    nums = input("input your xihuan nums: ")
    with open(file_name, 'w') as file1:
        json.dump(nums, file1)
    return nums


def greet_user():
    nums = get_stored_username()
    if nums:
        print("your xihuan num is %d" % int(nums))
    else:
        nums = get_new_username()
        print("you is a new name ans your xihuan num is %d" % int(nums))

greet_user()