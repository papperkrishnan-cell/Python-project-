import socket
import time 

def port():
    target = input("Enter the IP address: ")
    port = int(input("Enter the port: "))
    
    # socket.SOCK_STREAM എന്ന് ക്യാപിറ്റൽ ലെറ്ററിൽ വേണം
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # settimeout എന്ന് കൃത്യമായി എഴുതണം
    s.settimeout(1)
    
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        else:
            print(f"[-] Port {port} is closed")    
    except socket.error:
        print("Could not connect to server")
    finally:
        # s.closed() അല്ല, s.close() ആണ് ഉപയോഗിക്കേണ്ടത്
        s.close()

port()
