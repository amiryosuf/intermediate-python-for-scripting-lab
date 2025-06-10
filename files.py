# Create a function that reads a text file and counts the number of words in the text file
# Ensure it handles potential "FilenotFoundError" exceptions gracefully
def count_words_in_file(file_path):
    """
    Counts the number of words in a text file.
    Reads the file at the specified path and returns the word count.
    Handles potential FileNotFoundError exceptions gracefully.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0
    


# Create a function that takes a list of strings
# Ensure it writes each string to a new line in a file named "output.txt"
def write_strings_to_file(strings, file_path='output.txt'):
    """
    Writes a list of strings to a file, each string on a new line.
    
    Parameters:
    - strings: List of strings to write to the file.
    - file_path: The path to the output file (default is 'output.txt').
    """
    try:
        with open(file_path, 'w') as file:
            for string in strings:
                file.write(string + '\n')
        print(f"Successfully written {len(strings)} strings to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
