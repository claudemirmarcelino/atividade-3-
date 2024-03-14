def verificar_string():
    string_usuario = input("Digite uma string: ")
    if not string_usuario.isupper():
        raise ValueError("A string contém letras minúsculas!")
    else:
        print("A string contém apenas letras maiúsculas!")

try:
    verificar_string()
except ValueError as e:
    print(e)
