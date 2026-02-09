def read_text_file(filename):
    """
    Reads the contents of a text file.
    
    Args:
        filename (str): The name (and path) of the file to read.
        
    Returns:
        str: The content of the file, or an error message.
    """
    try:
        # 'r' mode is for reading (default)
        with open(filename, 'r') as file:
            # Read the entire file content into a single string variable
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example Usage:
# Make sure you have a file named 'example.txt' in the same directory, 
# or provide the full path like 'C:/Users/YourName/Documents/example.txt'

file_path = 'example.txt' 
text_data = read_text_file(file_path)

print(f"Content successfully pulled into the code:\n---")
print(text_data)
print(f"---")

# You can now use the 'text_data' string variable in your program
word_count = len(text_data.split())
print(f"The file contains {word_count} words.")
