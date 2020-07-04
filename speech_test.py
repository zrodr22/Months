import speech_recognition as sr

print("Beginning")

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response accordingly
    try:
        response = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response = None
        print("API unavailable")
    except sr.UnknownValueError:
        # speech was unintelligible
        response = None
        print("Unable to recognize speech")

    return response


if __name__ == "__main__":

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    listening = True

    while listening:
    
        while True:
            guess = recognize_speech_from_mic(recognizer, microphone)
            if guess:
                break

        print(guess)
        if guess == "thank you":
            listening = False

