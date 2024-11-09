import getpass
import string
import os
import time

# creating list of user, their PINs and bank statements
user_list = ["ansari","abdul","muqtadir"]
pins = ['2002', '2005', '2009']
amount = ['100000', '200000', '300000']
count = 0
time.sleep(5)

# while loop checks existence of entered username
print("*****************************************************")
print("*                                                   *")
print("  *       welcome to SBI BANK ATM SYSTEM        *")
print("*                                                   *")
print("*****************************************************")
while True:
    input_user = input('\nENTER USER NAME: ')
    input_user = input_user.lower()
    if input_user in user_list:
        if input_user == user_list[0]:
            n = 0
        elif input_user == user_list[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('-----------------')
        print('*****************')
        print('INVALID USERNAME ')
        print('-----------------')
        print('*****************')

# comparing pin
while count < 3:
    print('-----------------')
    print('*****************')
    pin = str(getpass.getpass('PLEASE ENTER PIN:'))
    print('-----------------')
    print('*****************')
    if pin.isdigit():
        if input_user == "ansari":
            if pin == pins[0]:
                break
            else:
                count += 1
                print('-----------------')
                print('*****************')
                print('INVALID PIN')
                print('-----------------')
                print('*****************')
                print()

        if input_user == "abdul":
            if pin == pins[1]:
                break
            else:
                count += 1
                print('-----------------')
                print('*****************')
                print('INVALID PIN')
                print('-----------------')
                print('*****************')
                print()

        if input_user == "muqtadir":
            if pin == pins[2]:
                break
            else:
                count += 1
                print('-----------------')
                print('*****************')
                print('INVALID PIN')
                print('-----------------')
                print('*****************')
                print()
    else:
        print('-----------------')
        print('*****************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('-----------------')
        print('*****************')
        count += 1

# in case of a valid pin-continuing, or exiting
if count == 3:
    print('---------------------------------')
    print('*********************************')
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!YOUR CARD HAS BEEN LOCKED!!!!')
    print('---------------------------------')
    print('*********************************')
    exit()

print('---------------------------------')
print('*********************************')
print('LOGIN SUCCESSFUL, CONTINUE')
print('---------------------------------')
print('*********************************')
print()
print('---------------------------------')
print('*********************************')
print("Welcome to the ATM",str.capitalize(user_list[n]))
print('*********************************')
print('- - - - - -ATM SYSTEM- - - - - - -')



# Main menu
while True:
    # os.system('clear')
    print('---------------------------------')
    print('*********************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement_(S)  \nWithdraw_(W) \nDeposit_(D) \nTransafer__(T) \nRecipe__(R) \nPin_(P) \nNew Register__(N) \nQuit___(Q) : ').lower()
    print('---------------------------------')
    print('*********************************')
    valid_responses = ['s',  'w', 'd','t','r', 'p', 'q','n']
    response = response.lower()
    if response == 's':
        print('---------------------------------')
        print('*********************************')
        print(str.capitalize(user_list[n]), 'YOU HAVE', amount[n], 'RUPEES ON YOUR ACCOUNT.')
        print('---------------------------------')
        print('*********************************')
        
    elif response == 'w':
        print('---------------------------------')
        print('*********************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW:'))
        print('---------------------------------')
        print('*********************************')
        if cash_out % 10 != 0:
            print('---------------------------------')
            print('*********************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 10 RUPEES NOTES')
            print('---------------------------------')
            print('*********************************')
        elif cash_out > int (amount[n]):
            print('---------------------------------')
            print('*********************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('---------------------------------')
            print('*********************************')
        else:
            amount[n] = int(amount[n]) - cash_out
            print('---------------------------------')
            print('*********************************')
            print('YOUR NEW BALANCE IS:', amount[n], 'RUPEES')
            print('---------------------------------')
            print('*********************************')

    elif response == 'd':
        print()
        print('---------------------------------')
        print('*********************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO deposit: '))
        print('---------------------------------')
        print('*********************************')
        print()
        if cash_in % 10 != 0:
            print('---------------------------------')
            print('*********************************')
            print('AMOUNT YOU WANT TO deposit MUST TO MATCH 10 RUPEES NOTES')
            print('---------------------------------')
            print('*********************************')
        else:
            amount[n] = int(amount[n]) + cash_in
            print('---------------------------------')
            print('*********************************')
            print('YOUR NEW BALANCE IS:', amount[n], 'RUPEES')
            print('---------------------------------')
            print('*********************************')

    elif response == 't':
            print('---------------------------------')
            print('*********************************')
            print('User_list:',user_list)

            print('-------------------------------------------------')
            recipient = input('Enter the username of the recipient: ').lower()
            print('*************************************************')
            
            if recipient in user_list:
                    print('-----------------------------------------------------')     
                    amount_to_transfer = int(input('Enter the amount you want to transfer: '))
                    print('*****************************************************')
                    if amount_to_transfer <= int(amount[n]):
                        recipient_index = user_list.index(recipient)
                        amount[n] = int(amount[n]) - amount_to_transfer
                        amount[recipient_index] = int(amount[recipient_index]) + amount_to_transfer
                        
                        print('---------------------------------')
                        print('Transfer successful!')
                        print('*********************************')
                        
                        print('Your new balance:', amount[n], 'Rupees')
                    else:
                        print('---------------------------------')
                        print('Insufficient balance to transfer.')
                        print('*********************************')
            else:
                print('Recipient username does not exist.')

    elif response == 'r':
        print('---------------------------------')
        print('*********************************')
        print("*******  Recipe   *******")
        print('---------------------------------')
        print('*********************************')
    
    elif response == 'p':
        print('---------------------------------')
        print('*********************************')
        new_pin = str(getpass.getpass('ENTER A NEW PIN:'))
        print('---------------------------------')
        print('*********************************')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('---------------------------------')
            print('*********************************')
            new_ppin = str(getpass.getpass('CONFIRM NEW PIN:'))
            print('---------------------------------')
            print('*********************************')
            if new_ppin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('------------')
                print('************')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('---------------------------------')
            print('*********************************')
            print('  NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('---------------------------------')
            print('*********************************')
    
    elif response == 'n':
        new_user = input('Enter the username of the new user: ').lower()
        if new_user in user_list:
            
            print('*********************************')
            print('User already exists!')
            print('*********************************')
        else:
            new_pin = input('Enter the PIN for the new user (4 digits): ')
            if new_pin.isdigit() and len(new_pin) == 4:
                user_list.append(new_user)
                pins.append(new_pin)
                amount.append('0')  # Set initial balance to 0 for new user
                print('---------------------------------')
                print('*********************************')
                print('User registered successfully!')
                print('---------------------------------')
                print('*********************************')
            else:
                print('Invalid PIN. Please enter a 4-digit PIN.')
    
    elif response == 'q':
        print('---------------------------------')
        print('*********************************')
        print('THANK YOU FOR USING SBI BANK ATM')
        print('          HAVE A NICE DAY         ')
        print('*********************************')
        break  
    