def sps():

    global point_sps
    global result_sps
    
    print(" ------------------------", "\n", "| STONE PAPER SCISSORS |", "\n", "------------------------")
    print(" -Enter 0 for Stone.", "\n", "-Enter 1 for Paper.", "\n", "-Enter 2 for Scissors.")
    x = "Computer Won!"
    y = "You Won!"
    import random as rn
    print("The more points of game you play , more will be your score")
    ans = "y"
    while ans.lower() == "y":
        point_sps = int(input("Enter for how many points you have to play : "))
        me = 0
        comp = 0
        while me < point_sps and comp < point_sps:

            user = int(input("Enter : "))
            cm = rn.randrange(0, 3)

            if user == cm:
                print("DRAW!!")
                print("You :", me, "Computer :", comp)

            elif user == 0:
                if cm == 1:
                    print("Stone vs Paper")
                    print(x)
                    comp += 1
                    print("You :", me, "Computer :", comp)
                else:
                    print("Stone Vs Scissors")
                    print(y)
                    me += 1
                    print("You :", me, "Computer :", comp)

            elif user == 1:
                if cm == 2:
                    print("Paper vs Scissors")
                    print(x)
                    comp += 1
                    print("You :", me, "Computer :", comp)
                else:
                    print("Paper Vs Stone")
                    print(y)
                    me += 1
                    print("You :", me, "Computer :", comp)

            elif user == 2:
                if cm == 0:
                    print("Scissors Vs Stone")
                    print(x)
                    comp += 1
                    print("You :", me, "Computer :", comp)
                else:
                    print("Scissors Vs Paper")
                    print(y)
                    me += 1
                    print("You :", me, "Computer :", comp)

            else:
                print("You Entered Something Wrong.")

            if me == point_sps:
                print("You have won this game!")
                result_sps = 1
                lb_sps()

            elif comp == point_sps:
                print("You Lost!")
                print("Computer have won this game!")
                result_sps = 0

        print("Press Y to play again , press any other letter to leave the game")
        ans=input("Your Response: ")


    #Leaderboard Structure

    scoredata = "SELECT DISTINCT PLAYER , SCORE FROM SPS"
    cur.execute(scoredata)

    list_sgame = []
    for i in cur:
        list_sgame.append(i)

    cur.execute(scoredata)
    list_score = []
    for i in cur:
        list_score.append(i[1])

    list_score = list(dict.fromkeys(list_score))
    list_score.sort(reverse=True)

    ######################################

    def stringfix():
        for i in list_score:
            for j in list_sgame:
                if i == j[1]:
                    spaces = 4
                    ye = (j[0] + (" " * spaces) + "|     " + str(j[1]))

                    if len(ye) == len(stringlength):

                        print(ye)
                    else:
                        spaces+=1




    select = "SELECT DISTINCT PLAYER FROM SPS"
    cur.execute(select)

    namelist = []
    for i in cur:
        namelist.append(i[0])

    namelistsps = sorted(namelist,key=len,reverse=True)

    print()
    print("------------------------------------------------------------------------------------------")
    print("|                                      LEADERBOARD                                       |")
    print("------------------------------------------------------------------------------------------")
    print()

    try:
        stringlength = len(namelistsps[0])+4+1+4+4


        spaces = 4
        while True:

            playerfix = "Player" + (" " * spaces) + "|   Scores"

            if len(playerfix) == (stringlength+2):

                print(playerfix)
                break
            else:

                spaces += 1


        for i in list_score:

            for j in list_sgame:

                if i == j[1]:
                    spaces = 4
                    while True:


                        ye = (j[0] + (" " * spaces) + "|    " + str(j[1]))

                        if len(ye) == stringlength:

                            print(ye)
                            break

                        else:
                            spaces += 1

    except:
        print("NO HIGHSCORES YET")



def lb_sps():

    if result_sps==1:
        score = str(point_sps*100)



    insertion="INSERT INTO SPS VALUES(\""+userid+"\",\""+score+"\")"
    cur.execute(insertion)
    db.commit()

def wgame():


    import random as rn
    from time import sleep as s

    global lenword
    global result_wgame
    ans = "Y"
    while ans == "y" or ans == "Y":

        animals = ["alligator", "ant", "bear", "bee", "bird", "camel", "cat",
                   "cheetah", "chicken", "cow", "crocodile",
                   "deer", "rat", "scorpian", "seal", "shark", "sheep",
                   "snail", "snake", "spider", "squirrel", "tiger", "turtle",
                   "wolf", "zebra", "dog", "dolphin", "duck", "eagle", "elephant",
                   "fish", "fly", "fox", "frog", "giraffe", "goat", "goldfish",
                   "hamster", "horse", "kangaroo", "kitten",
                   "lion", "lobster", "monkey", "octopus", "owl", "panda", "pig",
                   "puppy", "rabbit"]

        colours = ["red", "pink", "orange", "yellow", "purple", "green"
            , "blue", "brown", "white", "grey", "black", "gold", "silver",
                   "bronze", "violet", "indigo", "magenta", "cyan", "teal",
                   "turquoise", "fuchsia", "crimson", "coral"]

        fruits = ["apple", "apricot", "avocado", "banana", "blueberry", "cherry",
                  "cucumber", "clementine", "cranberry", "date", "fig", "grape",
                  "melon", "kiwi", "lemon", "pepper", "pumpkin", "mandarin", "tomato", "mango"
            , "mulberry", "nectarine", "olive", "orange", "peach", "pear", "pineapple",
                  "plum", "prune", "raspberry", "rhubarb", "tangerine"]

        musical_instruments = ["accordian", "bagpipes", "bassoon",
                               "cello", "clarinet", "cornet", "cymbal", "drums", "flute",
                                "gong", "guitar", "harmonica", "harp",
                                "oboe", "organ", "piano", "recorder",
                               "saxophone", "tambourine", "timpani",
                               "triangle", "trombone", "trumpet", "ukulele", "viola",
                               "violin", "xylophone"]

        sports = [ "archery", "athletics", "badminton","baseball", "swimming", "boxing","canoe", "diving",
                   "fencing", "football", "golf", "handball","hockey", "judo", "karate", "cycling", "rowing",
                   "rugby","sailing", "shooting", "softball", "surfing","tennis", "wrestling", "skiing",
                  "bobsleigh", "skating"]

        vegetables = ["asparagus", "bean", "beet","broccoli", "cabbage", "carrot", "celery", "corn", "eggplant",
                      "ginger", "kale", "leek", "lettuce", "mushroom", "onion", "parsnip", "pea", "potato",
                      "radish", "shallot", "spinach", "squash", "turnip"]

        print("""Themes:
1.Animals
2.Colours
3.Fruits
4.musical Instrument
5.Sports
6.Vegetables\n""")

        themes = [animals, colours, fruits, musical_instruments, sports, vegetables]

        n = int(input("Select theme: "))
        theme = themes[n - 1]
        word = rn.choice(theme)
        lenword = len(word)
        type(lenword)
        strp = []

        for i in range(len(word)):
            strp.append("*")

        def string(x):
            string = ""
            for i in range(len(x)):
                string += x[i]
            return (string)

        chances = 0
        print("The bigger the word is, the more points you will get ")
        print("Entering The letter u already guessed or tried to guess will cost one chance\nBEWARE !! ")

        print("The Word Is Ready !")

        s(0.5)

        print("You Will Get", len(word) + 2, " Chances\n")
        s(0.5)

        print("To Be Guessed: ", string(strp))
        s(0.5)

        while chances <= len(word) + 1:

            if string(strp) == word:
                print("You guessed it right ")
                print("Wanna Play Again ?")
                ans = input("Y or N ? :")

                lb_wgame()
                break

            s(0.5)
            guess = input("Try to Guess: ")

            if len(guess) == len(word):
                if guess == word:
                    print("You guessed it right")
                    print("\n\nWanna Play Again ?")
                    ans = input("Y or N ? :")

                    lb_wgame()
                    break
                else:
                    print("Nahh\n")

            elif len(word) != len(guess) and len(guess) != 1:
                print("You entered something wrong")

            elif len(guess) == 1:
                indicies = []

                for a in range(len(word)):
                    if guess == word[a]:
                        indicies.append(a)

                if indicies != []:
                    print("You entered", guess)
                    print(guess, "has occured", word.count(guess), "times\n")

                    for i in range(len(word)):
                        for j in indicies:
                            if i == j:
                                strp[i] = guess
                else:
                    print(guess, "Doesn't come in word\n")

            s(1)
            print("To be guessed :", string(strp))
            chances += 1
            print("Chances left", len(word) + 2 - chances)

        if string(strp) != word and guess != word:
            print("You Lost !!")

            s(0.5)
            print("The Word Was :", word)


            print("\n\nWanna Play Again ?")
            ans = input("Y or N ? :")


    #Leaderboard Structure

    scoredata = "SELECT DISTINCT PLAYER , SCORE FROM WGAME"
    cur.execute(scoredata)

    list_wgame = []
    for i in cur:
        list_wgame.append(i)

    cur.execute(scoredata)
    list_score = []
    for i in cur:
        list_score.append(i[1])

    list_score = list(dict.fromkeys(list_score))
    list_score.sort(reverse=True)

    select = "SELECT DISTINCT PLAYER FROM WGAME"
    cur.execute(select)

    namelist = []
    for i in cur:
        namelist.append(i[0])


    namelistwgame = sorted(namelist, key=len, reverse=True)

    print()
    print("------------------------------------------------------------------------------------------")
    print("|                                      LEADERBOARD                                       |")
    print("------------------------------------------------------------------------------------------")
    print()

    try:
        stringlength = len(namelistwgame[0]) + 4 + 1 + 4 + 4


        spaces = 4
        while True:

            playerfix = "Player" + (" " * spaces) + "|   Scores"

            if len(playerfix) == (stringlength + 2):

                print(playerfix)
                break
            else:

                spaces += 1

        for i in list_score:

            for j in list_wgame:

                if i == j[1]:
                    spaces = 4
                    while True:

                        ye = (j[0] + (" " * spaces) + "|    " + str(j[1]))

                        if len(ye) == stringlength:

                            print(ye)
                            break

                        else:
                            spaces += 1

    except:
        print("NO HIGHSCORES YET")




def lb_wgame():

    score = str(lenword*100)


    insertion="INSERT INTO WGAME VALUES(\""+userid+"\","+score+")"
    cur.execute(insertion)
    db.commit()





def ngame():

    global result_ngame
    print("------------------------")
    print("| NUMBER GUESSING GAME |")
    print("------------------------")

    l1 = int(input("Enter the lower limit of range : "))

    l2 = int(input("Enter the upper limit of range : "))

    import random as rn
    ans="c"
    while ans == "c" or ans == "C":
        lu = rn.randint(l1, l2)
        b = int(input("Guess a number : "))

        if b == lu:
            print("You Won!")
            print("\n", "Real Number : ", lu, "\n", "Guessed Number : ", b)
            result_ngame=1
            lb_ngame()
            ans = input("Enter C to continue or Enter S to stop : ")

        elif (b >= l1 and b <= l2) and b != lu:
            print("Wrong Guess!")
            print("\n", "Real Number : ", lu, "\n", "Guessed Number : ", b)
            ans = input("Enter C to continue or Enter S to stop : ")

        elif b < l1 or b > l2:
            print("Entered number is out of range.")
            ans = input("Enter C to continue or Enter S to stop : ")

    #Leaderboard Structure

    scoredata = "SELECT DISTINCT PLAYER , SCORE FROM NGAME"
    cur.execute(scoredata)

    list_ngame = []
    for i in cur:
        list_ngame.append(i)

    cur.execute(scoredata)
    list_score = []
    for i in cur:
        list_score.append(i[1])

    list_score = list(dict.fromkeys(list_score))
    list_score.sort(reverse=True)

    select = "SELECT DISTINCT PLAYER FROM NGAME"
    cur.execute(select)

    namelist = []
    for i in cur:
        namelist.append(i[0])

    namelistngame = sorted(namelist, key=len, reverse=True)




    print()
    print("------------------------------------------------------------------------------------------")
    print("|                                      LEADERBOARD                                       |")
    print("------------------------------------------------------------------------------------------")
    print()


    spaces = 4
    try:

        stringlength = len(namelistngame[0]) + 4 + 1 + 4 + 7
        while True:

            playerfix = "Player" + (" " * spaces) + "|   No. Of Wins"

            if len(playerfix) == (stringlength + 4):

                print(playerfix)
                break
            else:

                spaces += 1

        for i in list_score:

            for j in list_ngame:

                if i == j[1]:
                    spaces = 4
                    while True:

                        ye = (j[0] + (" " * spaces) + "|    " + str(j[1])+" wins")

                        if len(ye) == stringlength:

                            print(ye)
                            break

                        else:
                            spaces += 1

    except:
        print("NO HIGHSCORES YET")


def lb_ngame():

    if result_ngame == 1:
        score = str(result_ngame)



    cur.execute("SELECT PLAYER FROM NGAME")
    for i in cur:
        if userid == i[0]:
            cur.execute("SELECT SCORE FROM NGAME WHERE PLAYER=\""+userid+"\"")
            for j in cur:

                sscore = int(j[0])


            score_update=sscore+1

            updation = "UPDATE NGAME SET SCORE="+str(score_update)+" WHERE PLAYER=\""+userid+"\""

            cur.execute(updation)

            db.commit()

            break

    else:
        insertion = "INSERT INTO NGAME VALUES(\"" + userid + "\","+str(score)+")"

        cur.execute(insertion)
        db.commit()



def master():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("| WELCOME TO THE GAMING CENTRE |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("""Games:
1.NUMBER GUESSING GAME
2.STONE PAPER SCISSORS
3.WORD GUESSING GAME
# Press any character to quit.""")
    gchoice = input("Enter the number corresponding the game you want to play : ")
    if gchoice == '1':
        ngame()
        first = input("\n\nEnter Y if you want to play any other game or enter any other character to quit : ")
        if first == 'Y' or first == 'y':
            master()
        else:
            end()
    elif gchoice == '2':
        sps()
        sec = input("\n\nEnter Y if you want to play any other game or enter any other character to quit : ")
        if sec == 'Y' or sec == 'y':
            master()
        else:
            end()
    elif gchoice == '3':
        wgame()
        third = input("\n\nEnter Y if you want to play any other game or enter any other character to quit : ")
        if third == 'Y' or third == 'y':
            master()
        else:
            end()
    else:
        end()


    return


def end():
    print("Thanks For Playing!\n")
    print("Hope You Enjoyed It.\n")
    print('''Made By 
Devank Sachdeva XII-A
Advit Khera XII-B''')






import mysql.connector

x=input("Enter The Password Of Your Database: ")
dr=mysql.connector.connect(
    host="localhost",
    user="root",
    password=x)
cr=dr.cursor()
cr.execute('CREATE DATABASE IF NOT EXISTS Project_GameCenter')
db=mysql.connector.connect(host="localhost",user="root",password="devank2003",db="Project_GameCenter")
cur=db.cursor(buffered=True)

cur.execute("CREATE TABLE IF NOT EXISTS DATA(Userid VARCHAR(50),Password VARCHAR(50))")
cur.execute("CREATE TABLE IF NOT EXISTS NGAME(Player VARCHAR(50),Score INT)")
cur.execute("CREATE TABLE IF NOT EXISTS SPS(Player VARCHAR(50),Score INT)")
cur.execute("CREATE TABLE IF NOT EXISTS WGAME(Player VARCHAR(50),Score INT)")
db.commit()

print("Press L for existing user or Press N for new user")

ye=input("Your choice: ")

if ye.lower()=="n":
    userid = input('Enter User Id: ')
    password=input("Enter pass: ")
    str1="INSERT INTO DATA VALUES(\""+userid.lower()+"\",\""+password.lower()+"\")"
    cur.execute(str1)
    db.commit()
    master()




elif ye.lower() =="l":
    userid=input('Enter User Id: ')
    password=input("Enter pass: ")
    cred=(userid.lower(),password.lower())

    cur.execute("SELECT * FROM DATA")


    for i in cur:
        if cred==i:
            master()
            break

    else:
        print("Invalid Credentials")
        end()

else:
    print("You typed something wrong")
    print("Aborting")




