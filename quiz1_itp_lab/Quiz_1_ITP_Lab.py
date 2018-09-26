#Isinya Fridge (names)
fridge = {
    "top" : [],
    "mid" : [],
    "bottom" : [],
}

#max value in fridge
value = {
    "top" : 15,
    "mid" : 15,
    "bottom" : 15,
}

#how much space it needs
isifridge = {
    "top" : [],
    "mid" : [],
    "bottom" : [],
}


#mulai
def main():

    global value


    #insert what you want to do
    number = input("watchu wanna do to this fridge\n1.Insert food\n2.Take out food\n3.view\n4.stop\nChoose a number((1-4): ")

    while not number.isdigit():
        number = input("please input a whole numbers: ")
    number = int(number)

    if number < 1 or number > 4:
        print("PLEASE TRY AGAIN")
        main()


    while number != 4:


        #Inserting food into fridge
        if number == 1:
            where = input("which row(top/mid/bottom): ")

            if where != "top" and where != "mid" and where != "bottom":
                print("PLEASE CHOOSE A CORRECT OPERATION AND TRY AGAIN")
                main()

            food = input("insert food here: ")
            size = input("size of item: ")

            while not size.isdigit():
                size = input("please input size of item (whole numbers): ")
            size = int(size)

            if  size > value[where]:
                print("NOT ENOUGH STORAGE, TRY AGAIN")
                main()

            value[where] = value[where] - size
            fridge[where].append(food)
            isifridge[where].append(size)


            print("space:",value["top"],"top:", fridge["top"])
            print("space:", value["mid"], "top:", fridge["mid"])
            print("space:", value["bottom"], "top:", fridge["bottom"])


            #looping back to main
            redo = input("access fridge? (yes/no): ")

            if redo == "yes":
                main()

            elif redo == "no":
                quit()


            else:
                while not redo == "yes" or "no":
                    redo = input("please insert yes/no:  ")

                    if redo == "yes":
                        main()

                    elif redo == "no":
                        quit()

            second()


        #Taking out food from fridge
        if number == 2:

            where = input("access which row (top/mid/bottom)? :")

            if where != "top" and where != "mid" and where != "bottom":
                print("please try again and choose a correct option")
                main()

            print("space:", value[where], "top:", fridge[where])
            chose = input("choose food position(stating from 1):")

            while not chose.isdigit():
                chose = input("please insert item number correctly (whole numbers): ")
            chose = int(chose)

            if chose != isifridge[where]:
                print("item doesnt exist, try again")
                main()

            value[where] = value[where] + isifridge[where][chose - 1]
            del fridge[where][chose - 1]

            print("space:", value["top"], "top:", fridge["top"])
            print("space:", value["mid"], "top:", fridge["mid"])
            print("space:", value["bottom"], "top:", fridge["bottom"])

            value[where] = value[where] + isifridge[where][chose - 1]


            #looping back to main
            redo = input("access fridge? (yes/no): ")

            if redo == "yes":
                main()

            elif redo == "no":
                quit()


            else:
                while not redo == "yes" or "no":
                    redo = input("please insert yes/no:  ")

                    if redo == "yes":
                        main()

                    elif redo == "no":
                        quit()

            second()


        #viewing whats inside the fridge
        if number == 3:

            print("space:", value["top"], "top:", fridge["top"])
            print("space:", value["mid"], "top:", fridge["mid"])
            print("space:", value["bottom"], "top:", fridge["bottom"])


            #looping back to main
            redo = input("access fridge? (yes/no): ")


            if redo == "yes":
                main()

            elif redo == "no":
                quit()


            else:
                while not redo == "yes" or "no":
                    redo = input("please insert yes/no:  ")

                    if redo == "yes":
                        main()

                    elif redo == "no":
                        quit()

            second()


        #quitting
        if number == 4:
            quit()


main ()