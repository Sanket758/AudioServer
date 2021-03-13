from audiofile import AudioFile

class AudioBook(AudioFile):
    def __init__(self, ID, Title, Author, Narrator, Duration, Uploadedtime):
        super().__init__(ID, Duration, Uploadedtime)
        self.Title = Title     
        self.Author = Author
        self.Narrator = Narrator 
