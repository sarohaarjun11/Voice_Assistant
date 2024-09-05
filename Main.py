from Greeting import Greeting
from SystemManagement import SystemManagement
from Talk import Talk
from pystt import Speech
import pyautogui
import webbrowser

class Main(Greeting, SystemManagement, Talk, Speech):
    def _init_(self):
        super()._init_()
    __sr = Speech()

    __notebook = {}

    __query = ''
    __adjust = False
    __pause_threshold = 1

    def takeQuery(self):
        #self.__query = input("QUERY> ").lower()
        print("Listening")
        self.__query = self.__sr.getSpeech(self.__adjust, self.__pause_threshold)

    def notes(self, type):
        notebook = {}
        f = open("\\Notes\\notebook", "rb")
        notebook = f.read()
        f.close()
        heading = ""
        data = ""
        if "write" in type or "start" in type:
            heading = input("ENTER HEADING> ").lower()
            while True:
                bit = input("DATA> ")
                if data != '':
                    data += bit + '\n'
                else:
                    break
            notebook.update({heading: data})
        if "read" in type or "show" in type:
            self.speak("Notes:\n")
            for key in notebook.keys():
                self.speak(key)
            self.speak("Which note would u like to read?")
            choice = input(">").lower()
            if choice == (key for key in notebook.keys()):
                try:
                    data = notebook[choice]
                except:
                    self.speak("Could not find the requested note.")
            else:
                self.speak("Could not find the requested note.")


    def respond(self):
        if "type" in self.__query:
            query = self.__query.replace("type ", "")
            pyautogui.typewrite(query)

        elif "press" in self.__query:
            query = self.__query.replace("key press", "")
            query = self.__query.replace("keypress", "")
            query = self.__query.replace("press", "")
            pyautogui.press(query.split())

        elif "battery" in self.__query:
            self.speak("Battery percentage : " + str(self.batteryPercent()))
            self.speak("Power plugged in : " + str(self.batteryCharging()))
            self.speak("Battery time left : " + str(self.batteryTimeLeft()))

        elif "search" in self.__query:
            query = self.__query.replace("search ", "").split()
            q = ""
            for word in query:
                q += word
                if query.index(word) != len(query) -1:
                    q += '+'
            url = "https://www.google.com/search?q=" + q
            webbrowser.open(url)

        elif "turn off" == self.__query:
            self.speak("Switching off...")
            exit()

        elif "system" in self.__query:
            if "shut" in self.__query and "down" in self.__query:
                self.speak("Shutting down...")
                self.systemShutdown()
            elif "log" in self.__query and "off" in self.__query:
                self.speak("Logging off...")
                self.systemLogOff()
            elif "lock" in self.__query:
                self.speak("Locking user...")
                self.systemLock()
            elif "restart" in self.__query:
                self.speak("Restarting...")
                self.systemRestart()

        elif "empty recycle bin" in self.__query:
            self.speak("Clearing bin...")
            self.emptyBin()
            self.speak("Recycle bin is empty")

        elif "time" in self.__query:
            self.speak(f"It is currently {self.getHour()}: {self.getMinute()}")

        elif "set" in self.__query:
            if "adjust" in self.__query:
                self.speak(f"Switch Microphone Noise adjustment?")
                if self.__adjust:
                    print("Current status: (ON)")
                else:
                    print("Current status: (OFF)")

            elif "tolerance" in self.__query:
                try:
                    int(self.__query.split()[2])
                except:
                    print("Enter integer value for tolerance \nEx: set tolerance 1\n\n")
                    pass
                self.__pause_threshold = int(self.__query.split()[2])

        elif "note" in self.__query:
            self.speak("Opening notes manager")
            self.notes()


def main():
    assistant = Main()

    assistant.greet()
    while True:
        assistant.takeQuery()
        assistant.respond()



if __name__ == "__main__":
    main()