isDirty = True

while isDirty == True:
    washing = input("Continue washing cloths?: (yes/no)").lower()

    if washing == "yes":
        print("Washing cloths now....")
        continue
    else:
        print("Stopped washing cloths...")
        break    