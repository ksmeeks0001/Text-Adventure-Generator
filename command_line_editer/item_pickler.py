import pickle
import items

def main():
    item_types = ['Health', 'Message']
    print("Item Types")
    for i in range(0,len(item_types)):
        print(i+1, item_types[i])

    choice = 0
    while choice < 1 or choice > len(item_types):
        try:
            choice = int(input("Enter the number of item type: "))
        except:
            print("Please enter valid number")

    new_item = dict()
    new_item['name'] = input("Item name: ")
    new_item['description'] = input("description: ")
    new_item['reusable'] = input("Single use item? (0 = no, 1 = yes): ")
    if new_item['reusable'] == 0:
        new_item['reusable'] = False
    else:
        new_item['reusable'] = True

    if choice == 1:
        effect = 0
        while effect <= 0:
            try:
                effect = int(input("Effect on health: "))
            except:
                print("Must enter a valid integer health effect.")
        
        new_item['effect'] = effect

        new_item = items.HealthItem(**new_items)

    if choice == 2:
        message = ''
        while message == '':
            message = input("Enter usage message ")

        new_item['message'] = message
        
        new_item = items.MessageItem(**new_item)

    file = open('items/'+new_item.name+'.pickle','wb')
    data = pickle.dumps(new_item)
    file.write(data)
    file.close()

main()
input()
