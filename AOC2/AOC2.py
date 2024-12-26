with open(r"C:\Users\user\Desktop\AOC2024\AOC2\input2.txt", 'r') as file:
    contenu = file.read().replace('\n', ' ')
    array = [element.strip() for element in contenu.split(' ') if element.strip()]
