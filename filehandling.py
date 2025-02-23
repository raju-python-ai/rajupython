import os

def find_and_replace(file_path, target_word, replacement_word):
    try:
    
        if not os.path.exists(file_path):
            raise FileNotFoundError("The specified file does not exist.")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        modified_content = content.replace(target_word, replacement_word)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print("File updated successfully!")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: Permission denied. Unable to modify the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


file_path = "sample.txt"  
target_word = "low"  
replacement_word = "high"  

find_and_replace(file_path, target_word, replacement_word)
