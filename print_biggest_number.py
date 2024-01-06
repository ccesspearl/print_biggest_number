# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# Pseudocode

# ask user to input 3 numbers
#print("We will ask you to input 3 numbers. In order to find the biggest number, you will only input numbers and not letters. Do not input same numbers.")
#print ()

# ask user to input 1st number
#first_number = float(input("Input first number: "))

# ask user to input 2nd number
#second_number = float(input("Input second number: ")) 

# ask user to input 3rd number
#third_number = float(input("Input third number: "))

# check if the first number is bigger
#if first_number > second_number and first_number > third_number:
    #biggest = first_number

# check if the second number is bigger
#elif second_number > first_number and second_number > third_number:
    #biggest = second_number

# check if the third number is bigger
#else:
    #biggest = third_number 

# print the biggest number
#print()
#print(biggest, "is the biggest number")




# using Tkinter 
import tkinter as tk

# turning the previous code into def function 
# finding the biggest number
def find_biggest():
    first_number = float(entry1.get())
    second_number = float(entry2.get())
    third_number = float(entry3.get())

    if first_number > second_number and first_number > third_number:
        biggest = first_number
    elif second_number > first_number and second_number > third_number:
        biggest = second_number
    else:
        biggest = third_number

    result_label.config(
        text=f"{biggest} is the biggest number.",
        font=("Courier", 13, "bold"),
        fg="blue", 
        bg="light green",
        border=1,  
        relief="solid"
    )

# creating main window
root = tk.Tk()
root.title("Find the Biggest Number")
root.geometry("800x380")
root.iconbitmap(r'C:\Users\Princess\Desktop\Assignments\print_biggest_number\numbersymbol.ico')
root.configure(bg="cyan")

# left and right icons 
left_icon_path = r"C:\Users\Princess\Desktop\Assignments\print_biggest_number\icon.png"
right_icon_path = r"C:\Users\Princess\Desktop\Assignments\print_biggest_number\icon.png"

left_icon = tk.PhotoImage(file=left_icon_path)
right_icon = tk.PhotoImage(file=right_icon_path)

# creating upper frame
upper_frame = tk.Frame(root, bg="yellow")
upper_frame.pack(fill="both")

# creating a title frame for left and right icon 
title_frame = tk.Frame(upper_frame, bg="yellow")
title_frame.pack()

# adding left icon
left_icon_label = tk.Label(title_frame, image=left_icon, bg="yellow")
left_icon_label.pack(side="left")

# adding title
title_label = tk.Label(title_frame, text="THE SEARCH FOR BIGGEST NUMBER", fg="black", font=("8514oem", 25), bg="yellow")
title_label.pack(side="left", padx=10) 

# adding right icon
right_icon_label = tk.Label(title_frame, image=right_icon, bg="yellow")
right_icon_label.pack(side="left")

# creating middle frame
middle_frame = tk.Frame(root, bg="cyan")
middle_frame.pack(fill="both")

# reminding the users 
text_label = tk.Label(middle_frame, text="\nWe will ask you to input 3 numbers. In order to find the biggest number, \nyou will only input numbers and not letters. Do not input same numbers.\n", font=("Courier", 10), bg="cyan")
text_label.pack()

# creating input labels and entry widgets

# asking user to input the first number 
tk.Label(middle_frame, text="Input first number: ", bg="cyan").pack()
entry1 = tk.Entry(middle_frame)
entry1.pack()

# asking user to input the second number 
tk.Label(middle_frame, text="Input second number: ", bg="cyan").pack()
entry2 = tk.Entry(middle_frame)
entry2.pack()

# asking user to input the third number 
tk.Label(middle_frame, text="Input third number: ", bg="cyan").pack()
entry3 = tk.Entry(middle_frame)
entry3.pack()

# creating lower frame
lower_frame = tk.Frame(root, bg="cyan")
lower_frame.pack()

# creating submit button 
submit_button = tk.Button(lower_frame, text="Submit", command=find_biggest, bg="yellow")
submit_button.pack(pady=10)

# labeling to display the result
result_label = tk.Label(lower_frame, text="", bg="cyan")
result_label.pack(pady=10)

root.mainloop()


