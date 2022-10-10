import os
import click
import questionary

# Used to saved color to output to the shell
FAIL = "\033[91m"
BOLD = "\033[1m"
SUCCESS = "\033[92m"
NORMAL = "\033[0m"
HEADER = "\033[33m"
@click.group()
def frap():
    '''
    A terminal commands manager
    '''
    pass

# Add the history command
@click.command(name="history", help="Display a list of your last commands")   
@click.option('--count', default=10, help="Display the number of commands of your choice")
@click.option('--r',default=True, help="True: Display your commands from most to least recent" + "\nFalse: Display your commands from least to most recent")
@click.option('--s',default=False, help="True: Display your saved commands" + "\nFalse: Display the terminal commands")

def history(count, r, s):
    # Define variables
    home_directory = os.path.expanduser('~')
    command_tracker = 0 # used to track the number of commands displayed
    
    #Displaying history of terminal commands
    if (not s):
        # print in reversed order
        if (r):
            print(f"{HEADER}Displaying commands from most recent {NORMAL}")
            
            # read the bash commands
            for line in reversed(list(open(home_directory + "/.bash_history"))):
                if command_tracker == count:
                    print(f"you have more than {command_tracker} commands, continue?")
                    break
                command = line.rstrip()
                print(command)
                command_tracker = command_tracker + 1
        
        # print in normal order
        else:
            print(f"{HEADER}Displaying commands from least recent {NORMAL}")
            # reade the bash commands
            for line in list(open(home_directory + "/.bash_history")):
                if command_tracker == count:
                    print(f"you have more than {command_tracker} commands, continue?")
                    break
                command = line.rstrip()
                print(command)
                command_tracker = command_tracker + 1

    # Displaying saved commands
    else:
        # if in reversed order
        if (r):
            print(f"{HEADER}Displaying your saved commands from most recent{NORMAL}")
            # read the saved commands
            for line in reversed(list(open(home_directory + "/custom_history.txt"))):
                if command_tracker == count:
                    print(f"you have more than {command_tracker} commands, continue?")
                    break
                
                command = line.rstrip()
                print(command)
                command_tracker = command_tracker + 1
        
        # in the normal order
        else:
            print(f"{HEADER}Displaying your saved commands from least recent{NORMAL}")

            for line in list(open(home_directory + "/custom_history.txt")):
                if command_tracker == count:
                    print(f"you have more than {command_tracker} commands, continue?")
                    break
                
                command = line.rstrip()
                print(command)
                command_tracker = command_tracker + 1


# Add the save command
@click.command(name='save', help="Save a specific command for further use")
@click.argument('command')
def save(command):
    # if there is a command
    if (command):
        home_directory = os.path.expanduser('~')
        # open the history file to read
        with open(home_directory + "\custom_history.txt", 'a') as f:
            f.write(command + "\n")
            f.close()
            print(f'{SUCCESS}Saved {command}!')
    # if there is no command
    else:
        print(f"{FAIL}Please provide an argument!{NORMAL}")
        

#Add the window commands        
@click.command(name='window', help="Display an interactive of your saved command")
def window():
    # Define variables
    home_directory = os.path.expanduser('~')
    saved_commands = []
    
    # Append to the saved commands to display
    for line in reversed(list(open(home_directory + "\custom_history.txt"))):
            command = line.rstrip()
            if (command):
                saved_commands.append(command)
    
    # Display an interactive window of saved commands
    if (saved_commands):
        chosen_command = questionary.select("Choose saved your commands to execute:", 
                                                choices=saved_commands).ask()
        os.system(chosen_command)
    else:
        print(f"{FAIL}Empty saved commands!")


# Add the clear commands
@click.command(name='clear', help="Clear all of your saved command history")
@click.option('-c', default="", help="Clear a specific command")
def clear(c):
    # Define variables
    home_directory = os.path.expanduser('~')
    
    # Open the the saved commands file
    with open (home_directory + "\custom_history.txt", 'w') as f:
        # removing commands
        if c:
            for line in (list(open(home_directory + "\custom_history.txt"))):
                if line.strip("\n") != c:
                    f.write(line)
        pass

    f.close()

# Add the commands to use
frap.add_command(history)
frap.add_command(save)
frap.add_command(window)
frap.add_command(clear)