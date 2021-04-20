import tkinter as tk
from tkinter import font as tkf
from functools import partial
from tkinter.messagebox import showinfo


####################################################################################
#
#                               PART 1: FUNCTIONS
#
#   1 - FUNCTION onclick_event => this event is triggered when user clicks a button
#        Function to find a button by its name
#        Function to set button's value (X or O)
#        Function to check game over
#   2 - FUNCTION getting_button_value => Returns button value/text (X or O)
#   3 - FUNCTION checking_game_over  => returns True or False
#   4 - FUNCTION reseting_game => clears all buttons text
#
####################################################################################


####################################################################################
        # PART 1.1: onclick_event (triggered when the user clicks a button)
####################################################################################

# Function receives the button's row and column as parameters
def onclick_event(row, col):
    global value
    # Variable button_name receives a string with the button's coordinates(button:0-0, button:0-1...)
    button_name = f'button_{row}_{col}'

    # Finding a button by its name
    clicked_button = window.nametowidget(button_name)

    # Checking if button has a value (X or O)
    if getting_button_value(row, col) == '':
        clicked_button.config(text=value)  # if it's empty then we set the value
        # changing to next value
        if value == 'X':
            value = 'O'
        else:
            value = 'X'

    # Checking game over
    gameover = checking_game_over()

    if gameover is True:
        print('Game Over!')
        showinfo("Game Over!", "Game over... click OK if you wish to restart :)")
        reseting_game()

####################################################################################
#   PART 1.2: FUNCTION getting_button_value (returns the button value/text: X or O)
####################################################################################

def getting_button_value(row,col):
    button_name=f'button_{row}_{col}'  # button name will show its coordinates (button_0_0, button_0_1)
    button=window.nametowidget(button_name)  # getting button from window
    return button ['text']   # returning button text ('X', 'O' or '')


####################################################################################
#   PART 2.3: FUNCTION checking_game_over
####################################################################################

# C0 C1 C2
#  x  x  x - row 0
#  O  O  O - row 1
#  O  O  O - row 2

def checking_game_over(): # checking rows, colums and diagonals to see if they have the same value and are not empty

    for n in [0,1,2]: # checking rows
        if getting_button_value(n, 0) == getting_button_value(n, 1) == getting_button_value(n, 2) != '':
            return True

    for col in range(3):  # checking columns
        if getting_button_value(0, col) == getting_button_value(1, col) == getting_button_value(2, col) != '':
            return True

    # checking diagonals
    if getting_button_value(0, 0) == getting_button_value(1, 1) == getting_button_value(2, 2) != '':
        return True
    if getting_button_value(0, 2) == getting_button_value(1, 1) == getting_button_value(2, 0) != '':
        return True


###############################################################################
        # PART 2.4: reseting_game => clears all buttons text
###############################################################################

def reseting_game():
    global value #using global variable value
    value='X' #as the game is reiniciated, it's necessary to start with X

    for row in range(3):
        for col in range(3):
            button_name=f'button_{row}_{col}'
            button=window.nametowidget(button_name)
            button.config(text='')

# C0 C1 C2
#  x  x  x - row 0
#  O  O  O - row 1
#  O  O  O - row 2


####################################################################################
#
#   PART 2: INITIALIZING
#   1 - Creating and setting window properties
#   2 - Creating font
#   3 - Declaring initial value (X)
#
####################################################################################



####################################################################################
             #   PART_1.1 - Creating and setting window properties
####################################################################################

# Instanciating class Tk() -> This variable window is an object of class Tk() from library tkinter
window=tk.Tk()

# Disable window resizing (it means user will not be unable to resize the window)
window.resizable(False, False)

# Setting window title
window.title('Tic-Tac-Toe')

####################################################################################
                             #   PART_1.2 - Creating font
####################################################################################

# Creating an instance of the class Font(), which means I'm creating an object
font_helv36 = tkf.Font(family='Helvetica', size=33, weight='bold')

####################################################################################
                             #   Part_1.3 - Declaring initial value (X)
####################################################################################

# initially, the variable "value" will receive "X"
value='X'


####################################################################################
#                  PART 3 - ADDING 9 BUTTONS TO MY CALCULATOR WINDOW
####################################################################################

for row in range(3):
    for col in range(3):
        action_when_clicked = partial(onclick_event, row, col)
        tk.Button(
            master=window, #parent=master do botão
            name=f'button_{row}_{col}',
            text='',
            font=font_helv36,
            width=3,
            height=1,
            command=action_when_clicked,
            bg="light blue",
        ).grid(column=col, row=row) #especificação das coordenadas do botão

#command está esperando uma ação. Sempre que o usuário clicar ele executa determinado comando. Mas qual botão q foi clicado?
# daí a necessidade da classe "partial". Dessa class estão sendo informados 3 parâmetros: a função onclick_event está sendo colocada como parâmentro.
#Essa ação será executada quando a ação acontecer. A função  "action_when_clicked" é diferente para cada botão.
# main loop
window.mainloop() #mantém a janela aberta dentro de um while q só termina qdo a janela fecha

print('the end!')

