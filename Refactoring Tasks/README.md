# Text Analyzer
## Project Overview
This program built in Python is designed to analyze a given text file. 
It provides total word count, unique word count, the top 5 most frequent 
words, and the number of long words (more than 3 characters).

## Features
This program has the following features:
1. Provides a total word count.
2. Unique word count
3. Provides the top 5 most frequent words
4. The number of long words. 

## How to Run the Program
1. To run this program: Ensure that you have Python 3 installed on your system.
2. Clone repository: Clone this repository to your local computer using Git.
   - git clone [https://github.com/shearr-csp/Introduction-to-Python/tree/main/Refactoring%20Tasks]
3. Navigate to the project directory:
   - cd Introduction-to-Python/Refactoring Tasks
4. Run the program:
   - python3 text_analyzer.py

## Refactoring Improvements
This version of the text analyzer has been significantly improved for 
readability, efficiency, and maintainability. Key improvements include:
1. Modularity: This program was broken down into several functions. For example,     
   read_text_file handles file, process_text_into_words handles text formatting, and count_word_frequencies performs the word counting. This improves readablity and easier 
   debugging.
2. PEP 8 Compliance: All function and variable names now adhere to snake_case, improving     
   readability. Docstrings were added to each function to clearly explain its purpose, and proper spacing was followed.
3. with: A with statement is used for file handling in read_text_file, ensuring that the 
   file is always closed, even if errors occur.
4. List comprehension: A list comprehension is used in find_long_words to create the list of 
   long words.
5. collections.Counter: The collections.Counter object is used to count word frequencies, 
   replacing a manual dictionary.