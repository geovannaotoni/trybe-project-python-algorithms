def find_duplicate(nums):
    """Função que encontra o número que se repete da lista."""

    unique_nums = set()
    for num in nums:
        if type(num) is not int or num < 0:
            return False

        if num in unique_nums:
            return num
        else:
            unique_nums.add(num)

    return False
