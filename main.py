#prompt user to enter something to be reversed

print("Enter a line of text:")
text = input()
text = text[::-1]
print(text)

#prompt user to enter a line of text to be converted to Bianry
print("Enter a line of text:")
binText = input()
convert = ''.join(format(ord(i), '08b') for i in binText)
print("The converted string is now: " + convert)

