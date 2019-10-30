# declare variables
name = "Stan"
age = 20
numbers = [12, 4, 56, 17, 8, 99]
alphabet = {"A" : "Apple", "B" : "Boy", "C" : "Cow", "D" : 'Dog', "E" : "Elephant", "F" : "Fish", "G" : "Ghost",
"H" : "Horse", "I" : "Icecream", "J" : "Jack", "K" : "Kangaroo", "L" : "Lamb", "M" : "Moon", "N" : "Nine", 
"O" : "Owl", "P" : "Pig", "Q" : "Queen", "R" : "Ruler", "S" : "Schoolbag", "T" : "Train", "U" : "Umbrella",
"V" : "Violet", "W" : "Wind", "X" : "Xylophone", "Y" : "Yo-yo", "Z" : "Zebra"}

#print hello world
print("Hello World\n")

#print name and age
print("My name is {}.".format(name))
print("I am {}+ years of age. Young, right? 😃\n".format(age))

#print calculations
print("The maximum number in this list: {} is {}.".format(numbers, max(numbers)))
print("The mean: {} is {}.\n".format(numbers, sum(numbers) / len(numbers)))

#print alphabets
for i in alphabet:
	print("{} for {}".format(i, alphabet[i]))


