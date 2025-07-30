# secret_message

This script fetches a Google Document containing character data, processes it to extract characters and their coordinates,
and writes a secret message to a text file in a grid format. The characters are placed according to their specified coordinates, 
and the output is reversed vertically to match the original document's layout. The script has the ability to print to the console,
with the optional console parameter.  This code file uses all Python code. 

### Parameters:
    url (str): The URL of the Google Document containing character data.
    console (bool): Whether to print messages to the console. Default is True.

    Returns:
        None

### Sample Usage:
 url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
 print_secret_message(url, console=True)
