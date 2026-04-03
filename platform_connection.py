import requests
import sys
import socket
import re
import random
import time
import os
import json
import concurrent.futures
import traceback
import queue
from constants import *

# I started this using DougDoug's code, but now I think it's barely recognizable. 
# I had to get it to work within seperate threads.
# Thanks, DougDoug and Ottomated and DDark and Wituz
MAX_TIME_TO_WAIT_FOR_LOGIN = 3
YOUTUBE_FETCH_INTERVAL = 1
REGEX_PATTERN = b'^(?::(?:([^ !\r\n]+)![^ \r\n]*|[^ \r\n]*) )?([^ \r\n]+)(?: ([^:\r\n]*))?(?: :([^\r\n]*))?\r\n'
IRC_HOST = 'irc.chat.twitch.tv'
IRC_PORT = 6667
NO_NEW_MESSAGE_TIMEOUT = 5
IRC_MESSAGE_QUEUE_1 = queue.Queue(maxsize=50)
IRC_MESSAGE_QUEUE_OVERFLOW = queue.Queue(maxsize=50)

NAME = 1
COMMAND = 2
PARAMS = 3
TRAILING = 4
 
class Twitch():
    '''
    Handles the communications with Twitch.
    
    Arguments:
        channel_name - Name of the Twitch channel to connect to.
    '''
    
    def __init__(self, *, channel_name: str):
        self._regexCore = re.compile(REGEX_PATTERN, re.MULTILINE)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._loginOk = False
        self._channelName = channel_name
        self._loginTimestamp = 0
        self._partial = []
    
    def connect(self) -> None:
        '''Connect to the socket and login to Twitch'''
        print("Connecting to Twitch...")
        self._socket.connect((IRC_HOST, IRC_PORT))
        self.login()
        
    def login(self) -> None:
        '''Creates a random username to login all sneaky-like'''
        user = 'justinfan%i' % random.randint(10_000, 99_999)
        self._socket.send(('PASS asdf\r\nNICK %s\r\n' % user).encode())
        self._loginTimestamp = time.time()
        
        self._socket.settimeout(10)
        ircMessage = self._socket.recv(4096)
        matches = list(self._regexCore.finditer(ircMessage))
        for match in matches:
            command = (match.group(COMMAND) or b'').decode(errors='replace')
            if (command == '001' or command == 'JOIN') and not self._loginOk:
                bytesSent = self._socket.send((f'JOIN #{self._channelName}\r\n').encode())
                if bytesSent > 0:
                        print(f'Successfully logged in. Listening to channel: {self._channelName}')
                        self._loginOk = True
                else:
                    print("FAILED TO LOGIN")
            else:
                continue
    
    def reconnect(self, *, delay: int = 0) -> None:
        '''
        Attempt to reconnect to Twitch.
        
        Arguments:
            delay - Value of the delay between reconnect attempts
        '''
        time.sleep(delay)
        self.connect()
    
    def extract_chat_message(self, irc_message: bytes, loggin_in: bool = False) -> dict:
        '''
        Takes an IRC message and takes out what we actually want from it
        
        Arguments:
            irc_message - The IRC message to get the chat message from.
        '''
        message: dict = None
        matches = list(self._regexCore.finditer(irc_message))
        for match in matches:
            messageData = ({
                'name':     (match.group(NAME) or b'').decode(errors='replace'),
                'command':  (match.group(COMMAND) or b'').decode(errors='replace'),
                'params':   list(map(lambda p: p.decode(errors='replace'), (match.group(PARAMS) or b'').split(b' '))),
                'trailing': (match.group(TRAILING) or b'').decode(errors='replace'),
            })

        cmd = messageData['command']
        if cmd == 'PRIVMSG':
            message = {
                'username': messageData['name'],
                'message': messageData['trailing']
            }
        elif cmd == 'PING':
            self._socket.send(b'PONG :tmi.twitch.tv\r\n')
        elif cmd == 'NOTICE':
            print('Server notice:', irc_message['params'], irc_message['trailing'])
        elif cmd in IRC_CMDS_TO_IGNORE:
            pass
        else:
            print(f"Unhandled IRC message: {irc_message}")
        
        return message

    def forever_listen_irc(self) -> None:
        while True:
            try:
                ircMessage = self._socket.recv(4096)
                if ircMessage and not b'JOIN' in ircMessage:
                    if not IRC_MESSAGE_QUEUE_1.full():
                        IRC_MESSAGE_QUEUE_1.put(ircMessage)
                    elif not IRC_MESSAGE_QUEUE_OVERFLOW.full():
                        IRC_MESSAGE_QUEUE_OVERFLOW.put(ircMessage)
            except socket.timeout:
                pass



