print("Stop! Who would cross the Bridge of Death /n Must answer me these questions three, 'ere the other side he see.")
name = input("What is your name:").lower()
if name=="arthur":
    print("you may pass")
else:
    seek = input("What is your quest ?")
    if "grail" in seek: # checking if there is grail in seek or not.
        color = input("what is your favourite color?").lower()
        if name[0]==color[0]: # comparing first letter of name with first letter of color.
            print("You may pass")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek the Grail may pass.")
        