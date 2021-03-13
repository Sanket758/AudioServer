from audiofile import AudioFile

class Song(AudioFile):
    def __init__(self, ID, Name, Duration, Uploadedtime):
        super().__init__(ID, Duration, Uploadedtime)
        self.Name = Name   
    
    def __repr__(self):
        return f'ID: {self.ID}, Name: {self.Name} Duration: {self.Duration}, Uploaded Time: {self.Uploadedtime}'
