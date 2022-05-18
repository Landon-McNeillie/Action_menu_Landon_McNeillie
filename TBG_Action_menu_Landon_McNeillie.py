#Landon
#McNeillie
#TBG Action Menu

print('Choose a direction: \nNorth \nSouth \nEast \nWest')
print('Choose an action: \nLook \nDefend \nAttack \nUse')
choice = input()

if choice == ('North'):
    print('you go North')
    
elif choice == ('South'):
    print('you go South')
    
elif choice == ('East'):
    print('you go East')
    
elif choice == ('West'):
    print('you go West')
    


elif choice == ('Look'):
    print('you look around')
    
elif choice == ('Defend'):
    print('you defend')
    
elif choice == ('Attack'):
    print('you attack')
    
elif choice == ('Use'):
    print('What do you want to use?')
    print('Inventory: Bandages, Axe, Rope')
    item = input('choose and item to use')
    if item == ('Bandages'):
        print('you gain +5 HP')
    elif item == ('Axe'):
        print('you equip the axe and gain + 5 DMG')
    elif item == ('Rope'):
        print('you have rope')
    else:
        print('invalid input, try using a capital')
        
else:
    print('invalid input, try using a capital')