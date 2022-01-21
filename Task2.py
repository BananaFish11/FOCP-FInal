print("Swallow Speed Analysis: Version 1.0")
tally=0
echo=[]
while True:
  check=input("Enter the Next Reading:")
  if tally==0 and check=="": # it cheaks if the value is zero or not.
    print("No readings entered. Nothing to do.")
    break
  elif check=="" and tally>=1 : # cheaks if the value is more than 1.
    max_speed=max(echo)
    avg_speed=sum(echo)/len(echo) #divides by the length of echo to caluculate its average speed
    min_speed=min(echo)
    print("Results Summary")
    
    print(tally,"Reading Analysed")
    print(f"Max speed: {max_speed:.2f} MPH, {max_speed*1.61:.2f} KPH.") 
    print(f"Min speed: {min_speed:.2f} MPH, {min_speed*1.61:.2f} KPH.") 
    print(f"Avg speed: {avg_speed:.2f} MPH, {avg_speed*1.61:.2f} KPH.") 
    break
  else:
    read=check[1:]
    tally = tally + 1
    print("Reading saved")
    if check[0]=="E": # cheaks if the first letter is U or E
      adv=float(read)/1.61 
      echo.append(adv)
    elif check[0]=="U":
      adv=float(read)
      echo.append(adv)
    else:
      print("Incorrect Reading!!")