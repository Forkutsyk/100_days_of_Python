def read_data_from_file():

    with open("passwords.txt", 'r') as file:
        data = file.read().strip()
        result = []
        for line in data.split('\n'):
            # Split the line into components
            parts = [part.strip() for part in line.split('|')]
            result.append(parts)

    return result


# Read and process the data
data_dict = read_data_from_file()

# Print the resulting dictionary
for i in data_dict:
    print(i)
