phone = input(" phone numbers: ")
numbers = {
  "1" : "one",
  "2" : "Two",
  "3" : " Three",
  "4" : "Four",
  "5" : "Five",
  "6" : "Six", "7": "Seven" , "8" : "Eight",
  "9" : " nine"
}
output = ""
for ch in phone:
  output += numbers.get(ch, "!") + ""
print(output)  