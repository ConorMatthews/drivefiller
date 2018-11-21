#Usage:
#To write 500 lines in the file 'text.txt' stored in 'C:\Documents\' with the text 'Hello World!' and check size in bytes:
#>>> import DriveFiller as df
#>>> Filler_Oblect = df.(path, filename, text, line_amount) # Do not use in code - solely to show the variables that are needed
#>>> Filler_Object = df.filler('C:\Documents\', 'text', 'Hello World!', 500)
#>>> Filler_Object.fill()
#>>> print(Filler_Object.sizeCheck()) # Outputs in bytes
#N.B Line amount is optional. If no line amount is specified, the program will fill infinitely untill KeyboardInterrupted.

import os
import sys
class filler:
    def __init__(self, path, filename, text, lines=None):
        self.path = path
        self.filename = filename
        self.text = text
        self.lines = lines
        try:
            if os.path.isdir(path) != True:
                raise ValueError()
            else:
                pass
        except:
            raise ValueError()
        try:
            self.text = str(text)
        except:
            raise ValueError()
        if filename == '':
            raise ValueError()
        try:
            if lines != None:
                lines = int(lines)
            else:
                pass
        except:
            raise TypeError()
    
    def fill(self):
        file = open(self.path + self.filename +'.txt', '+a')
        if self.lines != None:
            for i in range(0, self.lines):
                file.write(self.text+'\n')
        else:
            file = open(self.path + self.filename +'.txt', '+a')
            i = 0
            bpl = len(str(self.text))+1
            while True:
                file.write(self.text+'\n')
                i = i+1

    def checkSize(self):
        return os.stat(self.path + self.filename + '.txt').st_size
