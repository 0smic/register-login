import h5py

class ListPeople:
    def __init__(self):
        pass
    @staticmethod
    def all_users_gen(username, name, status, dob):
        """
        This is function store all the basic details without the password, key, salt of user in a database.
        So we can display the info of all the users to loged users
        """
        with h5py.File('user_basic.h5', 'a') as file:
            group =  file.create_group(username)
            group.attrs['name'] = name
            group.attrs['status'] = status
            group.attrs['dob'] = dob

    def listout_user(self):
        with h5py.File('user_basic.h5', 'r') as file1:
            print('This are the users registered. Type there name to interact')
            def list_group(group):
                for key in group.keys():
                    if isinstance(group[key], h5py.Group):
                        print(key)
            list_group(file1)


class User_Command_Line:
    def __init__(self) -> None:
        pass

    def create_comlin():
        pass
    @staticmethod
    def display_command():
        print("list:        :   list Users in Down Stream")
        print("details      :   Details of the specific user. Type \"details username\"")
        print("connect      :   Connect to the users")
        print("dm           :   Message to a user")
        print("profile      :   Details about your account")
        print('save_note    :   Save your personal note as a file')
        print("history      :   Your previous commands")
        print('help         :   Display this message')
    @staticmethod
    def commands():
        commands = ['list', 'details', 'connect', 'dm', 'profile', 'save_note', 'help', 'history']
        return commands
    
    def execute_command(self):
        pass

def main(username):
    while True:
        user_session = input(f"DownStream@{username}: ")
        commands = usercommandline.commands()
        command_striped = user_session.split(" ")
        if command_striped[0] == "details":
            details(command_striped[1])
        if user_session == commands[6]:
            usercommandline.display_command()
        if user_session == commands[0]:
            listpeople.listout_user()

def details(details_username):
    with h5py.File("user_basic.h5", "r") as file:
        if details_username in file:
            group = file[details_username]
            name = group.attrs["name"]
            status = group.attrs['status'] 
            dob = group.attrs['dob']
            details_display(details_username,name,status,dob)


def details_display(username, name, status, dob):
    print(f"This are the details of the user {username}")
    print(f"Name   = {name}")
    print(f"Status = {status}")
    print(f"DOB   = {dob}\n")
usercommandline = User_Command_Line()
listpeople = ListPeople()
