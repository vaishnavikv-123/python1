txt1 ="hello, and welcome to my world."
txt2 ="Hello, And Welcome To My World!"
txt3 ="banana"
txt4 ="I love apples, apple are my favorite fruit"
txt5 ="My name is Minå"
txt6 ="50800"
txt7 ="   "
txt8 = "     banana     "
txt9 = "Mi casa, su casa."
txt10 = "apple, banana, cherry"
txt11 ="For only {price:.2f} dollars!"

x = txt1.capitalize()
print(x)

x = txt2.casefold()
print(x)

x = txt3.center(20)
print(x)

x = txt4.count("apple")
print(x)

x = txt5.encode()
print(x)

x = txt1.endswith(".")
print(x)
 
x = txt1.find("welcome")
print(x)

print(txt11.format(price =49))
 
x = txt1.index("welcome")
print(x)

x = txt3.isalnum()
print(x)

x = txt3.isalpha()
print(x)

x = txt3.isascii()
print(x)

x = txt3.isdecimal()
print(x)

x = txt6.isdigit()
print(x)

x = txt3.isidentifier()
print(x)

x = txt1.islower()
print(x)

x = txt6.isnumeric()
print(x)
 
x = txt1.isprintable()
print(x)

x = txt7.isspace()
print(x)

x = txt2.istitle()
print(x)

x = txt1.isupper()
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
 
x = txt2.lower()
print(x)

x = txt8.lstrip()
print("of all fruits", x, "is my favorite")

mytable = txt3.maketrans("a", "A")
print(txt3.translate(mytable))

x = txt1.partition("and")
print(x)

x = txt4.replace("apples","bananas")
print(x)

x = txt9.rfind("casa")
print(x)

x = txt9.rindex("casa")
print(x)

x = txt3.rjust(20)
print(x, "is my favorite fruit.")

x = txt4.rpartition("apple")
print(x)

x = txt10.rsplit(", ")
print(x)

x = txt8.rstrip()
print("of all fruits", x, "is my favorite")

x = txt2.startswith("Hello")
print(x)

x = txt2.swapcase()
print(x)

x = txt1.title()
print(x)

x = txt3.upper()
print(x)

x = txt6.zfill(10)
print(x)