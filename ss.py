#! usr/bin/python


#libaries
import random as rn
import sys

#there is 3 possibilities in this game
first = ["p","s"]
second = ["p","k"]
third = ["s","k"]



#first we should select our weapon in game


#in this part client should choose her/his weapon
def selction_player() :
    user_selection = str(input("select your weapon : s or p or k\n"))
    users = user_selection
    player = { "user": users }
    return(player["user"])

#in this part coputer should choose randomly a weapon

def selction_cpu():
    options = ["s","p","k"]
    cpu_selection = rn.choices (options)
    cpus = str(cpu_selection[0]) 
    player = {"cpu": cpus}
    return(player["cpu"])

user = selction_player()
cpu = selction_cpu()

#in this part game has started
def start_game():

    #if cpu and user weapon was same ,game will finished
    if user == cpu :
        print("resualt of this match is draw")
        print(cpu , user)
        sys.exit("this match has finished")
        
    

    #first possibility
    if user in first and cpu in first :
        if user == "s" :
            print("you win!")
        else :
            cpu == 's'
            print("cpu won!")


    # second possibility
    if user in second and cpu in second :
        if user == "k" :
            print("you win!")
        else :
            cpu == 'k'
            print("cpu won!")

    # third possibility
    if user in third and cpu in third :
        if user == "s" :
            print("you win!")
        else :
            cpu == 's'
            print("cpu won!")



start_game()
print(cpu , user)




