import os
import click

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
        for line in reversed(list(open(home_directory + "/.bash_history"))):
            if command_tracker == count:
                print(f"you have more than {command_tracker} commands, continue?")
                break
            print(line.rstrip())
            command_tracker = command_tracker + 1
    else:
        for line in list(open(home_directory + "/.bash_history")):
            if command_tracker == count:
                print(f"you have more than {command_tracker} commands, continue?")
                break
            print(line.rstrip())
            command_tracker = command_tracker + 1


@click.command(name='save', help="Save a specific command for further use")
@click.argument('command')
def save(command):
    if (command):
        home_directory = os.path.expanduser('~')
        with open(home_directory + "\custom_history.txt", 'w') as f:
            f.write(command)
            f.close()
            print(f'Saved {command}!')
    else:
        print("Please provide an argument!")
        
frap.add_command(history)
frap.add_command(save)