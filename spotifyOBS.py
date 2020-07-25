#!/usr/bin/env python3

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import keyboard
import subprocess

# Author: Jonathan Shreckengost
# Description:
#   This script was developed in order to allow me to pause/play music when switching between specific scenes in OBS.
#   This script requires the spotipy library to interact with the Spotify web API.
#   In order to use this script you must also register your app with Spotify and create a dashboard account.


# Pauses Spotify
def pauseSpotify(token1, device_id, sp1):
    try:
        results = sp1.pause_playback(device_id=device_id)
    except:
        print("Unable to find the device. Press play from the app first.")

# Plays Spotify
def playSpotify(token1, device_id, sp1):
    try:
        results = sp1.start_playback(device_id)
    except:
        print("Unable to find the device. Press play from the app first.")

# Skips to next track
def nextTrack(token1, device_id, sp1):
    try:
        results = sp1.next_track(device_id)
    except:
        print("Unable to find the device. Press play from the app first.")

# Plays previous track
def previousTrack(token1, device_id, sp1):
    try:
        results = sp1.previous_track(device_id)
    except:
        print("Unable to find the device. Press play from the app first.")

# Checks and returns the current player status
def checkPlayerStatus(token2, sp2):
    try:
        results = sp2.currently_playing(market='US')

        return results['is_playing']
    except:
        return False

def main():
    newToken = 0

    subprocess.Popen(['C:\\Users\\INSERTUSERHERE\\AppData\\Roaming\\Spotify\\Spotify.exe']) # Opens the Spotify app on my machine

    username = ""
    scope1 = "user-modify-playback-state"
    scope2 = "user-read-currently-playing"
    client_id = ""
    client_secret = ""
    redirect_uri = "http://localhost:8888/callback/"

    device_id = ""

    # Token that uses the user-modify-playback-state scope required in altering player state
    token1 = util.prompt_for_user_token(
        username = username,
        scope = scope1,
        client_id = client_id,
        client_secret = client_secret,
        redirect_uri = redirect_uri)

    # Token that uses the user-read-currently-playing scope required in checking player status
    token2 = util.prompt_for_user_token(
        username = username,
        scope = scope2,
        client_id = client_id,
        client_secret = client_secret,
        redirect_uri = redirect_uri)

    sp1 = spotipy.Spotify(auth=token1)
    sp2 = spotipy.Spotify(auth=token2)

    # Loop containing custom keybindings to pause and play the spotify app
    # I've matched these to my scene keybinds in OBS and added a couple of extras
    # Edit the keybinds to your liking
    while True:
        if keyboard.is_pressed("Ctrl + alt + ["):
            # Previous Track
            if checkPlayerStatus(token2, sp2):
                previousTrack(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + alt + ]"):
            # Next Track
            if checkPlayerStatus(token2, sp2):
                nextTrack(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + alt + n"):
            # Pause
            if checkPlayerStatus(token2, sp2):
                pauseSpotify(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + alt + m"):
            # Play
            if not checkPlayerStatus(token2, sp2):
                playSpotify(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + F1"):
            # Play
            if not checkPlayerStatus(token2, sp2):
                playSpotify(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + F2"):
            # Pause
            if checkPlayerStatus(token2, sp2):
                pauseSpotify(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + F3"):
            # Pause
            if checkPlayerStatus(token2, sp2):
                pauseSpotify(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + F4"):
            #Play
            if not checkPlayerStatus(token2, sp2):
                playSpotify(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + F5"):
            #Play
            if not checkPlayerStatus(token2, sp2):
                playSpotify(token1, device_id, sp1)
        elif keyboard.is_pressed("Ctrl + F11"):
            newToken = 1
            break
        elif keyboard.is_pressed("Ctrl + alt + /"): # Ends the program
            print("Goodbye")
            break
            
    # Prevents multiple loops from running when refreshing for new token
    if newToken == 1:
        main()

if __name__ == '__main__':
    main()