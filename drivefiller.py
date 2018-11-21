#Usage:
#>>> Filler_Oblect = df.(path, filename, text, line_amount, size_in_bytes) # Do not use in code - solely to show the variables that are needed

#Examples:
#To write 500 lines in the file 'text.txt' stored in 'C:\Documents\' with the text 'Hello World!' and check size in bytes:
#>>> import DriveFiller as df
#>>> Filler_Object = df.filler('C:\Documents\', 'text', 'Hello World!', 500, 0)
#>>> Filler_Object.fill()
#>>> print(Filler_Object.sizeCheck()) # Outputs in bytes

#To write approx. 10,000 bytes in the file'text.txt' stored in 'C:\Documents\' with the text 'Hello World!' and check size in bytes:
#>>> import DriveFiller as df
#>>> Filler_Object = df.filler('C:\Documents\', 'text', 'Hello World!', 0, 10000)
#>>> Filler_Object.fill()
#>>> print(Filler_Object.sizeCheck()) # Outputs in bytes

#N.B Line amount and size is optional. If no line amount is specified, the program will fill infinitely until interrupted

import os
import sys
class filler:
    def __init__(self, path, filename, text, lines=None, size=None):
        self.path = path
        self.filename = filename
        self.text = text
        self.lines = lines
        self.size = size
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
                if size != None:
                    size = int(size)
                else:
                    pass
        except:
            raise TypeError()

    
    def fill(self):
        if self.lines > 0 and self.lines != None:
            file = open(self.path + self.filename +'.txt', '+a')
            for i in range(0, self.lines):
                file.write(self.text+'\n')
            file.close()
        elif self.size > 0 and self.size != None:
            while True:
                file = open(self.path + self.filename +'.txt', '+a')
                if os.stat(self.path + self.filename + '.txt').st_size < self.size:
                    file.write(self.text+'\n')
                    file.close()
                else:
                    break
                    
        else:
            file = open(self.path + self.filename +'.txt', '+a')
            i = 0
            bpl = len(str(self.text))+1
            while True:
                file.write(self.text+'\n')
                i = i+1

    def checkSize(self):
        return os.stat(self.path + self.filename + '.txt').st_size
