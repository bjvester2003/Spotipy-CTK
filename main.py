import spotipy
from spotipy.oauth2 import SpotifyOAuth

import customtkinter as ctk

import json

class NailPolish(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.creds = self.loadCredentials()
        self.AuthClient = self.createAuthClient(self.creds)
        
        self.title(" ")
        
        self.resizable(False, False)
        self.grid_columnconfigure((4, 20), weight=1)
        
        self.sliderVolume = ctk.CTkSlider(self, from_=0, to=100, orientation="horizontal", command=self.setVolume)
        self.sliderVolume.grid(row=0, column=0, columnspan=3,padx=5,sticky='ew')
        self.buttonPrevious =  ctk.CTkButton(self, text="<<", width=5, height=20, command=self.playPrevious)
        self.buttonPrevious.grid(row=1,column=0,padx=5,pady=5, sticky='ew')
        self.buttonPause =  ctk.CTkButton(self, text="||", width=5, height=20, command=self.playPause)
        self.buttonPause.grid(row=1,column=1,pady=5, sticky='ew')
        self.buttonNext =  ctk.CTkButton(self, text=">>", width=5, height=20, command=self.playNext)
        self.buttonNext.grid(row=1,column=2,padx=5,pady=5, sticky='ew')
        
        self.isPaused = False
        
    def button_callback(self):
        print("button pressed")
        
    def loadCredentials(self) -> list:
        with open('credentials.json', 'r') as credFile:
            data = json.load(credFile)

        return data

    def createAuthClient(self, credentials:list) -> object:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials["client_id"],
                                                       client_secret=credentials["client_secret"],
                                                       redirect_uri=credentials["redirect_uri"],
                                                       scope="user-modify-playback-state"))

        return sp
    
    def playPrevious(self):
        self.AuthClient.previous_track()
        
    def playNext(self):
        self.AuthClient.next_track()
    
    def playPause(self):
        if self.isPaused == False :
            self.AuthClient.pause_playback()
            self.isPaused = True
        else :
            self.AuthClient.start_playback()
            self.isPaused = False
    
    def setVolume(self, volume):
        self.AuthClient.volume(int(volume))
    
if __name__ == "__main__":
    app = NailPolish()
    app.mainloop()