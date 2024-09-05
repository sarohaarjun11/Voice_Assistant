import speech_recognition as sr


class Speech:
    __r = sr.Recognizer()

    def getSpeech(self, adjust, pause_threshold):
        with sr.Microphone() as source:
            if adjust:
                self.__r.adjust_for_ambient_noise(source)
            self.__r.pause_threshold = pause_threshold
            audio = self.__r.listen(source)

        try:
            print("Recognizing...")
            query = self.__r.recognize_google(audio, language="en-IN")
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

        return query
