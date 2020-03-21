
'''
This function prompts user to enter either a valid string or a number. If choice is left blank, user must enter a string. If choice is entered in (common choice 0 or 1), user must enter a integer. 

'''

def checkvalue(*choice): #ensures user types a str or int
  while True: 
    value = input("enter a value:")
    try:
      value = int(value) #tries to convert "value" to a integer
      if choice: 
        return value
      print("not a string, try again:") #we don't need else here because returning the value breaks the loop anways
    except ValueError:
      if choice: 
        print("not a number, try again:")
      else:
        return value
