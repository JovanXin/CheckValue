'''
This function prompts user to enter either a valid string or a number. Takes 2 parameters, prompt and type (either string/str or num)
'''

def checkvalue(prompt,data_type): #ensures user types a str or int

  data_type = data_type.lower()

  while True:
    value = input(prompt)

    try:
      value = int(value) #tries to convert "value" to a integer
      if "num" in data_type or "int" in data_type:
        return value
    except ValueError:
      if "str" in data_type:
        return value
