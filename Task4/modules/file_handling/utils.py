def write_to_file(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"Successfully writen to {filename}")
    except TypeError:
        print('Please enter a string to write to a file')

def read_file(filename):
    try:
        with open(filename) as file:
            print(file.readline())
    except FileNotFoundError:
        print("The file you specified was not found!")