# including the tkinter gui library and providing as alias tk
import tkinter as tk


# class definition that inherits methods from the tkinter Frame superclass
class Application(tk.Frame):
    # method executed once at object creation that takes a tkinter param or defaults to none if not provided
    def __init__(self, master=None):
        # call the superclass init method and pass the tkinter object to the Frame superclass
        super().__init__(master)
        # instance variable gets param variable 
        self.master = master
        # instance variable that acts as a buffer
        self.buffer = []
        # instance variable that is the calculator screen, set to an empty string 
        self.screen = tk.StringVar()
        # update the calculator screen to have an initial value of zero
        self.screen.set('0')
        # a class method to create the ui elements for calculator
        self.create_widgets()

    # a class method that creates all the ui elements
    def create_widgets(self):
        # create an entry field, with the text contained in the calculator screen, position the text to be on the right of the container
        display = tk.Entry(self.master, textvariable=self.screen, justify=tk.RIGHT)
        # defines the width or how many columns the entry field spans across 
        display.grid(columnspan=4)

        # iterate over the string and give each entry an index
        for index, digit in enumerate('789/456*123-C0=+'):
            # create a new button object and initialise it to contain the character, pass the digit as argument to a lamda function
            btn = tk.Button(self.master, text=digit, command=self.cmd(digit))
            btn.grid(row=2 + index // 4, column=index % 4, sticky='nsew')

    # a class method that calls a lambda that is executed on the fly receives a parm
    def cmd(self, digit):
        # calls an auxillary method to check if a button that contains a digit was pressed on the ui
        return lambda arg=digit: self.key_pressed(arg)

    # a class method that contains logic to evaluate equations, receives parm
    def key_pressed(self, digit):
        # if the user does not clear the screen
        if digit is not 'C':
            # insert the select digits into a temporary buffer 
            self.buffer.append(digit)
            # update the calculator screen to have the contents of whats in the buffer
            self.screen.set(self.buffer)
        # otherwise the user cleared the screen
        elif digit is 'C':
            # empty the contents of the buffer
            self.buffer.clear()
            # update the calculator ui to contain this empty buffer
            self.screen.set(self.buffer)
            # update the ui screen to contain a zero
            self.screen.set('0')

        # the user wants to calculate an expression
        if digit is '=':
            # if entry is valid
            try:
                # remove the equals sign from the experssion as this caused errors when evaluating 
                self.buffer.remove('=')
                # convert list into a string and store the evaluation in result
                result = eval(''.join(self.buffer))
                # update the screen to contain the result
                self.screen.set(result)
                # clear the buffer for a new equation to be entered
                self.buffer.clear()
            # throws an exception but doesnt break the program e.g. (+-/5) not a valid expression
            except SyntaxError:
                # empty the contents of the 'bad' buffer
                self.buffer.clear()
                # output an error message to the calculator screen
                self.screen.set('Error')


# create an tkinter instance and pass it into the Application class
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
