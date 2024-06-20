import random
lowercase = "abcdefghijklmnopqrstwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTWXYZ"
numbers = "0987654321"
special_chars = "[]{}.,/"
main_string = ""

islowercase = False
isuppercase = False
isnumbers = False
isspecialchars = False
password_length = ""
password = ""

password_length = int(input("Enter the password length: "))

islowercase = bool(input("Allow lowercase?(True/False): "))
isuppercase = bool(input("Allow uppercase?(True/False): "))
isnumbers = bool(input("Allow numbers?(True/False): "))
isspecialchars = bool(input("Allow special chars?(True/False): "))

if islowercase == True:
  main_string += lowercase
  if isuppercase == True: 
    main_string+=uppercase
    if isnumbers == True: 
      main_string+= numbers
      if isspecialchars == True:
        main_string += special_chars



for i in range(password_length):
  password += random.choice(main_string)

print(password)


