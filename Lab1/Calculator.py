import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.buffer = []
        self.screen = tk.StringVar()
        self.screen.set('0')
        self.create_widgets()

    def create_widgets(self):
        display = tk.Entry(self.master, textvariable=self.screen, justify=tk.RIGHT)
        display.grid(columnspan=4)

        for index, digit in enumerate('789/456*123-C0=+'):
            btn = tk.Button(self.master, text=digit, command=self.cmd(digit))
            btn.grid(row=2 + index // 4, column=index % 4, sticky='nsew')

    # insert comments here
    def cmd(self, digit):
        return lambda arg=digit: self.key_pressed(arg)

    def key_pressed(self, digit):
        if digit is not 'C':
            self.buffer.append(digit)
            self.screen.set(self.buffer)
        elif digit is 'C':
            self.buffer.clear()
            self.screen.set(self.buffer)
            self.screen.set('0')

        if digit is '=':
            try:
                self.buffer.remove('=')
                # convert list into a string and store the evaluation in result
                result = eval(''.join(self.buffer))
                self.screen.set(result)
                self.buffer.clear()
            except SyntaxError:
                self.buffer.clear()
                self.screen.set('Error')


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
