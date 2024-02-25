"""Create a dictionary of names and birthdays. When you run your program it
should ask the user to enter a name, and return the birthday of that person
back to them."""

birthday_list = {
	"Richard Stallman": ["16","03","1953"],
	"Dennis Ritchie": ["09","09","1941"],
	"Linus Torvalds": ["28","12","1969"]
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for i in birthday_list.keys():
    print(i)

def choose_bday(person):
    return birthday_list(person)

locale = input("Choose your date format (American / Normal): ")
choice = input("Whose birthday do you want to know? ")
bday = birthday_list[choice]

if locale == "American":
    print("The birthday of {} is {}/{}/{}".format(choice, bday[1], bday[0], bday[2]))
elif locale == "Normal":
    print("The birthday of {} is {}.{}.{}".format(choice, bday[0], bday[1], bday[2]))