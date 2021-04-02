from tkinter.filedialog import askopenfilename
from tkinter import *
import pyttsx3
import PyPDF2
window = Tk()

engine= pyttsx3.init('sapi5')
print(pyttsx3.init())
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
def say(audio):
    engine.say(audio)
    engine.runAndWait()

def open_file():
    path = askopenfilename(filetype=[('PDF','*.pdf')])
    with open(path, 'rb') as file:
        pdfReader = PyPDF2.PdfFileReader(file)
        pages = pdfReader.numPages
        print('total pages: ',pages)
        what_page_read = pdfReader.getPage(int(input('What page i read: ')))
        text = what_page_read.extractText()
        speak(text)
        # print(text)

btn = Button(text='open file',command=open_file)
btn.pack()


window.mainloop()