from email.mime import message
import pandas as pd # type: ignore
import requests

"""
This script fetches a Google Document containing character data, processes it to extract characters and their coordinates,
and writes a secret message to a text file in a grid format. The characters are placed according to their specified coordinates, 
and the output is reversed vertically to match the original document's layout.
Args:
    url (str): The URL of the Google Document containing character data.
    console (bool): Whether to print messages to the console. Default is False.

    Returns:
        None
"""
def print_secret_message(url, console=False):
    # Fetch the document content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch document. Status code: {response.status_code}")
        return
    
    content = response.content

    df = pd.read_html(content)

    # Parse the content to extract character data excluding the header row
    lines = df[0].iloc[1:,:]

    char_data = []
    
    for line in lines.iterrows():
        
        char = line[1][1]
        x = int(line[1][0])
        y = int(line[1][2])             

        # Handle if character is given as a Unicode code point (e.g., U+0041)
        if char.startswith('U+'):
            char_code = int(char[2:], 16)
            char = chr(char_code)

        char_data.append((x, y, char.upper() if char.islower() else char))

    if not char_data:
        print("No valid character found in document.")
        return
    
    # Determine grid dimensions
    max_x = max(x for x, y, _ in char_data)
    max_y = max(y for x, y, _ in char_data)
    
    # Create a grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Ensure the grid is large enough to hold all characters and fill
    for x, y, char in char_data:
        if y < len(grid) and x < len(grid[y]):
            grid[y][x] = char
    
    # Write the grid to a file in reverse order (bottom to top)
    file_name = 'secret_message.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        print_it("The secret message is:", f, console)
        for row in range(len(grid), 0, -1):
            print_it(''.join(grid[row-1]), f, console)

    print(f"Secret message has been written to '{file_name}'.")


"""
Function to print a message to the secret_message.txt file.
Args:
    message (str): The message to print.
    f (file object): The file to write the message to.
    console (bool): Whether to print the message to the console. Default is False.
Returns:
    None
"""
def print_it(message, f, console=False):
    f.write(message + '\n')
    # Print to console if required
    if console:
        print(message)



if __name__ == '__main__':
    #url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
    print_secret_message(url, console=True)

