# Python for Everybody - p. 135
# Excercise 2: Count all weekdays in lines starting with 'From' using a dict()
# Excercise 3: Do the same with mail addresses of senders

# Open the file in read-mode:
mails = open('mbox.txt', 'r')

# Create empty dictionaries to fill later:
weekdays = dict()
addresses = dict()

# Iterate over the lines in the opened file:
for line in mails:
    # Remove all line breaks by stripping the right-most character:
    line = line.rstrip()
    # Split lines starting with 'From' into a list:
    if line.startswith('From'):
        words = line.split()
        # If the list has more than two elements and the 3rd element (weekday)
        # is not in the dictionary, add it and set its value to 1:
        if len(words) > 2 and words[2] not in weekdays:
            weekdays[words[2]] = 1
        # If the weekday already exists, increment the key by 1:
        elif len(words) > 2 and words[2] in weekdays:
            weekdays[words[2]] += 1
        # Do the same with the 2nd element (mail addresses):
        if len(words) > 2 and words[1] not in addresses:
            addresses[words[1]] = 1
        elif len(words) > 2 and words[1] in addresses:
            addresses[words[1]] += 1

print(weekdays)
for key in addresses:
    print(f'{key}: {str(addresses[key])}')