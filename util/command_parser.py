# Split message into list while keeping !command    
def split_message(message):
    try:
        splitMessage = message.content.split(' ')
        return splitMessage
    except:
        print("Something went wrong during splitting")

# Remove !command from message string and return multiple elements as a list
def parse_multiple(message):
    try:
        splitMessage = message.content.split(' ')
        del splitMessage[0]
        return splitMessage
    except:
        print("Something went wrong during parsing")

# Remove !command from message string and return singular element as a string
def parse_singular(message):
    try:
        splitMessage = message.content.split(' ')[1]
        return splitMessage
    except:
        print("Something went wrong during parsing")
