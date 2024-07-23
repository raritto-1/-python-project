from cryptography.fernet import Fernet
def loadfile():
    file = open('key.key' , 'rb')
    key = file.read()
    file.close()
    return key

def write():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)




# write()# if you don't have any key first you have to createt one
key = loadfile()
fer = Fernet(key) 



def view():
    with open('password.txt' , 'r') as f:
        for line in f.readlines():
            data =line.rstrip()
            user , password = data.split("|")
            print("user:", user , ', password', str(fer.decrypt(password.encode())))


def add():
    name = input('Account name: ')
    pwd   = input('password: ')

    with open('password.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(pwd.encode()).decode()+ "\n")



while True:

    mode = input('would you like to add another password or view the password (view , add), press q to quit ').lower()
    if mode == 'q':
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else :
        print('invalide output')