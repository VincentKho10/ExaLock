import os, subprocess, sys, time, winreg, pyautogui
from pylnk3 import Lnk
import pygetwindow as gw

def preventIncognito():
    key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\\Policies", 0, winreg.KEY_WRITE)
    new_key = winreg.CreateKeyEx(key, "Google\\Chrome")
    
    winreg.SetValueEx(new_key, 'IncognitoModeAvailability', 0, winreg.REG_DWORD, 1)
    return


def linkToPath(lnk):
    lnk = Lnk(lnk)
    return (lnk.path, lnk.arguments)


def stopProcess(pcs):
    subprocess.Popen('taskkill /f /im {}.exe'.format(pcs))
    return


def isChromeFullscreen():
    active_window = gw.getActiveWindow()
    screen_width, screen_height = pyautogui.size()
    window_width, window_height = active_window.size
    return (screen_width, screen_height) == (window_width, window_height) 


def isChromeUp():
    chromewd = gw.getActiveWindow().title
    if 'Google Chrome' in chromewd:
        return True
    else:
        return False


def toggleChromeFullscreen():
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
    chrome_window.activate()

    pyautogui.press("F11")


def main():
    try:
        # Path('C:/Temp').mkdir(parents=True, exist_ok=True)
        wdir = os.getcwd().replace('\\','/')
        # xmpath = createXml('gohjdfmmkmbmipfalikhmgnmdbkhecdi',wdir)
        stopProcess("chrome")
        stopProcess("explorer")
        time.sleep(3)
        path, arg = linkToPath(sys.argv[1])
        lxt = '--load-extension=\"{}\\{}\"'.format(wdir,"ExaLockExt")
        # print("{} {} {}".format(path,arg,lxt))
        # preventUninstallation(xmpath)
        preventIncognito()
        time.sleep(5)
        subprocess.Popen("{} {} {}".format(path,arg,lxt))
        
        run = True
        while run:
            time.sleep(1)
            if not isChromeFullscreen():
                toggleChromeFullscreen()
                print('chrome not in fsc')
            time.sleep(2)
            if not isChromeUp():
                stopProcess('chrome')
                stopProcess('chrome')
                run = False
        stopProcess('chrome')
            
        # subprocess.Popen("{} {}".format(path,arg))
        input('press any key...')
    except Exception as e:
        print(e)
        input('ending with error press any key...')

if "__main__" == __name__:
    main()