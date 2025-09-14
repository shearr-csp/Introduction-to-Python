# unpythonic_analyzer.py
def analyze_text(file_name):
    # This function is full of bad practices.
    with open(file_name, 'r') as text_file:
        text_content = text_file.read()
    
    word_list = text_content.lower().split()
    
    # Let's count the occurrences of each word.
    word_count_dict = {}
    
    for word_item in word_list:
        if word_item in word_count_dict:
            word_count_dict[word_item] = word_count_dict[word_item] + 1
        else:
            word_count_dict[word_item] = 1
    
    # Now let's find the words with more than 3 characters.
    long_words = [word_element for word_element in word_list if len(word_element) > 3]
            
    print("The total number of words is: " + str(len(word_list)))
    print("The unique words count is: " + str(len(word_count_dict)))
    print("The most frequent words are:")
    
    for word, count in sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True)[:5]:
        print(f"'{word}': {count}")
    
    print(f"Long words (more than 3 characters): {len(long_words)}")
    
# You will need to create a text file named 'sample.txt' for testing.
analyze_text("sample.txt")