import os
import click
import questionary

@click.group()
def frap():
    '''
    A terminal commands manager
    '''
    pass

@click.command(name="history", help="Display a list of your last commands")   
@click.option('--count', default=10, help="Display the number of commands of your choice")
@click.option('--r',default=True, help="True: Display your commands from most to least recent" + "\nFalse: Display your commands from least to most recent")

def history(count, r):
    home_directory = os.path.expanduser('~')
    command_tracker = 0
    if (r):
        print("Displaying commands from most recent")
        for line in reversed(list(open(home_directory + "/.bash_history"))):
            if command_tracker == count:
                print(f"you have more than {command_tracker} commands, continue?")
                break
            command = line.rstrip()
            print(command)
            command_tracker = command_tracker + 1
    else:
        print("Displaying commands from least recent")
        for line in list(open(home_directory + "/.bash_history")):
            if command_tracker == count:
                print(f"you have more than {command_tracker} commands, continue?")
                break
            command = line.rstrip()
            print(command)
            command_tracker = command_tracker + 1


@click.command(name='save', help="Save a specific command for further use")
@click.argument('command')
def save(command):
    if (command):
        home_directory = os.path.expanduser('~')
        with open(home_directory + "\custom_history.txt", 'a') as f:
            f.write(command + "\n")
            f.close()
            print(f'Saved {command}!')
    else:
        print("Please provide an argument!")
        
@click.command(name='window', help="Display an interactive of your saved command")
def window():
    home_directory = os.path.expanduser('~')
    saved_commands = []
    for line in reversed(list(open(home_directory + "\custom_history.txt"))):
            command = line.rstrip()
            if (command):
                saved_commands.append(command)
    if (saved_commands):
        chosen_command = questionary.select("Choose saved your commands to execute:", 
                                                choices=saved_commands).ask()
        os.system(chosen_command)
    else:
        print("Empty saved commands!")

@click.command(name='clear', help="Clear all of your saved command history")
@click.option('-c', default="", help="Clear a specific command")
def clear(c):
    home_directory = os.path.expanduser('~')
    with open (home_directory + "\custom_history.txt", 'w') as f:
        if c:
            for line in (list(open(home_directory + "\custom_history.txt"))):
                if line.strip("\n") != c:
                    f.write(line)
        pass
    f.close()

frap.add_command(history)
frap.add_command(save)
frap.add_command(window)
frap.add_command(clear)