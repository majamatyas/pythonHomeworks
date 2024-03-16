import math

#exercises 3.1

reply = input("Podaj wyraz:")

border = "+"
wordLine ="|"

for char in reply:
     border += "---+"
     wordLine += " "+char+" |"

print(border)
print(wordLine)
print(border)

#exercises 3.2

for x in range(1, 41):
     if x != 13:
         if x % 5 !=0 and x % 7 != 0:
             print(x,' is not important')
         else:
             if x % 5 == 0 and x % 7 == 0:
                 print(x,' is divided by 5 and 7')
             elif x % 5 == 0:
                 print(x,' is divided by 5')
             else:
                 print(x,' is divided by 7')    

#exercises 3.3

n = 2022
x = math.pi
rounded_x = round(x, 5)
word = "Python"
polish = "książka"

outfile = open('vars.txt', 'w', encoding='utf-8')

outfile.write(str(n))
outfile.write("\n")
outfile.write(str(rounded_x))
outfile.write("\n")
outfile.write(word)
outfile.write("\n")
outfile.write(polish)
outfile.write("\n")

outfile.close()

infile = open('vars.txt', 'r', encoding='utf-8')
S = infile.read()
print(S)
infile.close()