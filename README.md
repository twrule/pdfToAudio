# pdfToAudio

One of my new years resolutions is to read at least one book a month for the year 2021.
I personally don't mind reading and quite enjoy it but the largest issue is that
reading takes too long.  My favorite way to read is to simply read while also listening
to an audiobook.  While there are services that allow you to purchase audiobooks,
I would like to find pdf's of books have a program that reads off the pdf.  Additionally
I want the program to have variable speeds so I could speed up and slow down the rate
at which the pdf is spoken from to make reading along go much faster.

I plan on building this program using python.  My idea is to first figure out a way of
taking a pdf file and then turning it into a text file.  From there I can use the Google
Text to Speech API which will allow me to easily convert the text to an mp3 file.  
Finally I must find a way to speed up or slow down that mp3 file and attempt to create an
interface to do that.

Found a Python Package called PyPDF2 that converts pdf files to txt files.


To run first install PyPDF2 (pip install PyPDF2) 	
Next Install Google Text-To-Speech (pip install gTTS)