# this shows the final answers
msg_A = "Most likely."
msg_B = 'It is certain that this will happen.”'
msg_C = """Concentrate and ask again."""
msg_D ="I doubt this will happen."
msg_E = "A yes in every universe... except ours."
msg_F = "I believe it will occur."
msg_G = "All the signs point to no."
msg_H = "The spirits say yes."

# this shows the different color options
set_a = ['orange', 'yellow', 'purple'] #even colors in group 2
set_b = ['black'] #odd colors in group 2
set_c = ['red', 'green', 'blue', 'white'] #group 1
set_d = ['black', 'orange', 'yellow', 'purple'] #group 2
set_e = ['blue'] #even colors in group 1
set_f = ['red', 'green', 'white'] #odd colors in group 1

# this is the start of the fortune teller
def start():
    print ("Your fortune awaits you; would you like me to reveal it?")
    ans = input().lower()
    yes = ('yes','y')
    no = ('no', 'n')

    if ans in yes:
        print ("A wise choice, let's begin")
   
    elif ans in no:
        print ("A wise choice, until next time my friend.")
        exit()

    else: 
        print ("Yes or No, my child?")
        start()

start()

# this is the first phase of the teller, where the instructions are given
def game_phase_one ():
    global answer_one    
    #print (answer)
    print ("""Say your question out loud, then give me any number from 1 through 8 and the crystal ball will swirl and reveal your next set of choices.""")
    answer_one = input().lower()
    acceptable = ["1", "2", "3", "4", "5", "6", "7", "8"]

    if answer_one in acceptable:
        print ("""Excellent! The ball has revealed more choices...""" + str(answer_one) + """ it is... Now pick a color below and type it in, my child.""")
       
    else:
        print ("Hmmm... Lets try again.")
        game_phase_one()

game_phase_one ()

# this is the second phase of the teller where the second answer is chosen
def game_phase_two():
    global answer_two

    answer = int(answer_one) % 2
    #print (answer)

    if answer > 0:  #odd
        print (str(set_c) )
        answer_two = str(input().lower())

    else: #even
        print (str(set_d) )
        answer_two = str(input().lower())

game_phase_two()
# this is the third phase of the teller where it prompts the user to pick one last choice
def game_phase_three():
    global answer_three
    
    if answer_two in set_e:
        print ("The ball requests for you to pick one more choice to receive your fortune!" + str(set_c))
        answer_three = str(input().lower())
    
    elif answer_two in set_f:
        print ("The ball requests for you to pick one more choice to receive your fortune!" + str(set_d))
        answer_three = str(input().lower())
    elif answer_two in set_a:
        print ("The ball requests for you to pick one more choice to receive your fortune!" + str(set_d))
        answer_three = str(input().lower())
    elif answer_two in set_b:
        print ("The ball requests for you to pick one more choice to receive your fortune!" + str(set_c))
        answer_three = str(input().lower())

    else: 
        print ("Please pick a valid choice, do not waste my time.")
        game_phase_two()

game_phase_three ()

# the final phase where the answer is revealed
def game_phase_four ():
    if answer_three == "red":
        print (msg_A)
    if answer_three == "purple": 
        print (msg_F)
    if answer_three == "blue": 
        print (msg_E)
    if answer_three == "orange": 
        print (msg_B)
    if answer_three == "yellow": 
        print (msg_C)
    if answer_three == "green": 
        print (msg_D)
    if answer_three == "black": 
        print (msg_G)
    if answer_three == "white": 
        print (msg_H)
   


game_phase_four()
