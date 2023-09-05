from tkinter import *
import random
from tkinter import messagebox


# Function to set number and lives
def set_number(level):
    hearts = 0
    number = 0
    heading_text = ""
    if (level == "easy"):
        heading_text = " 1-20"
        hearts = 4
        number = random.randint(1,20)
    elif (level == "medium"):
        heading_text = " 1-50"
        hearts = 5
        number = random.randint(1,50)
    else:
        heading_text = " 1-100"
        hearts = 7
        number = random.randint(1,100)
    return heading_text,hearts, number

# Forth page function
def forth_page():
    def yes_action():
        root.destroy()
        first_page()
        
    
    def no_action():
        root.destroy()
        exit()

    root = Tk()
    root.title("Guess number game")
    root.geometry("400x500")
    root['background']='#856ff8'
    root.minsize(400,500)
    root.maxsize(400,500)

    greeting_text = Label(root, text="Do to want to play again?", font= ('Helvetica 20 bold'), bg= '#856ff8', fg='#18122B')
    greeting_text.pack()
    greeting_text.place(y=50, relx= 0.5, anchor='center')   

    btn_yes = Button(root, text = 'Yes', command= lambda: yes_action(),
                    font= ('Helvetica 10 normal'), bg="#443C68", fg="#ffffff")
    btn_yes.pack()
    btn_yes.place(y = 120, width=80, relx= 0.5, anchor='center')

    btn_no = Button(root, text = 'No', command= lambda: no_action(),
                    font= ('Helvetica 10 normal'), bg="#cc3549")
    btn_no.pack()
    btn_no.place(y = 155, width=80, relx= 0.5, anchor='center')

    root.mainloop()

# Forth page function
def third_page(level, player_name):
    HEARTS = []
    heading_text,hearts, number = set_number(level)
    HEARTS.append(hearts)
    def write_to_file(condition):
         file = open("log.txt","a")
         text = player_name + " " + condition + '\n'
         file.write(text)
         file.close()
         
    def submit():
        inp = inputtxt.get(1.0, "end-1c")
        result = play_game(inp)
        if(HEARTS[0] <= 0):
            messagebox.showerror("Sorry", "You lost! Number was "+ str(number))
            write_to_file("lost")
            root.destroy()
            forth_page()
        if(result == 1):
            messagebox.showinfo("Congrats", "You won!")
            write_to_file("won")
            root.destroy()
            forth_page()
            
        elif(result == 2):
            messagebox.showerror("Wrong answer", "Go down!")
        else:
            messagebox.showerror("Wrong answer", "Go up!")
           
    def play_game(inp):
        if (int(inp) == number):
            return 1

        HEARTS[0] -= 1
        hearts_text['text'] = str(HEARTS[0]) # This line update lives of user after guess a number wrong
        if(int(inp) > int(number)):
            return 2
        else:
            return 3
    
    root = Tk()
    root.title("Guess number game")
    root.geometry("400x500")
    root['background']='#856ff8'
    root.minsize(400,500)
    root.maxsize(400,500)
    greeting_text = "Hi " + player_name

    greeting_text = Label(root, text=greeting_text, font= ('Helvetica 20 bold'), bg= '#856ff8', fg='#18122B')
    greeting_text.pack()
    greeting_text.place(y=50, relx= 0.5, anchor='center')

    text2 = Label(root, text='Choose a number between' + heading_text, font= ('Helvetica 12 normal'),
                        bg= '#856ff8', fg='#18122B')
    text2.pack()
    text2.place(y=90, relx= 0.5, anchor='center')

    emoji = Label(root, text="\u2764\ufe0f", font= ('Helvetica 12 normal'), bg= '#856ff8', fg='#18122B')
    emoji.pack()
    emoji.place(anchor='nw')
    hearts_text = Label(root, text=str(hearts), font= ('Helvetica 12 normal'), bg= '#856ff8', fg='#18122B')
    hearts_text.pack()
    hearts_text.place(x = 30, anchor='nw')

    inputtxt = Text(root,height = 2,width = 20)
    inputtxt.pack()
    inputtxt.place(y = 150, relx= 0.5, anchor='center')

    btn_easy = Button(root, text = 'Submit', command= lambda: submit(),
                    font= ('Helvetica 10 normal'), bg="#443C68", fg="#ffffff")

    btn_easy.pack()
    btn_easy.place(y = 200, width=80, relx= 0.5, anchor='center')
    root.mainloop()

# Second page function
def second_page(palyer_name):

    def game_window(level):
        root.destroy()
        third_page(level, palyer_name)

    
    root = Tk()
    root.title("Guess number game")
    root.geometry("400x500")
    root['background']='#856ff8'
    root.minsize(400,500)
    root.maxsize(400,500)
    greeting_text_ = "Hi " + palyer_name

    greeting_text = Label(root, text=greeting_text_, font= ('Helvetica 20 bold'), bg= '#856ff8', fg='#18122B')
    greeting_text.pack()
    greeting_text.place(y=50, relx= 0.5, anchor='center')

    level_text = Label(root, text='Choose level of difficulty', font= ('Helvetica 12 normal'), bg= '#856ff8', fg='#18122B')
    level_text.pack()
    level_text.place(y=90, relx= 0.5, anchor='center')

    btn_easy = Button(root, text = 'Easy',command=lambda: game_window("easy"),
                    font= ('Helvetica 10 normal'), bg="#443C68", fg="#ffffff")
    btn_medium = Button(root, text = 'Medium',command=lambda: game_window("medium"),
                        font= ('Helvetica 10 normal'), bg="#443C68", fg="#ffffff")
    btn_hard = Button(root, text = 'Hard',command=lambda: game_window("hard"),
                    font= ('Helvetica 10 normal'), bg="#443C68", fg="#ffffff")
    btn_easy.pack()
    btn_easy.place(y = 150, width=80, relx= 0.5, anchor='center')
    btn_medium.pack()
    btn_medium.place(y = 185, width=80, relx= 0.5, anchor='center')
    btn_hard.pack()
    btn_hard.place(y = 220, width=80, relx= 0.5, anchor='center')
    root.mainloop()


# First page
def first_page():
    def submit():
        inp = inputtxt.get(1.0, "end-1c")
        root.destroy()
        second_page(inp)

    root = Tk()
    root.title("Guess number game")
    root.geometry("400x500")
    root['background']='#856ff8'
    root.minsize(400,500)
    root.maxsize(400,500)

    greeting_text = Label(root, text='Welcome to my game', font= ('Helvetica 20 bold'), bg= '#856ff8', fg='#18122B')
    greeting_text.pack()
    greeting_text.place(y=50, relx= 0.5, anchor='center')

    level_text = Label(root, text='Enter your name', font= ('Helvetica 12 normal'), bg= '#856ff8', fg='#18122B')
    level_text.pack()
    level_text.place(y=90, relx= 0.5, anchor='center')

    inputtxt = Text(root,height = 2,width = 20)
    inputtxt.pack()
    inputtxt.place(y = 150, relx= 0.5, anchor='center')
    btn_easy = Button(root, text = 'Submit',command=lambda: submit(),
                    font= ('Helvetica 10 normal'), bg="#443C68", fg="#ffffff")
    btn_easy.pack()
    btn_easy.place(y = 200, width=80, relx= 0.5, anchor='center')
    root.mainloop()

first_page()
