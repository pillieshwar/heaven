import pyttsx3

def voice_modulator(text):
    voiceEngine = pyttsx3.init()
    rate = voiceEngine.getProperty('rate')
    volume = voiceEngine.getProperty('volume')
    voice = voiceEngine.getProperty('voice')
    newVoiceRate = 120
    newVolume = 1
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    voiceEngine.setProperty('rate', newVoiceRate)
    voiceEngine.runAndWait()
    voiceEngine.setProperty('rate', 125)
    voiceEngine.setProperty('volume', newVolume)
    engine.say(text)
    engine.runAndWait()