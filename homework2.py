from prettytable import PrettyTable

#exercise 2.1
x = int(37890789078900009876678907898988888800098777789000987)

print(str(x).count('0'))

#exercise 2.2

# Explain the results. 
# obie wartości muszą być false or true
# x = 5 
# x == 5 and 3 + 8   # 11 - jeśli pierwsza true to zwraca drugą
# x == 4 and 3 + 8   # False -> bo, pierwsza wartość jest false,
# 3 + 8 and x == 5   # True -> jeśli pierwsza true to zwraca drugą
# 3 + 8 and x == 4   # False -> bo, druga wartość jest false


#exercise 2.3

a = range(1, 2021, 2)
print(sum(i*i for i in a))

#exercise 2.4

myName = "Maja"
for char in myName:
    print(ord(char))


#pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4)]
#for (n, name, symbol, weight) in pt:
    # print(tabulate([[n, name, symbol, weight] in pt], headers=['No.', 'Name (en)', 'Symbol', 'Weight (u)'], tablefmt='pretty'))

table = PrettyTable()
table.field_names = ["No.", "Name (en)", "Symbol", "Weight (u)"]
table.align["No."] = "r"
table.align["Name (en)"] = "l"
table.align["Symbol"] = "c"
table.align["Weight (u)"] = "r"
table._min_width = {"No." : 3, "Name (en)" : 20, "Symbol" : 6, "Weight (u)" : 10}
table.add_rows(
    [
        [1,"Hydrogen","H",1],
        [2,"Helium","He",4],
        [3,"Lithium","Li",7],
        [4,"Berylium","Be",9],
        [5,"Boron","B",10],
        [6,"Carbon","C",12],
        [7,"Nitrogen","N",14],
        [8,"Oxygen","O",15],
        [9,"Fluorine","F",18],
        [10,"Neon","Ne",20]


    ]
)

print(table)


#exercise 2.5

S = "hey hi hello"
words = S.split()
noOfBlackChar = sum(len(word) for word in words)
print("Number of black characters in sentence: ", noOfBlackChar)
length = len(words)
print("Number of words in sentence: ", length)
longesWord = max(words, key=len)
print("Longest word in sentence: ", longesWord)
lexSort = sorted(words)
print("Lexicographic sort: ",lexSort)
lengthSort = sorted(words, key=len)
print("Sort by length of the words: ",lengthSort)

#excersise 2.6
# Find and explain the results.
t = (2, 4)
# print(t[2]) #wychodzi błąd bo w tabeli nie ma elementu o indeksie 2 (numeracja zaczyna się od 0)
#t.append(6) nie można dodać trzeciej warości do tuple
# a, b = t ; print(a,b) #podpisuje liczby literami


#exercises 2.79
R = dict([("I",1),("IV",4),("V",5),("IX",9),("X",10),("XL",40),("L",50),("XC",90),("C",100),("CD",400),("D",500),("CM",900),("M",1000)])
R2 = dict(I=1,IV=4,V=5,IX=9,X=10,XL=40,L=50,XC=90,C=100,CD=400,D=500,CM=900,M=1000)
print(R)
print(R2)