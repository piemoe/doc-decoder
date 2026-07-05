import requests
from bs4 import BeautifulSoup

# Turn the table into an array? Do I need to sort it?
def table_maker(message_url):
    response = requests.get(message_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    table_array = []

    if table:
        for row in table.find_all('tr'):
            row_data = []
            
            for cell in row.find_all('td'):
                row_data.append(cell.get_text(strip=True))
            
            table_array.append(row_data)
    
    return table_array


# Print from the array
def crypto_sorter(crypto):
    # sort table first, save some resources
    header = crypto[0]
    body = crypto[1:]
    body.sort(key=lambda x: x[0])
    sorted_crypto = [header] + body
    
    return sorted_crypto

def message_printer(intake):
    intake = intake[1:]     # shave the header
    max_x = max(int(item[0]) for item in intake)
    max_y = max(int(item[2]) for item in intake)
    
    print_map = {(int(item[0]), int(item[2])): item[1] for item in intake}
    
    for y in range(0, max_y + 1):
        row = []
        for x in range(0, max_x + 1):
            char = print_map.get((x, y), " ")
            row.append(char)
        print("".join(row))

def main():
    # hypothetically, could have a line for user input to take in a url here.
    table = table_maker("https://docs.google.com/document/d/e/2PACX-1vQiVT_Jj04V35C-YRzvoqyEYYzdXHcRyMUZCVQRYCu6gQJX7hbNhJ5eFCMuoX47cAsDW2ZBYppUQITr/pub")
    # sorted_table = crypto_sorter(table)
    
    message_printer(table)

if __name__ == '__main__':
    main()
