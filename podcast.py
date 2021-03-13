from audiofile import AudioFile

class Podcast(AudioFile):
    def __init__(self, ID, Name, Duration, Uploadedtime, Host, Participants):
        super().__init__(ID, Duration, Uploadedtime)
        self.Name = Name     
        self.Host = Host
        self.Participants = Participants 
