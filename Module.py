#1st module
""""

print("Text to speach in python")
import pyttsx3
engine = pyttsx3.init()
engine.say("Hey Code With Me ?")
engine.runAndWait()

"""
#2nd module
"""
print("Python code to get different jokes")

import pyjokes
joke = pyjokes.get_joke()
print(joke)

"""
#3rd module


print("Write a python program to print the contents of a directory using the os module. Search online for the function which does it")
import os

def print_directory_contents(path='/'):
    """Prints all entries in the given directory."""
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except Exception as e:
        print(f"Error accessing directory '{path}': {e}")

if __name__ == '__main__':
    # Optionally, you can pass a directory path here
    print_directory_contents()

