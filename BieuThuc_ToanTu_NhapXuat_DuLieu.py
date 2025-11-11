# BieuThuc_ToanTu_NhapXuat_DuLieu.ipynb

def W2A1():
    print("Hello World!")

def W2A2():
    name = input().strip()
    print(f"Hello {name}")

def W2A3():
    a, b = map(int, input().split())
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(f"{a / b:.2f}")

def W2A4():
    a1, b1, c1, a2, b2, a3 = map(float, input().split())
    average = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
    print(f"{average:.1f}")

def W2A5():
    a, b = map(int, input().split())
    print(a ** b)

def W2A6():
    ch = input().strip()
    unicode_code = ord(ch)
    print(unicode_code)
    print(chr(unicode_code - 32))

def W2A7():
    A = ((13 ** 2) * 3) + 5
    B = 13**2 * 3 + 5
    print(A)
    print(B)

def W2A8():
    C = float(input())
    F = (9 / 5) * C + 32
    print(f"{F:.2f}")

def W2A9():
    x = float(input())
    total = x + 10
    total += total * 0.30 + total * 0.10
    print(f"{total:.2f}")

def W2A10():
    a, b, c = input().split()
    print(f"Hi {c}, {b} and {a}.")

def W2A11():
    h, m = map(int, input().split())
    print(h * 3600 + m * 60)

def W2A12():
    n = int(input())
    print(6 * n * n)

def W2A13():
    a, b = map(int, input().split())
    print((a * b) % 10)

def W2A14():
    a, b = map(int, input().split())
    a, b = b, a
    print(a, b)

def W2A15():
    n = int(input())
    star_number = n * (2 * n - 1)
    print(star_number)

def W2A16():
    seasons = ["Spring", "Summer", "Autumn", "Winter"]
    print("\n".join(seasons))

def W2A17():
    print("  *  ")
    print(" *** ")
    print("*****")

def W2A18():
    print("### # #     ### ###")
    print(" #  # #    #   #   #")
    print(" #  # #     #  #   #")
    print(" #  # #    #   #   #")
    print(" #  # # #       #   #")

def W2A19():
    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    print("\n".join(days))

def W2A20():
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    print("\n".join(months))

def W2A21():
    for _ in range(10):
        print("Hello, world")

if __name__ == "__main__":
    print("This file contains 21 exercises as separate functions.")
    print("Call the function you want to test, e.g., W2A1()")
