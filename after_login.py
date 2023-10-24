import h5py

class ListPeople:
    def __init__(self):
        pass
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

    def create_comlin():
        pass

    def display_command():
        print("list:        :   list Users in Down Stream")
        print("details      :   Details of the specific user")
        print("connect      :   Connect to the users")
        print("dm           :   Message to a user")
        print("profile      :   Details about your account")
        print('save_note    :   Save your personal note as a file')
        print('help         :   Display this message')
    def commands():
        commands = ['list', 'details', 'connect', 'dm', 'profile', 'save_note', 'help']
        return commands
    def execute_command(self):

        pass


def main(username):
    while True:
        user_session = input(f"DownStream@{username}: ")
        commands = usercommandline.commands()
        if user_session == commands[6]:
            usercommandline.display_command()


usercommandline = User_Command_Line()
listpeople = ListPeople()
