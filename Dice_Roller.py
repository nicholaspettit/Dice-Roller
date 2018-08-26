#Dice Roller
#Purpose of this program is to randomly simulate rolling two die

#Functions          #Purpose
#main               This is the main function for the program
#copyright_fun      This function calls all of the copyright information
#random_generator   This function does the random number generation needed for the dice roll

#Variables          #Type           #Purpose
#rand_1             int             Hold the value of the first random die
#rand_2             int             Hold the value of the second random die
#dice_roll          str             Holds the answer from the user on rolling the dice
#view_copyright     str             This variable allows the user to select if they want to view the copyright information

##################################################################################

import math
import random

#Start of program
def main ():

    #Welcome user to the dice roller program
    print("Welcome to the dice roller generator")

    #Call copyright function
    copyright_fun ()

    #As the user to roll the dice
    print("Ready to roll the dice?")
    print("\n")
    print("Enter Y for yes")
    print("Enter N for no")
    dice_roll = str(input("Enter selection:"))
    print("\n")    


    #Validation loop of the anser given for dice roll
    #Only accept a capital Y or N right now to move on
    while True:          
        
        if dice_roll == 'N' :

            return

        elif dice_roll == 'Y' :

            #Call the random number generator function
            random_generator ()

            return

        elif dice_roll !="N" and dice_roll !="Y":

            print("Ready to roll the dice?")
            print("\n")
            print("Enter Y for yes")
            print("Enter N for no")
            dice_roll = str(input("Enter selection:"))
            print("\n") 

            return

    return
 
#Copyright protection function
def copyright_fun ():
        print("Copyright (c) 2018, Nicholas R Pettit")
        print("nicholas.r.pettit@protonmail.com")
        print("All rights reserved.")
        print("\n")
        print("To view entire copyright information press Y for Yes or N for No.")
        print("Enter Y for yes")
        print("Enter N for no")
        view_copyright = str(input("Enter selection:"))
        print("\n")    


        #Validation loop of the anser given for view_copyright
        #Only accept a capital Y or N right now to move on
        while True:          
        
            if view_copyright == 'N' :
                return

            elif view_copyright == 'Y' :
                print("Redistribution and use in source and binary forms, with or without")
                print("modification, are permitted provided that the following conditions are met:")
                print("\n")
                print("1. Redistributions of source code must retain the above copyright notice, this")
                print("list of conditions and the following disclaimer.")
                print("2. Redistributions in binary form must reproduce the above copyright notice,")
                print("this list of conditions and the following disclaimer in the documentation")
                print("and/or other materials provided with the distribution.")
                print("3. Neither Nicholas R Pettit nor the names of its contributors may be used")
                print("to endorse or promote products derived from this software without specific ")
                print("prior written permission.")
                print("\n")
                print("THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ""AS IS"" AND")
                print("ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED")
                print("WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE")
                print("DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR")
                print("ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES")
                print("(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;")
                print("LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND")
                print("ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT")
                print("(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS")
                print("SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.")
                print("\n")
                print("The views and conclusions contained in the software and documentation are those")
                print("of the authors and should not be interpreted as representing official policies,")
                print("either expressed or implied, of the FreeBSD Project.")
                print("\n")
                print("\n")
                return

            elif view_copyright !="N" and view_copyright !="Y":
                print("Yes or No answer only: ")
                print("Enter Y for yes")
                print("Enter N for no")
                view_copyright = str(input("Enter selection:"))
                print("\n")

#This is the random number generator function
def random_generator ():

    #Variables for the answer
    #rand_1 is die 1, and rand_2 is die 2
    rand_1 = random.randint(1,6)
    rand_2 = random.randint(1,6)

    #Print the dice
    print("Your roll is: ")
    print("Die 1: ", rand_1)
    print("Die 2: ", rand_2)

    print("\n")

    #As the user to roll the dice again
    print("Ready to roll the dice again?")
    print("\n")
    print("Enter Y for yes")
    print("Enter N for no")
    dice_roll = str(input("Enter selection:"))
    print("\n")    


    #Validation loop of the anser given for dice roll
    #Only accept a capital Y or N right now to move on
    while True:          
        
        if dice_roll == 'N' :

            return

        elif dice_roll == 'Y' :

            #Call the random number generator function
            random_generator ()

            return

        elif dice_roll !="N" and dice_roll !="Y":

            print("Ready to roll the dice?")
            print("\n")
            print("Enter Y for yes")
            print("Enter N for no")
            dice_roll = str(input("Enter selection:"))
            print("\n") 

            return

    return

#This is where I call the main function to run the program
main ()
