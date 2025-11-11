import pickle

# Ask user for the file path
file_path = input("Enter the path to the .pkl file: ")

# Load and print the pickle file content
try:
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
        print("Contents of the pickle file:\n")
        print(data)
except FileNotFoundError:
    print("Error: File not found.")
except pickle.UnpicklingError:
    print("Error: The file could not be unpickled (it might not be a valid .pkl file).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
