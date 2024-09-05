import _datetime
from bs4 import BeautifulSoup
import requests
from Talk import Talk

class Greeting:

    def __init__(self):
        self.__days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.__months = ["January", "Februry", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        self.__tts = Talk()


    def get_weather(self):
        city = "chandigarh+weather"
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=self.__headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        self.__weather = soup.select('#wob_dc')[0].getText().strip()
        self.__temp = soup.select('#wob_tm')[0].getText().strip() + "°C"
        return self.__temp, self.__weather

    def getHour(self):
        self.__hour = str(_datetime.datetime.now().time().hour)
        if len(self.__hour) == 1:
            self.__hour = "0" + self.__hour
        return self.__hour

    def getMinute(self):
        self.__minute = str(_datetime.datetime.now().time().minute)
        if len(self.__minute) == 1:
            self.__minute = "0" + self.__minute
        return self.__minute

    def getSecond(self):
        self.__second = str(_datetime.datetime.now().time().second)
        if len(self.__second) == 1:
            self.__second = "0" + self.__second
        return self.__second

    def getMonth(self):
        self.__month = str(self.__months[_datetime.datetime.now().date().month - 1])
        if len(self.__month) == 1:
            self.__month = "0" + self.__month
        return self.__month

    def getDate(self):
        self.__date = str(_datetime.datetime.now().date().day)
        if len(self.__date) == 1:
            self.__date = "0" + self.__date
        return self.__date

    def getYear(self):
        self.__year = _datetime.datetime.now().date().year
        return self.__year

    def getDay(self):
        self.__day = self.__days[_datetime.datetime.now().isoweekday() - 1]
        return self.__day

    def greet(self):
        hour = self.getHour()
        minute = self.getMinute()

        date = self.getDate()
        day = self.getDay()
        month = self.getMonth()
        year = self.getYear()

        temp, weather = self.get_weather()

        if int(hour) >= 0 and int(hour) < 12:
            phase = "morning"
        elif int(hour) >= 12 and int(hour) < 18:
            phase = "afternoon"
        else:
            phase = "evening"

        self.__tts.speak("My pleasure to be here sir!")
        self.__tts.speak(f"Today is {day}, {date} {month} {year}.")
        self.__tts.speak(f"It is currently {hour}:{minute} in the {phase}.")
        self.__tts.speak(f"It will be {temp} today with {weather} weather.")
