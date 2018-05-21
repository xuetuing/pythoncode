def f1(a):
    print(a)
    a=input("input a:")
    if a:
        print(a)
        yield f1(a)
    for i in rang(3):
        print(i)

if __name__ == '__main__':
    f1("lo")
