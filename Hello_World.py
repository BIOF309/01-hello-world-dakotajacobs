## --- First Script in Python --- ##

# print Hello World
print ("Hello World")

## --- Extra Stuff --- ##

# Ask user about their Origin Story
Origins = input("Where did you grow up?")

# See if Origins overlap
if Origins == "Oregon":
    print ("Oh wow me too!")
    City = input("Which part of Oregon?")                 # Specific city in Oregon
    if "Corvallis" in City:
        print ("That's pretty neat")
    else:
        print (City + " who?")

# If they don't overlap, ask about their Origins
if Origins != "Oregon":
    print ("I didn't grow up in " + Origins)
    Honesty = input("Is it nice? Yes or No")              # A moment of honest reflection
    if "Yes" in Honesty:
        print ("Prove it")
    if "No" in Honesty:
        print ("Then why would I want to go")
