def f1():
    print("f1 called...")

    def f2():
        print("f2 called...")
    
    return f2


x = f1()

x()
