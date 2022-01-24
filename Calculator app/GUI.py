from stringprep import b3_exceptions
from tkinter import *
from numpy import outer

from sympy import false, true

class gui:


    def __init__(self):

        self.currentnumber = ""
        self.firstnumber = false
        self.numberstore = []
        self.orderoperations = []
        self.currentoperator = ""

        def buttonfunction(val):

  

            #0-9 numbers
            #10 plus
            #11 minus
            #12 divide
            #13 multiply
            #14 equals
            #15 clear

            if val == 0:
                if self.firstnumber == false:
                    print("First number can't be a negative")

                else:
                    self.firstnumber = true
                    self.currentnumber = self.currentnumber + str(val)
                    print(self.currentnumber)

            elif val in range (1,10):
                self.firstnumber = true
                self.currentnumber= self.currentnumber + str(val)
                print(self.currentnumber)


            elif val in range (10,14):

                if val == 10:
                    
                    if self.currentoperator == "":
                        self.currentoperator = "+"
                        self.numberstore.append(int(self.currentnumber))
                        self.currentnumber = ""
                        self.orderoperations.append("+")
                        print(self.numberstore)

                    else:
                        self.currentoperator = "+"
                        self.orderoperations.pop(-1)
                        self.orderoperations.append("+")
                    
                                
                elif val == 11:
                    
                    if self.currentoperator == "":
                        self.currentoperator = "-"
                        self.numberstore.append(int(self.currentnumber))
                        self.currentnumber = ""
                        self.orderoperations.append("-")
                        print(self.numberstore)
                    
                    else:
                        self.currentoperator = "-"
                        self.orderoperations.pop(-1)
                        self.orderoperations.append("-")
                    

                elif val == 12:
                    if self.currentoperator == "":
                        self.currentoperator = "/"
                        self.numberstore.append(int(self.currentnumber))
                        self.currentnumber = ""
                        self.orderoperations.append("/")
                        print(self.numberstore)
                    else:
                        self.currentoperator = "/"
                        self.orderoperations.pop(-1)
                        self.orderoperations("/")

                    
                            
                elif val == 13:
    
                    if self.currentoperator == "":
                        self.numberstore.append(int(self.currentnumber))
                        self.currentnumber = ""
                        self.orderoperations.append("x")
                        print(self.numberstore)
                    else:
                        self.currentoperator = "x"
                        self.orderoperations.pop(-1)
                        self.orderoperations("x")



            elif val == 14:
                self.numberstore.append(int(self.currentnumber))
                print(self.orderoperations)
                print(self.numberstore)
                        
                finalcalc = []

        

                operation = [item for sublist in zip(self.numberstore, self.orderoperations) for item in sublist]
                
                finalnum = self.numberstore[-1]

                operation.append(finalnum)

                
                operation = str(operation)

                operation = operation.replace("[", "")
                operation = operation.replace("]", "")
                operation = operation.replace("'", "")
                operation = operation.replace(",", "")

                if "x" in operation:
                    operation = operation.replace("x", "*")
                    operation = operation.replace("'", "")
                else:
                    pass

                output = eval(operation)

                print(output)

            elif val == 15:
                self.currentnumber = ""
                self.firstnumber = false
                self.numberstore = []
                self.orderoperations = []


            

        root = Tk()
        #GUI basic attributes
        root.geometry("400x620")
        root.config(bg="white")
        root.title("Calculator")
        root.resizable(FALSE, FALSE)

        #display area

        displayarea= Canvas(root, width=360, height=100)
        displayarea.place(x=20, y=20)

        b7 = Button(root, text="7", bg="white", padx=50, pady=35, command=lambda: buttonfunction(7))

        b7.place(x=20, y=160)

        b8 = Button(root, text="8", bg="white", padx=50, pady=35, command=lambda: buttonfunction(8))
        b8.place(x=150, y=160)

        b9 = Button(root, text="9", bg="white", padx=45, pady=35, command=lambda: buttonfunction(9))
        b9.place(x=280, y=160)



        b4 = Button(root, text="4", bg="white", padx=50, pady=35, command=lambda: buttonfunction(4))
        b4.place(x=20, y=270)

        b5 = Button(root, text="5", bg="white", padx=50, pady=35, command=lambda: buttonfunction(5))
        b5.place(x=150, y=270)

        b6 = Button(root, text="6", bg="white", padx=45, pady=35, command=lambda: buttonfunction(6))
        b6.place(x=280, y=270)


        b1 = Button(root, text="1", bg="white", padx=50, pady=35,command=lambda: buttonfunction(1))
        b1.place(x=20, y=380)

        b2 = Button(root, text="2", bg="white", padx=50, pady=35, command=lambda: buttonfunction(2))
        b2.place(x=150, y=380)

        b3 = Button(root, text="3", bg="white", padx=45, pady=35, command=lambda: buttonfunction(3))
        b3.place(x=280, y=380)

        b0 = Button(root, text="0", bg="white", padx=50, pady=45, command=lambda: buttonfunction(0))
        b0.place(x=150, y=490)

        plus = Button(root, text="+", bg="grey", padx=20, pady=15, command=lambda: buttonfunction(10)) 
        plus.place(x=20, y=490)

        subtract = Button(root, text="-", bg="grey", padx=20, pady=15, command=lambda: buttonfunction(11)) 
        subtract.place(x=80, y=490)

        multiply = Button(root, text="x", bg="grey", padx=20, pady=15, command=lambda: buttonfunction(13)) 
        multiply.place(x=20, y=550)

        divide = Button(root, text="/", bg="grey", padx=20, pady=15, command=lambda: buttonfunction(12)) 
        divide.place(x=80, y=550)

        equals = Button(root, text="=", bg="grey", padx=44, pady=15, command=lambda: buttonfunction(14))
        equals.place(x=280, y=490)


        clear = Button(root, text="Clear", bg="grey", padx=35, pady=15, command=lambda: buttonfunction(15))
        clear.place(x=280, y=550)


        root.mainloop()





object1 = gui()


