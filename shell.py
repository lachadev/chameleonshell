# Chameleonshell by lachameleon
# lachadev.github.io

import subprocess
import os
import time
import config
import platform
import threading
import platform
import time
import os
# DO NOT DELETE
state = config.state

fav1 = state['fav1']
fav2 = state['fav2']

command = 'Woo, lachadev dc!'
noescape = False
def play_sound(path):
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    elif system == "Darwin":
        subprocess.run(["afplay", path])
    elif system == "Linux":
        subprocess.run(["aplay", path])
    else:
        raise OSError("Unsupported OS")

def clear_screen():
    subprocess.run(["clear"])

def run_animation():
    subprocess.run('python3 animation.py', shell=True, text=True)

def set_user():
    global user
    user = input('What would you like to set your user to? > ')
    state["user"] = user
    config.save(state)
    subprocess.run('clear', shell=True, text=True)
    print('User set to', user)

def toggle_playsound():
    global hasansweredplaysound
    while not hasansweredplaysound:
        ps = input('True or False? > ')
        if ps in ['True', 'False']:
            state["playsound"] = ps
            config.save(state)
            hasansweredplaysound = True
        else:
            print('Structurally incorrect. Try again. Case sensitive!!!')

def toggle_quickanimation():
    global hasanswredquickanimation
    while not hasanswredquickanimation:
        qa = input('True or False? > ')
        if qa in ['True', 'False']:
            state["quickanimation"] = qa
            config.save(state)
            hasanswredquickanimation = True
        else:
            print('Structurally incorrect. Try again. Case sensitive!!!')

def setquickcd():
    slotnumber = input('Which favourite directory would you like to set? (1 or 2) > ')
    if slotnumber == '1':
        fav1 = input('Type the path to the directory (Favourite 1) > ')
        state["fav1"] = fav1
        config.save(state)
    if slotnumber == '2':
        fav2 = input('Type the path to the directory (Favourite 2) > ')
        state["fav2"] = fav2
        config.save(state)

def set_theme():
    # This is under construction
    print('This area is under construction. Instead, you can try editing the theme manually at the theme.json file.')

def restart():
    subprocess.run('python3 animation.py', shell=True, text=True)

def run_music():
    subprocess.run('python3 music.py', shell=True, text=True)

def handle_command(cmd):
    global cwd
    parts = cmd.strip().split()
    if not parts:
        return

    if parts[0] == "cd":
        # Handle 'cd' commands
        if len(parts) == 1:
            # Just 'cd' with no argument → go home
            home_dir = os.path.expanduser("~")
            os.chdir(home_dir)
        else:
            try:
                os.chdir(os.path.expanduser(parts[1]))
            except FileNotFoundError:
                print(f"No such directory: {parts[1]}")
            except Exception as e:
                print(f"Error changing directory: {e}")
        cwd = os.getcwd()
        return

    # Existing commands
    if cmd == 'setuser':
        set_user()
    elif cmd in ['quit', 'q']:
        clear_screen()
        time.sleep(0.3)
        run_animation()
        global running
        running = False
        exit()
    elif cmd == 'hi':
        print('hi :)')
    elif cmd == 'playsound':
        toggle_playsound()
    elif cmd == 'quickanimation':
        toggle_quickanimation()
    elif cmd == 'help':
        subprocess.run('python3 help.py', shell=True, text=True)
    elif cmd == 'music':
        print('Music is disabled right now due to difficulty implementing.')
    elif cmd == 'who ate the barber':
        subprocess.run('clear', shell=True, text=True)
        print('It was your father...')
        time.sleep(1)
        subprocess.run('clear', shell=True, text=True)
    elif cmd == 'restart':
        restart()
    elif cmd == 'theme':
        set_theme()
    elif cmd == 'donut':
        subprocess.run('python3 donut.py', shell=True, text=True)
    elif cmd == 'setcd':
        setquickcd()
    elif cmd == 'cdf':
        cdchoice = input('Favourite 1 or 2? > ')
        if cdchoice == 1:
            os.chdir

    else:
        subprocess.run(cmd, shell=True, text=True)

# --- Main ---
user = state["user"]
cwd = os.getcwd()
hasansweredplaysound = False
hasanswredquickanimation = False

clear_screen()
run_animation()
print('Welcome back', user + '!')
print('Easy to use daily driver shell made for non-devs.')

# Main shell loop
while True:
    cwd = os.getcwd()
    try:
        command = input(f"\033[1;32m{user}\033[0m:\033[1;34m{cwd}\033[0m > ")
        handle_command(command)
    except KeyboardInterrupt:
        subprocess.run('python3 animation.py', shell=True, text=True)
        subprocess.run('clear', shell=True, text=True)
        print('Seeya!')
        running = False
        break
