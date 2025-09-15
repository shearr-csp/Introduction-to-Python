# refactored_analyzer.py
from collections import Counter

def read_text_file(file_name):
    """Reads a file and returns its content as a string."""
    with open(file_name, 'r') as text_file:
        return text_file.read()

def process_text_into_words(text_content):
    """Converts a string of text into a list of lowercase words."""
    return text_content.lower().split()

def count_word_frequencies(word_list):
    """
    Counts the frequency of each word in a list using 
    collections.Counter.
    """
    return Counter(word_list)

def find_long_words(word_list, min_length=3):
    """
    Finds all words in a list that are longer than the specified 
    minimum length.
    """
    return [word for word in word_list if len(word) > min_length]

def print_analysis(word_list, word_count, long_words):
    """Prints the analysis results to the console."""
    print(f"The total number of words is: {len(word_list)}")
    print(f"The unique words count is: {len(word_count)}")
    print("The most frequent words are:")
    

    word_counts = Counter(word_list)

    top_5_words = word_counts.most_common(5)

    for word, count in top_5_words:
        print(f"'{word}': {count}")
    
    print(f"Long words (more than 3 characters): {len(long_words)}")

def analyze_text(file_name):
    """
    This function analyzes a text file. 
    To improve modularity, this function calls the different helper 
    functions to analyze and print results.
    """
    # Read and process the text
    text_content = read_text_file(file_name)
    word_list = process_text_into_words(text_content)
    
    # Analyze the processed data
    word_count = count_word_frequencies(word_list)
    long_words = find_long_words(word_list)
    
    # Print the results
    print_analysis(word_list, word_count, long_words)


# File to have the text analyzed.
analyze_text("sample.txt")