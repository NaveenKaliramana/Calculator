#           Multitask Calculator
import math
def sum():
    global n
    try:
        n = eql()
        x = float(input("Enter a Number to add : "))
        n = n + x
        print(n)
        eql()
    except:
        print("Error Occured")
    finally:
        page1()
def diff():
    global n
    try:
        n = eql()
        x = float(input("Enter a Number to substract : "))
        n = n - x
        print(n)
        eql()
    except:
        print("Error Occured")
    finally:
        page1()
def mul():
    global n
    try:
        n = eql()
        x = float(input("Enter a Number to Multiply : "))
        n = n * x
        print(n)
        eql()
    except:
        print("Error Occured")
    finally:
        page1()
def div():
    global n
    try:
        n = eql()
        x = float(input("Enter a Number to Divide : "))
        n = n / x
        print(n)
        eql()
    except:
        print("Error Occured")
    finally:
        page1()
def pow():
    global n
    try:
        n = eql()
        p = int(input("Enter Power to find : "))
        n = n ** p
        print(n)
        eql()
    except:
        print("Error Occured")
    finally:
        page1()
def srt():
    global n
    try:
        n = eql()
        n = math.sqrt(n)
        print(n)
        eql()
    except:
        print("Error Occured")
    finally:
        page1()
def log():
    global n
    try:
        n = eql()
        b = float(input("Enter Base : "))
        n = math.log(n, b)
        print(n)
        eql()
    except:
        print("Error Occured")
    finally:
        page1()
def eql():
    global z
    z = n
    return z
def page1():
    print("+. Sum \n-. Substraction \n*. Multiplication \n/. Division \n^. Power \nrt/RT. Square Root \nlog. log \n=. Equal to \nq/Q. Quit")
    a = input("Enter Action to be Performed : ")
    if a == "+":
        sum()
    elif a == "-":
        diff()
    elif a == "*":
        mul()
    elif a == "/":
        div()
    elif a == "^":
        pow()
    elif a == "rt" or a == "RT":
        srt()
    elif a == "log":
        log()
    elif a == "=":
        res = eql()
        with open("Result.txt", "a") as f:
            f.write(f"{res}\n")
        print("Result : ", res)
    elif a == "q" or a == "Q":
        res = eql()
        with open("Result.txt", "a") as f:
            f.write(f"{res}\n")
        print("Result : ", res)
        exit
    else:
        print("Invalid Input")
        page1()
n = float(input("Enter a Number : "))
eql()
page1()