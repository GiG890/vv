def greet(name):
    print(f"Здравствуйте, {name}")

def square(n):
    print(n**2)

def max_of_two(a, b):
    if a>b:
        print(a)
    else:
        print(b)

def describe_person(name, age=30):
    print(f"Имя: {name}, Возраст: {age} лет")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



