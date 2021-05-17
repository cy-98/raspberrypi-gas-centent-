from tkinter import *

white = '#FFF'

class WindowInstance():

    def __init__(self):
        self.window = Tk()

    def start(self):
        self.load()
        self.show()

    def load(self): 
        # data
        self.rules = []
        self.data  = {}
        #components
        self.formWidth = 40
        self.form = Frame(self.window, pady=10, bg=white)
        
        self.gasVariable       = Variable()
        self.operatorVariable  = StringVar()
        self.celesiusVarirable = Variable()
        
        self.fields('gas', self.gasVariable, self.gasRule)
        self.fields('operator', self.operatorVariable, self.operatorRule)
        self.fields('celesius', self.celesiusVarirable, self.celesiusRule)
        
        self.formSubmitBtn = Button(self.form, text='submit', width=self.formWidth, bg='#3f8', command=self.validate)
        self.formSubmitBtn.pack()
        self.form.pack()

    def validate(self):
        for rule in self.rules:
            isValidate, info = rule()
            if not(isValidate):
                messagebox.showerror('please check input box', info)
                return
        # TODO: upload data or ...
        
        
    def gasRule(self):
        content = self.gasVariable.get()
        try:
            value = float(content)
        except ValueError:
            return (False, 'gas content must be a number!')
        else:
            return (True, '')

    def operatorRule(self):
        content = self.operatorVariable.get()
        try:
            value = float(content)
        except ValueError:
            return (True, '')
        else:
            return (False, 'operator could not be a number!')
    
    def celesiusRule(self):
        content = self.celesiusVarirable.get()
        try:
            value = float(content)
        except ValueError:
            return (False, 'celesius must be a number')
        else:
            return (True, '')

    def fields(self, text, var, rule):
        Label(self.form, width=self.formWidth, text=text, pady=5).pack()
        Entry(self.form, width=self.formWidth, textvariable=var).pack()
        self.rules.append(rule)
        
    def show(self):
        maxWidth, maxHeight  = self.window.maxsize()
        width  = min(maxWidth, 1200)
        height = min(maxHeight, 800)
        self.window['bg'] = white
        self.window.title('gas content')
        self.window.geometry("%dx%d"%(width, height))
        self.window.mainloop()

def OpenWindow():
    window = WindowInstance()
    window.start()
    
OpenWindow()
