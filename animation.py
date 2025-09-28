import subprocess
import time
import platform
import subprocess
import config
# States
state = config.state
playsound = state.get("playsound", 'True')
timevar = 0.1
green = "\033[92m"
reset = "\033[0m"
quickanimation = state.get("quickanimation", 'False')
user = state['user']

# Theme importer (Chatgpt wrote it, uses json states)
import json

with open("theme.json", "r") as f:
    theme = json.load(f)

RAINBOW = list(theme["colors"].values())
RESET = theme["reset"]



# ChatGPT Theme loader python function (Don't touch)

def rainbow_print(ascii_art: str):
    lines = ascii_art.strip("\n").split("\n")
    for i, line in enumerate(lines):
        color = RAINBOW[i % len(RAINBOW)]
        print(color + line + RESET)


# Rest of the code i wrote
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

if quickanimation == 'True':
        subprocess.run('clear', shell=True, text=True)
        rainbow_print("""
        888                                  888            \x1b]8;;http://lachadev.github.io\x1b\\lachadev.github.io\x1b]8;;\x1b\\      
        888                                  888                         
        888                                  888                         
 .d8888b88888b.  8888b. 88888b.d88b.  .d88b. 888 .d88b.  .d88b. 88888b.  
d88P"   888 "88b    "88b888 "888 "88bd8P  Y8b888d8P  Y8bd88""88b888 "88b 
888     888  888.d888888888  888  8888888888888888888888888  888888  888 
Y88b.   888  888888  888888  888  888Y8b.    888Y8b.    Y88..88P888  888 
 "Y8888P888  888"Y888888888  888  888 "Y8888 888 "Y8888  "Y88P" 888  888
              
                           
                """)
        if playsound == 'True':
                play_sound("assets/sounds/sound.wav")
                exit()
        else:
                print('')
        rainbow_print("""
                           
                             
                             
 .d8888b
d88P"   
888     
Y88b.   
 "Y8888P
              
made with ❤️ by lachameleon
	  """)
time.sleep(timevar)
subprocess.run('clear', text=True)
rainbow_print("""
        888                                                                                    
        888                                                        
        888                                                     
 .d8888b88888b. 
d88P"   888 "88b
888     888  888
Y88b.   888  888
 "Y8888P888  888
      
made with ❤️ by lachameleon      
	  """)
time.sleep(timevar)
subprocess.run('clear', text=True)
rainbow_print("""
        888                                                                  
        888                                                           
        888                                              
 .d8888b88888b.  8888b. 
d88P"   888 "88b    "88b
888     888  888.d888888
Y88b.   888  888888  888
 "Y8888P888  888"Y88888
      
made with ❤️ by lachameleon      
	  """)
time.sleep(timevar)
subprocess.run('clear', text=True)
rainbow_print("""
        888                                                                 
        888                                                        
        888                                                       
 .d8888b88888b.  8888b. 88888b.d88b. 
d88P"   888 "88b    "88b888 "888 "88b
888     888  888.d888888888  888  888
Y88b.   888  888888  888888  888  888
 "Y8888P888  888"Y888888888  888  888
      
made with ❤️ by lachameleon      
	  """)
time.sleep(timevar)
subprocess.run('clear', text=True)
rainbow_print("""
        888                                                                   
        888                                                       
        888                                                     
 .d8888b88888b.  8888b. 88888b.d88b.  .d88b.  
d88P"   888 "88b    "88b888 "888 "88bd8P  Y8b
888     888  888.d888888888  888  88888888888
Y88b.   888  888888  888888  888  888Y8b.    
 "Y8888P888  888"Y888888888  888  888 "Y8888 
      
made with ❤️ by lachameleon      
	  """)
time.sleep(timevar)
subprocess.run('clear', text=True)
rainbow_print("""
        888                                  888            
        888                                  888                         
        888                                  888                         
 .d8888b88888b.  8888b. 88888b.d88b.  .d88b. 888
d88P"   888 "88b    "88b888 "888 "88bd8P  Y8b888
888     888  888.d888888888  888  88888888888888
Y88b.   888  888888  888888  888  888Y8b.    888
 "Y8888P888  888"Y888888888  888  888 "Y8888 888
      
made with ❤️ by lachameleon      
	  """)
time.sleep(timevar)
subprocess.run('clear', text=True)
rainbow_print("""
        888                                  888                      
        888                                  888                         
        888                                  888                         
 .d8888b88888b.  8888b. 88888b.d88b.  .d88b. 888 .d88b. 
d88P"   888 "88b    "88b888 "888 "88bd8P  Y8b888d8P  Y8
888     888  888.d888888888  888  888888888888888888888
Y88b.   888  888888  888888  888  888Y8b.    888Y8b.    
 "Y8888P888  888"Y888888888  888  888 "Y8888 888 "Y8888 
      
made with ❤️ by lachameleon      
	  """)
time.sleep(timevar)
subprocess.run('clear', text=True)
rainbow_print("""
        888                                  888                     
        888                                  888                         
        888                                  888                         
 .d8888b88888b.  8888b. 88888b.d88b.  .d88b. 888 .d88b.  .d88b. 
d88P"   888 "88b    "88b888 "888 "88bd8P  Y8b888d8P  Y8bd88""88b
888     888  888.d888888888  888  8888888888888888888888888  888
Y88b.   888  888888  888888  888  888Y8b.    888Y8b.    Y88..88P 
 "Y8888P888  888"Y888888888  888  888 "Y8888 888 "Y8888  "Y88P"
      
made with ❤️ by lachameleon       
	  """)
time.sleep(timevar)
subprocess.run('clear', text=True)
rainbow_print("""
        888                                  888            \x1b]8;;http://lachadev.github.io\x1b\\lachadev.github.io\x1b]8;;\x1b\\      
        888                                  888                         
        888                                  888                         
 .d8888b88888b.  8888b. 88888b.d88b.  .d88b. 888 .d88b.  .d88b. 88888b.  
d88P"   888 "88b    "88b888 "888 "88bd8P  Y8b888d8P  Y8bd88""88b888 "88b 
888     888  888.d888888888  888  8888888888888888888888888  888888  888 
Y88b.   888  888888  888888  888  888Y8b.    888Y8b.    Y88..88P888  888 
 "Y8888P888  888"Y888888888  888  888 "Y8888 888 "Y8888  "Y88P" 888  888
      
made with ❤️ by lachameleon      
	  """)

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

if playsound == 'True':
        play_sound("assets/sounds/sound.wav")
else:
     exit()
