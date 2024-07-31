from tkinter import * 

def converter():
    kilogram = kg_value.get()

    gram = (float(kilogram)*1000)
    gram_answer.config(text = str(gram), font = ("times"))

    pound = (float(kilogram)*2.205)
    pound_answer.config(text = str(pound))   

    ounce = (float(kilogram)*35.274)
    ounce_answer.config(text = str(ounce))


 
window = Tk()
window.geometry("730x160")
window.title("Conveting Kg")
window.config(background= "white")

#first row 
question = Label(window, text = "Enter the weight in Kg:", fg = "black", bg = "white", font = ("times", 20)).grid(row = 1, column = 1, padx = 30, pady = 5)
kg_value = Entry(window)
convert = Button(window, text = "Convert", width = 10, command = converter).grid(row = 1, column = 3, padx= 60)

#second row
gram_label = Label(window, text = "Gram:", bg = "white", fg = "black", font = ("arial", 30, "bold")).grid(row = 2, column = 1, pady = 20)
pound_label = Label(window, text = "Pound:", bg = "white", fg = "black", font = ("arial", 30, "bold")).grid(row = 2, column = 2)
ounce_label = Label(window, text = "Ounce:", bg = "white", fg = "black", font = ("arial", 30, "bold")).grid(row = 2, column = 3)

#third row 
gram_answer = Label(window, fg = "white", bg = "grey", width = 25)
pound_answer = Label(window, fg = "white", bg = "grey", width = 25)
ounce_answer = Label(window, fg = "white", bg = "grey", width = 25)


#placing some of the already created widgets 
kg_value.grid(row = 1, column = 2)
gram_answer.grid(row = 3, column = 1)
pound_answer.grid(row = 3, column = 2)
ounce_answer.grid(row = 3, column = 3)


window.mainloop()

