def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except IOError:
        print(f"Error: Unable to read the file '{file_path}'.")
        return None


def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_path}' has been successfully updated.")
    except IOError:
        print(f"Error: Unable to write to the file '{file_path}'.")


def find_and_replace(file_path, word_to_find, replacement_word):
    content = read_file(file_path)
    if content is None:
        return

    print("\nOriginal Content:")
    print(content)
    modified_content = content.replace(word_to_find, replacement_word)

    print("\nModified Content:")
    print(modified_content)

    write_file(file_path, modified_content)

if __name__ == "__main__":
    print("Basic File Handling Program")
    file_path = input("Enter the path of the file: ")

    word_to_find = input("Enter the word to find: ")
    replacement_word = input("Enter the replacement word: ")

    find_and_replace(file_path, word_to_find, replacement_word)
