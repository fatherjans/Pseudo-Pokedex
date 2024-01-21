import pakuri, pakudex

def menu():
    # prints main menu
    print('\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit')

# ------------------------------PROGRAM-------------------------------------
def main():
    print('Welcome to Pakudex: Tracker Extraordinaire!')
    while True:
        # keeps looping till a valid max capacity number is entered
        cap_num = input('Enter max capacity of the Pakudex: ')
        try:
            cap_num = int(cap_num)
            if cap_num > 0:
                print(f'The Pakudex can hold {cap_num} species of Pakuri.')
                break
            else:
                # raise a value error if max cap number is not valid
                raise ValueError
        except ValueError as error:
            print('Please enter a valid size.')
    paku = pakudex.Pakudex(cap_num)     # creates a pakudex with cap_num
    
    while True:
        # loops through pakudex options
        menu()
        option = input('\nWhat would you like to do? ')
        try:
            option = int(option)
        except: 
            # if option is not a valid integer num, print the following statement and loop again
            print('Unrecognized menu selection!\n')
            continue
        
        if option == 1:
             species_name = paku.get_species_array()
             # get a string array of the species
             if species_name is None:
                 # if species_name is none, print that there's no pakuri in the pakudex, then loop again
                 print('No Pakuri in Pakudex yet!\n')
                 continue
             else:
                 # if there is pakuri in the pakudex, loop with a counter and print list
                 print('Pakuri In Pakudex: ')
                 counter = 1
                 for i in species_name:
                    print(f'{counter}. {i}')
                    counter += 1

        elif option == 2:
            species_name = input('Enter the name of the species to display: ')
            pakuri_stats = paku.get_stats(species_name)
            # get the states of the species name
            if pakuri_stats is not None:
                # if pakuri_stats returns an interger list, print stats
                print(f'\nSpecies: {species_name}\nAttack: {pakuri_stats[0]}\nDefense: {pakuri_stats[1]}\nSpeed: {pakuri_stats[2]}\n')
            else:
                # print error if no stats returned
                print(f'Error: No such Pakuri!')

        elif option == 3:
            if paku.get_size() >= paku.get_capacity():
                # if the num of pakuri in the pakudex is equal or greater than the max capacity, return that pakudex is full and loop again
                print('Error: Pakudex is full!')
                continue
            else:
                new_species = input('Enter the name of the species to add: ')
                # if max cap is not full, prompts to add species
            successful = paku.add_pakuri(new_species)
            if successful:
                # checks to see if adding the pakuri was successful, if so add it and prompt message
                print(f'Pakuri species {new_species} successfully added!')
            else: 
                # if not successful, prompt pakudex already has this species
                print('Error: Pakudex already contains this species!')

        elif option == 4:
            species_name = input('Enter the name of the species to evolve: ')
            evolve = paku.evolve_species(species_name)
            # if evolve is true, then the species has evolved
            if evolve:
                print(f'{species_name} has evolved!')
            else:
                print('Error: No such Pakuri!')
        
        elif option == 5:
            # sorts pakuri and prompts message
            paku.sort_pakuri()
            print('Pakuri have been sorted!')

        elif option == 6:
            # exits loop and program
            print('Thanks for using Pakudex! Bye!')
            exit()

        else: 
            # if option input not within 1-6, prompt following message
            print("Unrecognized menu selection!")
        
if __name__ == '__main__':
    main()
