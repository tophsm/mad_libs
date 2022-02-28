#Project 1
#Learning String Concatenation to play "madlibs"
#first fill in: "Subscribe to _____"
#youtuber = "" #youtuber will fill in the blank

#ways to print statement with value (youtuber)
#print("Subscribe to " + youtuber)
#print("Subscribe to {}".format(youtuber))
#print(f"Subscribe to {youtuber}")

#My Own Madlib
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
emotion = input("Enter an emotion ending in '-ly': ")
noun3 = input("Enter a noun: ")

madlib = "Row, row, row your " + noun1 + " gently down the " + noun2 + ". " + emotion + " " + emotion + "\
 " + emotion + " " + emotion + ". Life is but a " + noun3 + "."

print(madlib)
