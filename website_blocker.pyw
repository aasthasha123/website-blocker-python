import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'    # FOR WINDOWS
redirect = "127.0.0.1"
website_list = ["www.domainname.com"]    # ADD WEBSITE YOU WANT TO BLOCK
 
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12)<dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,22):   # SPECIFY WORKING HOURS
        print("Working Hours...")
        with open(hosts_path,'r+') as file:
            content = file.read()
            
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect + " " + website)
            
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()


        print("ENJOY")
        

    time.sleep(5)
