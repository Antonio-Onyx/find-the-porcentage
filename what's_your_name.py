def full_name(first, last):
    x = f"hola {first} {last}, bienvenido a python"
    return x

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print(full_name(first_name, last_name))