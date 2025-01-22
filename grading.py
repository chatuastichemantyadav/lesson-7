marks=int(input("write your marks"))

if marks<5:
    print("your grade is E2, you have failed")
elif marks<20:
    print("your grade is E1, you have failed")
elif marks<40:
    print("your grade is F, you have failed")
elif marks<65:
    print("your grade is D, you have passed barely")
elif marks<75:
    print("your grade is C, you have passed with a decent grade ")
elif marks<80:
    print("your grade is B, you have passed with a good grade")
elif marks>90:
    print("your grade is A, you have passed with an EXCELENT grade")