def distribute(num_person, cards):
    output = []
    for i in range(num_person):
        output.append("".join([cards[j] for j in range(len(cards)) if j % num_person == i]))
    return output

def distrobute2(num_person, cards):
    output = [""] * num_person
    for i, card in enumerate(cards):
        output[i % num_person] += card
    return output

cards = distribute(num_person=4, cards="abcdefghijklm")
cards = distrobute2(num_person=4, cards="abcdefghijklm")
print(cards)
