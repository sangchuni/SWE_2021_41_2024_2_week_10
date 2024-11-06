from typing import List

def even_list(int_list: List[int]) -> List[int]:
    """
    Determines if a number is even and return an even list.
    Args:
    int_list: A list of integer.
    Returns:
    A list of even integers.
    """
    pass

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum_squares = 0
    for num in even_int_list:
        sum_squares += num ** 2
    return sum_squares

def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()