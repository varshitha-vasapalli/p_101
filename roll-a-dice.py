import random
response = input('Would you like to roll the dice [y/n]?\n')

while response != 'n':
    if response == 'y':
        die = random.randint(1, 6)
        if die ==1:
         print("[-----]")
         print("[     ]")
         print("[  0  ]")
         print("[     ]")
         print("[-----]")
        if die ==2:
            print("[-----]")
            print("[0    ]")
            print("[     ]")
            print("[    0]")
            print("[-----]")
        if die ==3:
            print("[-----]")
            print("[0    ]")
            print("[  0  ]")
            print("[    0]")
            print("[-----]")
        if die ==4:
            print("[-----]")
            print("[ 0 0 ]")
            print("[     ]")
            print("[ 0 0 ]")
            print("[-----]")
        if die ==5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        if die ==6:
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[-----]")
        
       
        response = input('Would you like to roll the dice [y/n]?\n')
    else:
        print('Invalid response. Please type "y" or "n".')
        response = input('Would you like to roll the dice [y/n]?\n')        

print('Good-bye!')
