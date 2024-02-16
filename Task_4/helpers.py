def parseInput(userInput):
    cmd, *args = userInput.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def addContact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return 'Contact added'
    else:
        return "Contact already exists"
    
def updateContact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return f"Contact with name {name} not found"
    
def findContact(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact with name {name} not found" 
    
def getAllContacts(contacts):
    if len(contacts) > 0:
        return contacts
    else:
        return "Contacts list is empty"  
  
  
  
  
