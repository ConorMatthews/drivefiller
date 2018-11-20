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
                raise ValueError('Unable to create DriveFiller Object. The path specified does not exist or is inaccessible.')
            else:
                pass
        except:
            raise ValueError('Unable to create DriveFiller Object. Invalid path specified.')
        try:
            self.text = str(text)
        except:
            raise ValueError('Unable to create DriveFiller Object. Text cannot be empty or non-zero.')
        if filename == '':
            raise ValueError('Unable to create DriveFiller Object. Filename cannot be empty or non-zero.')
        try:
            if lines != None:
                lines = int(lines)
            else:
                pass
        except:
            raise TypeError('Unable to create DriveFiller Object. Lines must be an non-zero integer.')
    
    def fill(self):
        file = open(self.path + self.filename +'.txt', '+a')
        if self.lines != None:
            print('Writing to file')
            print('To abort, use ^C or [CTRL]^C...')
            for i in range(0, self.lines):
                file.write(self.text+'\n')
            print('Write Completed!')
        else:
            print('Starting Infinite Write.')
            print('To abort, use ^C or [CTRL]^C...')
            file = open(self.path + self.filename +'.txt', '+a')
            i = 0
            bpl = len(self.text)+1
            while True:
                file.write(self.text+'\n')
                i = i+1
                print(i, ' lines written. Total Bytes: ',bpl*i, end='\r')

    def checkSize(self):
        return os.stat(self.path + self.filename + '.txt').st_size
