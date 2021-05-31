import numpy as np
#from numpy.linalg import inv, qr

def new():
    global i
    print("Matrix ", i)
    r = int(input("Number of rows of matrix: "))
    c = int(input("Number of columns of matrix: "))
    elements = list(map(int, input().split()))
    while len(elements) != r * c:
        print("Enter the entries again:")
        elements = list(map(int, input().split()))
    matrx = np.array(elements).reshape(r, c)
    
    i += 1
    return matrx

def add(a, b):
    if a.shape != b.shape:
        return None
    return a + b

def multiply(a, b):
    if a.shape[1] != b.shape[0]:
        return None
    return a@b

def inverse(a):
    if a.shape[0] != a.shape[1]:
        return None
    elif  np.linalg.det(a) == 0:
        return None
    else:
        return np.linalg.inv(a)

#def main()
i = 1
a = new()
print(a)

b = new()
print(b)
list_op = ['+', '-', '*', 'T', 'inv', 'quit']
op = input("Operation: ")

while op != 'quit':
    while op not in list_op:
        op = input("Enter again: ")
    if op != 'quit':
        if op == '+':
            result = add(a, b)
            if result is None:
                print("Error")
            else:
                print("a + b = \n", result)
        elif op == '-':
            result = add(a, -b)
            if result is None:
                print("Error")
            else:
                print("a - b = \n", result)
        elif op == '*':
            result = multiply(a, b)
            if result is None:
                print("Error")
            else:
                print("a * b = \n", result)
                    
        elif op == 'T':
            matrix = input("Which matrix? ")
            while matrix != 'a' and matrix != 'b':
                matrix = input("Enter again: ")

            if matrix == 'a':
                print("a(T) = \n", np.transpose(a))
            else:
                print("b(T) = \n", np.transpose(b))

        elif op == 'inv':
            matrix = input("Which matrix? ")
            while matrix != 'a' and matrix != 'b':
                matrix = input("Enter again: ")

            if matrix == 'a':
                result = inverse(a)
                if result is None:
                    print("Error")
                else:
                    print("a^(-1) = \n", result)
            else:
                result = inverse(b)
                if result is None:
                    print("Error")
                else:
                    print("b^(-1) = \n", result)
        op = input("Operation: ")

