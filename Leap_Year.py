"""check whether a given year is leap or not """

year=int(input("Pls Enter Year "))
if(year>=999 and year<=9999):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
             print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
else:
    print("incorrect input ! pls Enter 4 digit Number ")
