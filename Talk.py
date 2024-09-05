import pyttsx3


class Talk:
    __engine = pyttsx3.init()
    __voices = [__engine.getProperty('voices'), 0]
    __rate = __engine.getProperty('rate')
    __engine.setProperty('voice', __voices[0][0].id)
    __engine.setProperty('rate', 180)


    def speak(self, text):
        print(text)
        self.__engine.say(text)
        self.__engine.runAndWait()

    def changeVoice(self, n = 1):
        if len(self.__voices[0]) >= n > 0:
            self.__engine.setProperty('voice', self.__voices[0][int(n) - 1].id)
            self.__voices[1] = n-1
            self.speak("Voice has been changed")
            return "Voice has been changed"
        else:
            self.speak("Invalid input...")
            return "Invalid input..."

    def showVoice(self):
        n = self.__voices[1]
        self.speak(f"Current Voice ID is below.")
        return f"{self.__voices[0][n].id}"

    def showRate(self):
        rate = self.__rate
        self.speak(f"Current Voice rate is {rate}")
        return f"{rate}"

    def changeRate(self, level = 5):
        if level == 1:
            level = 140
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 2:
            level = 150
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 3:
            level = 160
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 4:
            level = 170
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 5:
            level = 180
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 6:
            level = 190
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 7:
            level = 200
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 8:
            level = 210
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 9:
            level = 220
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        elif level == 10:
            level = 230
            self.__engine.setProperty('rate', level)
            self.__rate = level
            self.speak(f"Voice rate changed to {level}")
            return f"Voice rate changed to {level}"
        else:
            self.speak("Given level is out of range")
            return "Given level is out of range"


