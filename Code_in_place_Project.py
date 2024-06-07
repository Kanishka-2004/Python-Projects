import random

def main():
    print("\nLet's play the game of Rock,Paper,Scissor")
    print("\nThe winning rules of the game are:\n"
    +"Rock vs Paper --> Paper wins\n"
    +"Rock vs Scissor --> Rock wins\n"
    +"Scissor vs Paper --> Scissor wins")

    Choices = ['Rock','Paper','Scissor']
    Computer_choice= Choices[random.randint(0,2)]

    User_Count=0
    Computer_Count=0

    for i in range(0,5):

        User_choice = input("\nRock,Paper,Scissor?: ")

        if User_choice==Computer_choice:
            print("Tie!!")
            

        elif User_choice=="Rock":
            if Computer_choice=="Paper":
                print("You lose! your opponent used paper")
                Computer_Count+=1
            else:
                print("You win yayyyy!! ><")
                User_Count+=1

        elif User_choice=="Paper":
            if Computer_choice=="Scissor":
                print("You lose! your opponent used Scissor")
                Computer_Count+=1
            else:
                print("You win yayyy!! ><")
                User_Count+=1

        elif User_choice=="Scissor":
            if Computer_choice=="Rock":
                print("You lose! your opponent used Rock")
                Computer_Count+=1
            else:
                print("You win yayyy!! ><")
                User_Count+=1    
        else:
            print("That's a invalid input. Provide an appropriate choice!")

    if User_Count > Computer_Count:
        print("\nYayyy You won all the five 5 round")
        print("Your points are: "+str(User_Count)+"  And the opponent points are: "+str(Computer_Count))
    elif User_Count==Computer_Count:
        print("\nOh you had a tie!")
        print("Your points are: "+str(User_Count)+"  And the opponent points are: "+str(Computer_Count))

    else:
        print("\nOops You lost!, Don't worry better luck next time")
        print("Your points are: "+str(User_Count)+"  And the opponent points are: "+str(Computer_Count))

        
        Computer_choice=Choices[random.randint(0,2)]   


    

if __name__ == "__main__":
    main()