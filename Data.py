from tkinter import *
import csv

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()

    def output(self):
        Label(text="Donor Organ Details").pack(side=LEFT,padx=5,pady=5)
        Label(text='Name:').pack(side=LEFT,padx=5,pady=5)
        self.e = Entry(root, width=10)
        self.e.pack(side=LEFT,padx=5,pady=5)
        Label(text='Inactive Time:').pack(side=LEFT, padx=5, pady=5)
        self.e1 = Entry(root, width=10)
        self.e1.pack(side=LEFT, padx=5, pady=5)
        Label(text='Blood Group:').pack(side=LEFT, padx=5, pady=5)
        self.e2 = Entry(root, width=10)
        self.e2.pack(side=LEFT, padx=5, pady=5)
        Label(text='Contact No.:').pack(side=LEFT, padx=5, pady=5)
        self.e3 = Entry(root, width=10)
        self.e3.pack(side=LEFT, padx=5, pady=5)
        Label(text='Age:').pack(side=LEFT, padx=5, pady=5)
        self.e4 = Entry(root, width=10)
        self.e4.pack(side=LEFT, padx=5, pady=5)

        self.b = Button(root, text='Submit', command=self.writeToFile)
        self.b.pack(side=RIGHT,padx=5,pady=5)



    def writeToFile(self):
        with open('set.csv', 'a') as f:
            w = csv.writer(f, quoting=csv.QUOTE_ALL)
            #w1 = csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([self.e.get()])
            w.writerow([self.e1.get()])
            w.writerow([self.e2.get()])
            w.writerow([self.e3.get()])
            w.writerow([self.e4.get()])

if __name__ == "__main__":
    root=Tk()
    root.title('Auto Logger')
    root.geometry('1000x100')
    app=App(master=root)
    app.mainloop()
    root.mainloop()