# should_continue = True
# if should_continue == True:  # the == true is implied (no real need to include)
#     print('Hello')

# known_people = ['Isabelle', 'Camille', 'Guillaume', 'Marie-Andree', 'Michel']
# person_input = input('Enter the person you know: ')

# if person_input in known_people:
#     print('You know {} =)'.format(person_input))
# else:
#     print('You do not know {} =('.format(person_input))

# Exercise

# Version 1


'''def who_do_you_know():
    # Ask the user for people they know
    people_input = input('Enter the names of the people you know, seperated by commas: ')
    # Split the string into a list
    people_list = people_input.split(',')
    # Remove potential spaces
    people_input_nospace = []
    for person in people_list:
        people_input_nospace.append(person.strip())

    # Return that list
    return people_list'''

# Version 2


def who_do_you_know():
    # Ask the user for people they know
    people_input = input('Enter the names of the people you know, seperated by commas: ')
    # Split the string into a list
    people_list = people_input.split(',')
    # Remove spaces
    people_input_nospace = [person.strip() for person in people_list]

    # Return that list
    return people_input_nospace


def ask_user():
    # Ask user for a name
    name_input = input('Enter the name of someone you know: ')
    # See if their name is in the list of people they know
    if name_input in who_do_you_know():
        # Print out that they know the person
        print('You know {}'.format(name_input))
    else:
        print('You do not know {}'.format(name_input))


ask_user()
