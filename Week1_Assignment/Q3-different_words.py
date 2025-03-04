def count_unique_words(text):
    words = text.lower().split()  
    unique_words = set(words)  
    return len(unique_words)

string = """
I have provided this text to provide tips on creating interesting paragraphs.
First, start with a clear topic sentence that introduces the main idea.
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""

print("Number of different words:", count_unique_words(string))