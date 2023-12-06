
import  random
gam = True
# def arch (a):
#     if plist[a] == 1:
#         print("apetqdit da waaget)")
#
#     elif plist[a]==0:
#         print("gilocavt +1 qula")
#     else:
#         print("error")
# def dawyeba ():
#
#     print("gsurt tavidan dawyeba? ")
#     a = str(input("ki AN ara"))
#     if a == "ki":
#         return
#     else:
#         print("ok")
#
randomm = random.randint(0,1)
wail =int(0)
print("Welcome  today we will play this game")
print("The rules are as follows:You have to choose the height and width of the board there are 50 drawers but there is a chance of an explosion, as there may be a bomb in the drawer. ")
print("Your main goal is not to explode and take the maximum score (+1 point per tray)")
print("0 choose forbidden")
qula = int(0)
cageba = int(0)
b = int(0)
c = int(0)
plist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #1
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #2
list3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #3
list4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]#4
list5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]#5
for i in range (0,3):
    randomm = random.randint(0, 1)
    plist[randomm]=1
    list2[randomm]=1
    list3[randomm]=1
    list4[randomm]=1
    list5[randomm]=1
simagle = 0
sigane = 0

while gam==True:

    simagle = int(input(" Choose height "))
    sigane = int(input(" Select width "))
    if simagle == 0:
        print("Read the rules ")
    elif sigane == 0:
        print("Read the rules ")
    elif simagle and sigane == 0:
        print("Read the rules ")
    elif simagle == 1:
        if plist[sigane] == 1:
            print("You lost")
            qula = 0
            print("do you Want to continue playing?")
            kiara = str(input("yes or no"))
            if kiara == "yes":
                print("ok")
            elif kiara == "no":

                break
            else:
                print("error")
                break

        elif plist[sigane]==0:
             print("+1")
             qula += 1
             print("do you Want to continue playing?")
             f = str(input("yes or no"))
             if f == "no":
                 break

        else:
             print("error")
    elif simagle == 2:
        if list2[sigane] == 1:
            print("You lost")
            qula = 0
            print("do you Want to continue playing?")
            kiara = str(input("yes or no"))
            if kiara == "yes":
                print("ok")
            elif kiara == "no":

                break
            else:
                print("error")
                break

        elif plist[sigane] == 0:
            print("+1")
            qula += 1
            print("do you Want to continue playing?")
            f = str(input("yes or no"))
            if f == "no":
                break

        else:
            print("error")
    elif simagle == 3:
        if list3[sigane] == 1:
            print("You lost")
            qula = 0
            print("do you Want to continue playing?")
            kiara = str(input("yes or no"))
            if kiara == "yes":
                print("ok")
            elif kiara == "no":

                break
            else:
                print("error")
                break

        elif plist[sigane] == 0:
            print("+1")
            qula += 1
            print("do you Want to continue playing?")
            f = str(input("yes or no"))
            if f == "no":
                break
        else:
            print("error")
    elif simagle == 4:
        if list4[sigane] == 1:
            print("You lost")
            qula = 0
            print("do you Want to continue playing?")
            kiara = str(input("yes or no"))
            if kiara == "yes":
                print("ok")
            elif kiara == "no":

                break
            else:
                print("error")
                break

        elif plist[sigane] == 0:
            print("+1")
            qula += 1
            print("do you Want to continue playing?")
            f = str(input("yes or no"))
            if f == "no":
                break
        else:
            print("error")
    elif simagle == 5:
        if list5[sigane] == 1:
            print("You lost")

            print("do you Want to continue playing?")
            kiara = str(input("yes or no"))
            if kiara == "yes":
                print("ok")
            elif kiara == "no":

                break
            else:
                print("error")
                break

        elif plist[sigane] == 0:
            print("+1")
            qula += 1
            print("do you Want to continue playing?")
            f = str(input("yes or no"))
            if f == "no":
                break
        else:
            print("error")
print("you have " , qula ,"points")

# arch(player)

#     print("gsurt tavidan dawyeba? ")
#     a = str(input("ki AN ara"))
#     if a == "ki":
#         gam = True
#     else:
#         print("ok")
# blomde ver miviyvan
