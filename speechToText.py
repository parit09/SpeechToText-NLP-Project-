import speech_recognition as sr

def speech2Text(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        print("Transcription:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
        return "Could not understand audio"
    except sr.RequestError as e:
        print("Could not request results from Google API; {0}".format(e))
        return "Google API request failed"
