
class OddNumberException(Exception):
    pass

num = int(input("Digite um número inteiro: "))

if num % 2 != 0:

    raise OddNumberException("O número digitado é ímpar.")
else:

    print("O número digitado é par.")
