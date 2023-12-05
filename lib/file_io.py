def write_file(file_name = "swot.txt", file_content= "name"):
    with open(f'{file_name}.text', 'w') as f:
        f.write(file_content)

    pass

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)
    pass

def read_file(file_name):
    with open (f'{file_name}.txt', 'r') as f:
        file_content = f.read()
    return file_content
    pass
