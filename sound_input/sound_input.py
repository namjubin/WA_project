import speech_recognition as sr

class Sound_listen:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        
    def listen(self):
        with self.mic as source:
            audio = self.r.listen(source)
            
        try:
            data = self.r.recognize_google(audio, language="ko")
        except:
            return False
            
        return data
    
if __name__ == "__main__":
    sound = Sound_listen()
    print(sound.listen())