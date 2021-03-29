#Name: Calvin Warwick
#Date: 3-27-2020
#Program Name: Warwick_Module10_Word_Occurence_Documentation
#Purpose: Generates Documentation for the Word Occurence Program

#Imports
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from collections import Counter
from tkinter import messagebox
import collections
from io import StringIO
import unittest
import pydoc

# Initialize the dictionary
"""This starts the dictionary by initilizating the initial dictionary"""
wordcount = {}

#Unit Test
"""this creates the class for the unit test"""
class TestWordCounts(unittest.TestCase):
    TEST_FILENAME = './Macbeth Entire Play.txt'
    n_print = 5
    EXPECTED_RESULT = {'the' : 731,
                       'and' : 565,
                       'to' : 379,
                       'of' : 342,
                       'i' : 313}
    """this is where the unit test will begin to run"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_text()
    """This is the second method of the unit test where it tests whether we passed or not"""
    def test_collections_counter(self):
        ''' Count words collections.Counter. '''
        counter = collections.Counter((word for word in self.clean_text.split()))
        self.assertEqual(len(counter), len(self.EXPECTED_RESULT))
        self.assertEqual(counter, self.EXPECTED_RESULT)
        print('test_collections_counter passed')
    """This method will count the words manually"""
    def test_manual_count(self):
        ''' Count words manually. '''
        word_counts = self.count_words(self.clean_text)
        self.assertEqual(len(word_counts), len(self.EXPECTED_RESULT))
        self.assertEqual(word_counts, self.EXPECTED_RESULT)
        print('test_manual_count passed')

    def get_text(self):
        ''' Read test file then convert to lowercase and remove punctuation. '''
        with open(self.TEST_FILENAME, encoding="utf8") as file:
            text = file.read()

        cleaned = text.lower()
        for substring in '. , : " \' ! *'.split():
            cleaned = cleaned.replace(substring, "")
        self.clean_text = cleaned

    def count_words(self, file_text):
        wordcount = collections.defaultdict(int)
        for word in file_text.split():
            wordcount[word] += 1
        return dict(wordcount)


if __name__ == '__main__':

    # Run unit test, capture output, and then print it.
    output = StringIO()
    tests = unittest.TestLoader().loadTestsFromTestCase(TestWordCounts)
    test_result = unittest.TextTestRunner(stream=output).run(tests)
    print(output.getvalue())  # Print captured output from running test.

        

#open Macbeth text file
"""This opens the Macbeth text file"""
file = open('Macbeth Entire Play.txt', encoding="utf8")
a= file.read()
"""This creates the tkinter gui frame which is what the user will see"""
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__()  # Call __init__() method in parent (tk.Frame)
        """First Command that asks how many words to sort"""
        self.label = tk.Button(self, text='How many words to Sort?', command=self.ask_count)
        self.label.grid(row=0)
        """Second command button that will compute what we insert"""
        self.open_btn = tk.Button(text='Compute', command=self.ask_count)
        self.open_btn.pack(pady=(30,10))
        """Third command button that will exit out of the gui and destroy the program @ master.destroy"""
        self.exit_btn = tk.Button(text='Exit', command=master.destroy)
        self.exit_btn.pack()

    def ask_count(self):
        """this converts the txt file to a readable file"""   
        with open('Macbeth Entire Play.txt', encoding="utf8") as file:
            self.file_text = file.read()
        for word in a.lower().split():
          word = word.replace(".","")
          word = word.replace(",","")
          word = word.replace(":","")
          word = word.replace("\"","")
          word = word.replace("!","")
          word = word.replace("â€œ","")
          word = word.replace("â€˜","")
          word = word.replace("*","")
          """If and else statement that determines whether we count the word or not"""
          if word not in wordcount:
              wordcount[word] = 1
          else:
              wordcount[word] += 1
        n_print = int(input("How many most common words are: "))
        print("\nThe {} most common words are as follows\n".format(n_print))
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(n_print):
          print(word, ": ", count)
        messagebox.showinfo("Top words...", "The top words are: \n" + "\n".join([(str(word)+": "+str(count)) for word, count in word_counter.most_common(n_print)]))

        # Close the file
        file.close()
        messagebox.showinfo("The top words are: ")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Count words")
    root.geometry('400x400+900+50')
    app = Application(root)
    app.pack(expand=True, fill='both')
    root.mainloop()
    #run unit test
    unittest.main()
