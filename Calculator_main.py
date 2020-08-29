from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title('GPA Calculator')
root.geometry('360x200')

# -------------------------------------------------------------------------------------------
# Heading Size Setting
HeadingSize = tkFont.Font(size=13)

# -------------------------------------------------------------------------------------------
# COURSE NAMES HEADING and blank label for spacing out the rows
CourseHeading = Label(text='Course', font=HeadingSize).grid(row=0, column=0)
blankLabel = Label(text='      ').grid(row=0, column=1)

# -------------------------------------------------------------------------------------------
# GRADE HEADING
GradeHeading = Label(text='Grade (0-100)', font=HeadingSize).grid(row=0, column=2, )
blankLabel2 = Label(text='      ').grid(row=0, column=3)

# -------------------------------------------------------------------------------------------
# CREDIT AMOUNT HEADING
CreditHeading = Label(text='CREDITS', font=HeadingSize).grid(row=0, column=4, )

# -------------------------------------------------------------------------------------------
# COURSE NAME INPUTS
Course1 = Entry(root, justify='center')
Course1.grid(row=1, column=0)
Course1.insert(0, "Course 1")

Course2 = Entry(root, justify='center')
Course2.grid(row=2, column=0)
Course2.insert(0, "Course 2")

Course3 = Entry(root, justify='center')
Course3.grid(row=3, column=0)
Course3.insert(0, "Course 3")

Course4 = Entry(root, justify='center')
Course4.grid(row=4, column=0)
Course4.insert(0, "Course 4")

Course5 = Entry(root, justify='center')
Course5.grid(row=5, column=0)
Course5.insert(0, "Course 5")

# -------------------------------------------------------------------------------------------
# Grade inputs
Grade1 = Entry(root, justify='center', width=10)
Grade1.grid(row=1, column=2)

Grade2 = Entry(root, justify='center', width=10)
Grade2.grid(row=2, column=2)

Grade3 = Entry(root, justify='center', width=10)
Grade3.grid(row=3, column=2)

Grade4 = Entry(root, justify='center', width=10)
Grade4.grid(row=4, column=2)

Grade5 = Entry(root, justify='center', width=10)
Grade5.grid(row=5, column=2)

# -------------------------------------------------------------------------------------------
# Credit inputs
Credit1 = Entry(root, justify='center', width=7)
Credit1.grid(row=1, column=4)
Credit1.insert(0, str(3))

Credit2 = Entry(root, justify='center', width=7)
Credit2.grid(row=2, column=4)
Credit2.insert(0, str(3))

Credit3 = Entry(root, justify='center', width=7)
Credit3.grid(row=3, column=4)
Credit3.insert(0, str(3))

Credit4 = Entry(root, justify='center', width=7)
Credit4.grid(row=4, column=4)
Credit4.insert(0, str(3))

Credit5 = Entry(root, justify='center', width=7)
Credit5.grid(row=5, column=4)
Credit5.insert(0, str(3))


# -------------------------------------------------------------------------------------------
# BUTTON CLICK FUNCTION

def CalculateClick():
    numerator = (int(Grade1.get()) * int(Credit1.get())) + (int(Grade2.get()) * int(Credit2.get())) + (
                int(Grade3.get()) * int(Credit3.get())) + (int(Grade4.get()) * int(Credit4.get())) + (
                            int(Grade5.get()) * int(Credit5.get()))
    denominator = (
                int(Credit1.get()) + int(Credit2.get()) + int(Credit3.get()) + int(Credit4.get()) + int(Credit5.get()))

    CalculatedOutput = Label(text='Your weighted average is ' + str(numerator / denominator), wraplength=100).grid(
        row=7, column=2)


# -----------------------------------------------------------------------------------------------
# Calculate Button
blankLabel3 = Label(text='      ').grid(row=6, column=0)
CalculateButton = Button(root, text='Calculate CGPA', command=lambda: CalculateClick()).grid(row=7, column=0)

# -----------------------------------------------------------------------------------------------
root.mainloop()

# FORMULA FOR WEIGHTED AVERAGE CALCULATION
# int(GradeX.get()) * int(CreditX.get())
# CalculatedOutput = Label(text='Your weighted average is ' + str((int(Grade1.get()) * int(Credit1.get())) + (int(Grade2.get()) * int(Credit2.get())) + (int(Grade3.get()) * int(Credit3.get())) + (int(Grade4.get()) * int(Credit4.get())) + (int(Grade5.get()) * int(Credit5.get()))), wraplength=100)
