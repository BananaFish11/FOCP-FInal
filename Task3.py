from random import choice
def inspect_mail(address,zone="pop.ac.uk"):
  ''' looks at the area of a mail ''' #docstring
  if "@" in address: 
    check_mail=address.split("@")
    if check_mail[1]==zone:
      return True
    else:
      return False
print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.")
system=["Asuna","SicK","Subroza","Zombs","Dapr","Shaz"]# random names for insteraction between user
exp=["Hmmm", "Oh, yes, I see","Tell me more","See i, Yes","K?","Roza?"]
end=["bye","finish","altf4","exit"]
mail=input("Please enter your Poppleton email address:")
chance=[1,1,1,1,1,1,1,1,1,0] #disconnects the server by 10%
gain=inspect_mail(mail)
if gain:
  get=mail.split("@")
  name=get[0]
  print(f"Hi {name}! Thank you, and Welcome to PopChat!\nMy name is {choice(system)}, and it will be my pleasure to help you.")
  while True:
    type=input("--->").lower()
    if choice(chance)==0:
      print("**NETWORK ERROR**") 
      print(f"Thank You {name},for using PopChat. See you again soon!") #fstring
      break
    if type in end:
        print(f"Thank You {name},for using PopChat. See you again soon!") #fstring for formating
        break
    dic={'library':['The library is closed today.','Library is currently open','The library opens at sharp 9 am'],#key and value paires.
      'wifi':['WiFi is excellent across the campus.','WiFi is currently unaviliable','WiFi is open but not accessible'],
      "deadline":['Your deadline has been extended by two working days.','Your deadline for submission has already passed'],
      'hospital':['The Hospital is closed today','The Hospital is currently open','The Hospital remains closed today'], 
      'pub':['The Pub is closed today','the Pub is open today','The Pub has moved to a new place'],
      'gamezone':['The gamezone is currently open for booking','The gamezone is closed due to some tech problem','Tha gamezone is closed'] }

    try: #cheaks for error.
      print(choice(dic[type]))
    except: #error handling.
      print(choice(exp))
else:
  print("Invalid mail")