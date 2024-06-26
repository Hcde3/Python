def binary_to_decimal(b):
    b = b[::-1]
    d = 0
    for i,u in enumerate(b):
        d += int(u)*(2**i)
    return d

def decimal_to_binary(d):
    d = int(d)
    b = ""
    while d > 0:
        b = str(d%2) + b
        d //= 2
    return b

def binary_addition(A,B):
    main = str(max([int(A),int(B)]))[::-1]
    less = str(min([int(A),int(B)]))[::-1]
    new = ""
    carried = 0
    for i,x in enumerate(main):
        just_carried = False
        if i > len(less)-1:
            less = less + "0"
        print(new)
        if [x,less[i]] == ["1","0"] or [x,less[i]] == ["0","1"]:
            new = "1" + new
        elif [x,less[i]] == ["0","0"]:
            new = "0" + new
        elif [x,less[i]] == ["1","1"]:
            new = "0" + new
            carried = 1
            if not just_carried:
                just_carried = True
        if carried and not just_carried:
            print(new, x)
            if new[0] == "0":
                new = "1" + new[1:]
                carried = 0
            elif new[0] == "1":
                new = "0" + new[1:]
                carried = 1
            print(new)
    if carried:
        new = "1" + new
    return new
        

#choice = input("Choose a Mode:\n(1) Binary to Decimal\n(2) Decimal to Binary\n(3) Binary Addition\n")
choice = "3"
if choice == "1":
    num1 = input("Input a binary number:   ")
    print(binary_to_decimal(num1))
elif choice == "2":
    num1 = input("Input a decimal number:   ")
    print(decimal_to_binary(num1))
elif choice == "3":
    num1 = input("Input your first binary number:   ")
    num2 = input("Input your second binary number:   ")
    print(binary_addition(num1,num2))