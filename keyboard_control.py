import pydirectinput
import time
from constants import *
from platform_connection import *

PRESET_FOR_THREAD = None

def get_action(cmd, preset: dict):
    key = None
    cmdType = None
    controls = preset[CONTROLS]
    combos = preset[COMBO_BUTTONS]
    
    for button in controls:
        try:
            if button == 'combo_buttons':
                continue
            pressCmd = controls[button]['press']
            holdCmd = controls[button]['hold']
            if cmd == pressCmd:
                key = controls[button]['key']
                cmdType = 'press'
                break
            elif cmd == holdCmd:
                key = controls[button]['key']
                cmdType = 'hold'
                break
            else:
                continue
        except (ValueError, AttributeError):
            continue
        
    if not key:
        for combo in combos:
            pressCmd = combo['press']
            holdCmd = combo['hold']
            if cmd == pressCmd or cmd == holdCmd:
                cmdType = 'press' if cmd == pressCmd else 'hold'
                key = (combo['key1'], combo['key2'])
    
    return (key, cmdType)

def keyboard_execute_thread(controls: dict):
    print("Executing...")
    ircMessages: list[bytes] = []
    chatMessages: list[dict] = []
    while not KILL_THREADS_FLAG.is_set():
        EXECUTOR_THREAD_FLAG.wait()
        print('exe')
        if not IRC_MESSAGE_QUEUE_1.empty():
            while not IRC_MESSAGE_QUEUE_1.empty():
                ircMessages.append(IRC_MESSAGE_QUEUE_1.get())
            
        if not IRC_MESSAGE_QUEUE_OVERFLOW.empty():
            while not IRC_MESSAGE_QUEUE_OVERFLOW.empty():
                ircMessages.append(IRC_MESSAGE_QUEUE_OVERFLOW.get())
        
        if ircMessages:
            for ircMessage in ircMessages:
                chatMessages.append(TWITCH_MANAGER.extract_chat_message(ircMessage))
                ircMessages.remove(ircMessage)
        
        if chatMessages:
            for message in chatMessages:
                if message:
                    cmd = message['message']
                    key, cmdType = get_action(cmd=cmd, preset=controls)
                    print(key, cmdType)
                    if key and pydirectinput.is_valid_key(key):
                        print(key, cmdType)
                        match cmdType:
                            case 'press':
                                print("Pressing")
                                press_key(key)
                            case 'hold':
                                print("Holding")
                                hold_key(key)
                        
                    chatMessages.remove(message)



def hold_key(key: str, *, duration: int = keys.HOLD_KEY_DURATION) -> None:
    '''
    Holds down the key for a certain interval.
    
    Arguments:
           key - The key to press down
      duration - How long you want the key pressed for
    '''
    if pydirectinput.is_valid_key(key):
        pydirectinput.keyDown(key=key)
        time.sleep(duration)
        pydirectinput.keyUp(key=key)
    else:
        raise ValueError(f"{key} is not a valid key! Maybe a typo or something?")

def press_key(key: str) -> None:
    '''Simply presses and releases a key.'''
    if pydirectinput.is_valid_key(key):
        pydirectinput.keyDown(key=key)
        time.sleep(keys.PRESS_TIME_DURATION)
        pydirectinput.keyUp(key=key)
    else:
        raise ValueError(f"{key} is not a valid key! Maybe a typo or something?")

def release_key(key: str) -> None:
    '''Simply releases a key'''
    if pydirectinput.is_valid_key(key):
        pydirectinput.keyUp(key)
    else:
        raise ValueError(f"{key} is not a valid key! Maybe a typo or something?")

def press_combo_key(*, key_1: str, key_2: str) -> None:
    '''
    Press 2 buttons at the same time.
    
    Arguments:
        key_1 - One of the 2 keys.
        key_2 - The other key.
    '''
    press_key(key_1)
    press_key(key_2)

def hold_combo_key(*, key_1: str, key_2: str, duration: int = keys.HOLD_KEY_DURATION) -> None:
    '''
    Hold 2 buttons at the same time.
    
    Arguments:
        key_1 - One of the 2 keys.
        key_2 - The other key.
    '''
    hold_key(key_1, duration=duration)
    hold_key(key_2, duration=duration)




def left_click_mouse() -> None:
    pass

def move_mouse(*, axis: str, distance: int, duration: int = 3) -> None:
    '''
    Moves the mouse in the desired direction.
    
    Arguments:
           axis - The axis you want the mouse to move on (x, y, xy)
       distance - The amount you want to move the mouse.
       duration - How long you want it to take to get to the destination.
    '''
    pass