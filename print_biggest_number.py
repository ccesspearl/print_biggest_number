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

    result_label.config(result_label.config(text=f"{biggest} is the biggest number"))

# creating main window
root = tk.Tk()
root.title("Find the Biggest Number")
root.geometry("650x350")
root.iconbitmap(r'C:\Users\Princess\Desktop\python\learn\favicon (1).ico')
root.configure(bg="cyan")

# creating upper frame
upper_frame = tk.Frame(root, bg="yellow")
upper_frame.pack(fill="both")

root.mainloop()


