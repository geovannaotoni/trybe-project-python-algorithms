def is_palindrome_iterative(word):
    """Função que verifica se uma palavra é um palíndromo."""
    if len(word) == 0:
        return False

    # opção 1: com range
    for i in range(len(word)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

    # opção 2: com slicing
    # if word != word[::-1]:
    #     return False
    # return True
