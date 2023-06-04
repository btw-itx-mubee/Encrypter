import os

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    except OSError as e:
        print(f"Error deleting file: {e}")

# Example usage: delete a file
file_path = 'C:/Windows/Test'  # Replace with the actual file path
delete_file(file_path)
