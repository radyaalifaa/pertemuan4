a = int(input("masukan angka : "))
for hasil in range(1,a):
    if hasil%5==0 and hasil%3==0:
        print("fizzbuzz")
    elif hasil%5==0:
        print("buzz")
    elif hasil%3==0:
        print("fizz")
    else:
        print(hasil)