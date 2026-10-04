import socket
import json
import os
import requests  # requests മോഡ്യൂൾ ഇൻപോർട്ട് ചെയ്തു

# custom Exception class ശരിയാക്കി
class WrongResult(Exception):
    def __init__(self, response):
        self.response = response
        super().__init__("Wrong request result")

# .xml എന്നതിന് പകരം .json നൽകി
filename = "data.json"

# നിലവിലുള്ള JSON ഫയൽ റീഡ് ചെയ്യുന്നു
if os.path.exists(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = {}
else:
    data = {}

def BannerGrader(ip, port, targetName):
    try:
        # socket കോൺഫിഗറേഷൻ തിരുത്തി (AF_INET, SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)  # Connection സമയം കണക്കാക്കാൻ timeout നൽകി
        s.connect((ip, port))
        
        # Requests ഉപയോഗിച്ച് ഡാറ്റ എടുക്കുന്നു
        response = requests.get("https://api.github.com")
        
        # Response status പരിശോധിച്ച് Dictionary തയ്യാറാക്കുന്നു
        if response.status_code == 200:
            file_data = {
                "target": targetName,
                "status": response.status_code,
                "message": "Success"
            }
        elif response.status_code == 300:
            file_data = {
                "target": targetName,
                "status": response.status_code,
                "message": "Redirect"
            }
        else:
            file_data = {
                "target": targetName,
                "status": response.status_code,
                "message": "Failed"
            }

        # JSON ഫയലിലേക്ക് സേവ് ചെയ്യുന്നു
        with open(filename, "w") as file:
            json.dump(file_data, file, indent=4)
            
        if response.status_code == 404:
            raise WrongResult(response)

    except socket.error as e:
        print("Could not connect to socket server:", e)
    except requests.exceptions.RequestException as e:
        print("HTTP Request Error:", e)

# ഫംഗ്ഷൻ റൺ ചെയ്യാനുള്ള ഉദാഹരണം
BannerGrader("127.0.0.1", 80, "GitHub API")
print("Saved Data:", data)
