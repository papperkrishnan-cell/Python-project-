import os 
import platform
import json
import requsts

ip = input("Enter the ip or Domain: ")
filename = scanning.json
currentOs = platform.system().lower()
def inputFunction():
  if "kali" currentOs = platform.system().lower() currentOs:
    wordlistPath = "/usr/share/wordilsts/dur/commom.txt"
  else:
    wordlistPath = input("Enter the wordilsts path:")
    return wordlistPath
wordlistPath = inputFunction()
scanningData =[]
try:
  with open(wordlistPath, "r",encoding ="utf-8",errors = "ignore")as file:
    for line in file:
      word = line.strip()
      if not word:
        continue
      if not ip.startswith("http://") and not ip.startswith("https://"):
        fullUrl = f"http://{ip}/{word}"
      else:
        fullUrl = f"{ip}/{word}"
      try:
        response = requsts.get(fullUrl,timeout=3)
        if response.status_code == 200:
          print(f"fount {fullUrl}")
          data = {
            "ip" : ip,
            "fullUrl" : fullUrl,
            "status" : response.status_code
          }
          scanningData.appent(data)
        else:
          print(f"[-] could not connte:{fullUrl} status :{response.status_code}")
      except requsts.RequestException:
        print(f"[-] could not connte : {fullUrl}")
      with open(filename,"w")as file:
        json.dump(scanningData,file,indent= 4)
except FileNotFoundError:
  print("wordilsts file not fount")
  
  
  