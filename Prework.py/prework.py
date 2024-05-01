"Q1"
def hello_name(user_name):
    print(f"Hello, {user_name}!")

# Example usage:
hello_name("Jessica")

def first_odds():
    for num in range(1, 101, 2):  # Start from 1, go up to 100, step by 2 to get only odd numbers
        print(num)
"Q2"

def max_num_in_list(a_list):
    if not a_list:  # Check if the list is empty
        return None
    return max(a_list)

# Example usage:
print(max_num_in_list([1, 5, 3, 7, 2]))
"Q3"
def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False

# Example usage:
print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
"Q4"
def is_consecutive(a_list):
    return all(a_list[i] == a_list[i-1] + 1 for i in range(1, len(a_list)))
# Example usage:
print(is_consecutive([2, 3, 4, 5, 6, 7]))  # True
print(is_consecutive([1, 2, 4, 5]))  # False
