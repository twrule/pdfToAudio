from PyPDF2 import PdfFileReader, PdfFileWriter
from gtts import gTTS
import os

def main():
	print("Welcome to your Audio-Book Generator\n")
	filePath = input("Please Enter Your PDF filepath: ")
	pdf = PdfFileReader(filePath)

	txtFileName = input("What would you like the .txtFile called (please note anything with the same filename will be overwritten): ")

	txtFileName = txtFileName + ".txt"

	pdfToText(pdf, txtFileName)

	parseTxtFile(txtFileName)

	if os.path.exists('asdf.txt'):
		os.remove('asdf.txt')

	textToAudio(txtFileName)


def pdfToText(pdf, txtFileName):
	with open('asdf.txt', 'w') as f:
		for pageNum in range(pdf.numPages):
			pageObj = pdf.getPage(pageNum)

			try:
				txt = pageObj.extractText()
			except:
				pass
			else:
				f.write(txt)

		f.close();

def parseTxtFile(txtFileName):
	with open('asdf.txt', 'r') as infile, open(txtFileName, 'w') as outfile:
		# I have a Moby Dick pdf and below are a few weird things in the file I wanted to parse out
		Lines = infile.readlines()
		for line in Lines:
			if '˜˙' in line or '˜˚' in line or '˜˜' in line or 'ˇ˘ˇ' in line or '.˙' in line or '˛˘' in line:
				line = ""
			line = line.replace("™", "")
			line = line.replace("Š", "")
			line = line.replace("˘", "")
			line = line.replace("˜", "")
			line = line.replace("˚", "")
			outfile.write(line)
		# ===================================================
		infile.close()
		outfile.close()


		


def textToAudio(txtFileName):
	data = None
	with open(txtFileName, 'r') as file:
		data = file.read().replace('\n', '')
	tts = gTTS(text = data, lang = 'en')
	tts.save("audio.mp3");
	file.close()

if __name__ == "__main__":
	main()
