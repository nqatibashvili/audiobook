import pyttsx3
import PyPDF3
book = open('audio.pdf', 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

