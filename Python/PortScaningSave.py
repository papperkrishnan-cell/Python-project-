import json
import OS
import socket


filename1 = "project.json"

# JSON ഫയൽ നിലവിലുണ്ടോ എന്ന് നോക്കി ലോഡ് ചെയ്യുന്നു
if os.path.exists(filename1):
    with open(filename1, "r") as file:
        data = json.load(file)
else:
    data = {}

# User Inputs
port = int(input("Enter the port: "))
ip = input("Enter the IP address: ")
targetName = input("Enter the target name: ")

# Port Scanner Function
def function(ip, port):
    op = None
    cp = None
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] port {port} is open")
            op = {targetName: {"ip": ip, "port": port, "status": "open"}}
        else:
            print(f"[-] port {port} is closed")
            cp = {targetName: {"ip": ip, "port": port, "status": "closed"}}
    except socket.error:
        print("[-] Could not connect to server")
    finally:
        s.close()

    return op, cp  # ഇപ്പോൾ എറർ വരില്ല (ഒരു വേരിയബിൾ ഡാറ്റയും മറ്റേത് None ആയും റിട്ടേൺ ചെയ്യും)

# Unpacking
openport, closedport = function(ip, port)

# Data JSON-ലേക്ക് ചേർക്കുന്നു
if openport:
    data.update(openport)
elif closedport:
    data.update(closedport)

# JSON ഫയലിലേക്ക് സേവ് ചെയ്യുന്നു
with open(filename1, "w") as file:
    json.dump(data, file, indent=4)
