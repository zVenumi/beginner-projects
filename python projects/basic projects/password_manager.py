from cryptography.fernet import Fernet
#fernet used to encrypt data

"""create a key, using fernet to generate a key, only needed to be used once so commented out after the key was generated. - file key.key
def write_key():
     key = Fernet.generate_key()
     with open("key.key", "wb") as key_file:
         key_file.write(key)
"""

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)

def view():
    with open("passwords.text", "r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            #.rstrip removes the \n so whenever it prints out a line to view the passwords it does not create another empty line.
            user, passw = data.split("|")
            #.split looks for the specific character to then return individual strings - for example, pp|painus|pizza would then become, "pp", "painus", "pizza"
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.text", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") #.encode converts a string into bytes format



while True:
    mode = input("Would you like to add a new password or view existing ones?: (view/add), press q to quit ").lower()
    if mode == "q":
        break
    
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue