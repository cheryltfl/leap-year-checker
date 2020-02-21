##  Leap years are in multiples of four, but century years (i.e. every 100 years) do not follow this rule.
##  They must be multiples of 400 to be a leap year, so 1800, 1900 and 2100 are not leap years, but 1600, 2000 and 2400 are leap years.

start = int(input("What is the starting year: "))
end = int(input("What is the ending year: "))
for i in range(start, end + 1):
    if i % 400 == 0:
        print(str(i) + " is a century and leap year!")
    elif i % 100 == 0:
        print(str(i) + " is a century year and NOT a leap year.")
    elif i % 4 == 0:
        print(str(i) + " is a leap year!")
