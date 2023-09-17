# Importing
from dis import show_code
from tkinter import *
from tkinter import filedialog
import PyPDF2 as pdf
import os

# Now
root = Tk()
root.geometry("600x450+500+100") #(Weidth X Height + X-Cordinate + Y Cordinate)
# given geometry to tkinter GUI

root.title("PDF Viewer")
root.config(bg="lightblue")
# Define function so that button works
def browseFile():
    NameOfFile= filedialog.askopenfilename(initialdir=os.getcwd(),
                                       title = "SELECT FILE",
                                       filetypes=((
                                           "PDF Files (.pdf)", ".pdf"),
                                           ("PDF Files (.pdf)", ".PDF"),
                                           ))
    v1 = pdf.ShowPdf()
    v2 = show_code.pdf_view(root, pdf_location=open(NameOfFile,"r"),width=70,height=100)
    v2.pack()
# Creating Button
B1 = Button(root, text="OPEN THE FILE",command = browseFile,width=50,font="courier 18",bd=4)
B1.pack(padx=100, pady=50)
root.mainloop()

