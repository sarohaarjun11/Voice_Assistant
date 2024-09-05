import psutil
import subprocess
import ctypes
import winshell
import ecapture.ecapture as ec
from Talk import Talk
from pycaw.pycaw import AudioUtilities ,ISimpleAudioVolume


class SystemManagement:
    __battery = psutil.sensors_battery()

    def emptyBin(self):
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)

    def systemShutdown(self):
        subprocess.call('shutdown /p /f')

    def systemRestart(self):
        subprocess.call(["shutdown", "/r"])

    def systemLock(self):
        ctypes.windll.user32.LockWorkStation()

    def systemHibernate(self):
        subprocess.call("shutdown /h")

    def systemLogOff(self):
        subprocess.call(["shutdown", "/l"])

    def capture(self):
        ec.capture(0, "fluxCam", "img.jpg")

    def batteryTimeLeft(self):
        if not self.batteryCharging():
            fTime = {"h":0, "m":0, "s":self.__battery.secsleft}
            if fTime["s"] >= 60:
                secs = fTime["s"]%60
                fTime["m"] = int((fTime["s"]-secs)/60)
                fTime["s"] = secs
            if fTime["m"] >= 60:
                mins = fTime["m"]%60
                fTime["h"] = int((fTime["m"]-mins)/60)
                fTime["m"] = mins
            if fTime["h"] >= 5:
                fTime["h"] = 5
            return f"{fTime['h']}:{fTime['m']}:{fTime['s']}"
        else:
            return "UNLIMITED"

    def batteryCharging(self):
        return self.__battery.power_plugged

    def batteryPercent(self):
        return self.__battery.percent

    def checkGeneralVolume(self):
        volume = {}
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            sVol = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and sVol.GetMasterVolume() not in volume.keys():
                volume[sVol.GetMasterVolume()] = [session.Process.name()]
            elif session.Process and sVol.GetMasterVolume() in volume.keys():
                volume[sVol.GetMasterVolume()].append(session.Process.name())

            return volume
