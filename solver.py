def find_sets_on_table(cards):
    sets = []
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            for k in range(j+1, len(cards)):
                if is_set_on_table(cards[i], cards[j], cards[k]):
                    sets.append([cards[i], cards[j], cards[k]])
    return sets


def is_set_on_table(card1, card2, card3):
    for attribute in ['color', 'fill', 'shape', 'number']:
        if ((card1[attribute] == card2[attribute] and card2[attribute] != card3[attribute]) or
                (card1[attribute] != card2[attribute] and card2[attribute] == card3[attribute]) or
                (card1[attribute] == card3[attribute] and card2[attribute] != card3[attribute])):
            return False
    return True


cards = []
while True:
    input_string = input("Enter the attributes for the card (color, fill, shape, number), separated by spaces, or 'done' to finish: ")
    if input_string == 'done':
        break
    components = input_string.split()
    card = {'color': None, 'fill': None, 'shape': None, 'number': None}
    for component in components:
        if component in ['r', 'g', 'b']:
            card['color'] = component
        elif component in ['v', 'h', 'l']:
            card['fill'] = component
        elif component in ['q', 'k', 'w']:
            card['shape'] = component
        elif component.isdigit():
            card['number'] = int(component)
    cards.append(card)

farben = {'r': 'rot', 'g': 'grün', 'b': 'blau'}
fuellungen = {'h': 'halb', 'v': 'voll', 'l': 'leer'}
formen = {'k': 'Kreis', 'q': 'Quadrat', 'w': 'Welle'}

sets = find_sets_on_table(cards)
print("Mögliche Sets:\n")
for s in sets:
    for card in s:
        farbe = farben[card['color']]
        fuellung = fuellungen[card['fill']]
        form = formen[card['shape']]
        nummer = card['number']
        print(f"{farbe} {fuellung} {form} {nummer}")
    print()
