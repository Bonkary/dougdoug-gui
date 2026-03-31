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

# This is all based off of DougDoug's code. I just refactored it more to my liking.
MAX_TIME_TO_WAIT_FOR_LOGIN = 3
YOUTUBE_FETCH_INTERVAL = 1
REGEX_PATTERN = b'^(?::(?:([^ !\r\n]+)![^ \r\n]*|[^ \r\n]*) )?([^ \r\n]+)(?: ([^:\r\n]*))?(?: :([^\r\n]*))?\r\n'
HOST = 'irc.chat.twitch.tv'
PORT = 6667

class Twitch():
    '''
    Handles the communications with Twitch.
    
    Arguments:
        channel_name - Name of the Twitch channel to connect to.
    '''
    
    def __init__(self, *, channel_name: str):
        self._regexCompile = re.compile(REGEX_PATTERN, re.MULTILINE)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._loginOk = False
        self._channelName = channel_name
        self._loginTimestamp = 0
        self._partial: list = None
        
    def connect(self) -> None:
        '''Connect to the socket and login to Twitch'''
        self._socket.connect((HOST, PORT))
        self.login()
        
    def login(self) -> None:
        '''Creates a random username to login all sneaky-like'''
        user = 'justinfan%i' % random.randint(10000, 99999)
        self._socket.send(('PASS asdf\r\nNICK %s\r\n' % user).encode())
        self._socket.settimeout(1.0/60.0)
        self._loginTimestamp = time.time()
        for ircMessage in self.receive_irc_data():
            if ircMessage['command'] == '001' and not self._loginOk:
                bytesSent = self._socket.send((f'JOIN #{self._channelName}\r\n').encode())
                if bytesSent > 0:
                    print(f'Successfully logged in. Joining channel {self._channelName}')
                    self._loginOk = True
    
    def reconnect(self, *, delay: int = 0) -> None:
        '''
        Attempt to reconnect to Twitch.
        
        Arguments:
            delay - Value of the delay between reconnect attempts
        '''
        time.sleep(delay)
        self.connect()
    
    def get_messages(self) -> list[dict]:
        cmdToIgnore = ['JOIN', '001', '002', '003', '004', '375', '372', '376', '353', '366']
        privmsgs = []
        ircMessages = self.receive_irc_data()
        for ircMessage in ircMessages:
            cmd = ircMessage['command']
            if cmd == 'PRIVMSG':
                newMessage = {
                        'username': ircMessage['name'],
                        'message': ircMessage['trailing']
                    }
                if not newMessage in privmsgs:
                    privmsgs.append(newMessage)
            elif cmd == 'PING':
                self._socket.send(b'PONG :tmi.twitch.tv\r\n')
            elif cmd == 'NOTICE':
                print('Server notice:', ircMessage['params'], ircMessage['trailing'])
            elif cmd in cmdToIgnore:
                continue
            else:
                print(f"Unhandled IRC message: {ircMessage}")
        
        if not self._loginOk:
            if time.time() - self._loginTimestamp > MAX_TIME_TO_WAIT_FOR_LOGIN:
                print("no response from twitch... reconnecting")
                self.reconnect()
                privmsgs = []

        return privmsgs
    
    def receive_irc_data(self) -> list[dict]:
        buffer = b''
        received = b''
        data = []
        self._socket.settimeout(10)
        while True:
            try:
                received = self._socket.recv(4096)
                buffer += received
            except socket.timeout:
                break
            except Exception as e:
                print('Unexpected connection error. Reconnecting in a second...', e)
                self.reconnect(delay=1)
                return []
            if not received:
                print('Connection closed by Twitch. Reconnecting in 5 seconds...')
                self.reconnect(delay=5)
                return []
            buffer += received
            received = b''
        
        if buffer:
            if self._partial:
                buffer = self._partial + buffer
                self._partial.clear()
            
            matches = list(self._regexCompile.finditer(buffer))
            for match in matches:
                data.append({
                    'name':     (match.group(1) or b'').decode(errors='replace'),
                    'command':  (match.group(2) or b'').decode(errors='replace'),
                    'params':   list(map(lambda p: p.decode(errors='replace'), (match.group(3) or b'').split(b' '))),
                    'trailing': (match.group(4) or b'').decode(errors='replace'),
                })
                
            if not matches:
                self._partial += buffer
            else:
                end = matches[-1].end()
                if end < len(buffer):
                    self._partial = buffer[end:]
                
                if matches[0].start():
                    print("IDK WHAT THIS MEANS")
        
        return data
            
        
        

        
        