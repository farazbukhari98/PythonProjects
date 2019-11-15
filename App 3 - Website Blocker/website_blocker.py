#Website Blocker Program
#This program adds Reddit and Twitter to the hosts file on my computer. It will run automatically and block these two websites between the hours of 8AM and 4PM.
import time
from datetime import datetime as dt

hosts_path = "/private/etc/hosts"

redirect = "127.0.0.1"

website_list = ["www.reddit.com", "reddit.com", "www.twitter.com", "twitter.com"]

while True:
    #year, month, day, hour
    #We have hour as a fixed number.
    #We are checking the current time with two different datetime values. We are comparing the current time with 8AM and 4PM.
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 10):
        #if this is true then do this
        print("Working hours...")
        #open the hosts file and be able to read and write to it by saying "r+".
        with open(hosts_path, 'r+') as file:
            content = file.read()
            #Go through each website in the website list
            for website in website_list:
                #If the website is already in the hosts file, then do nothing(pass)
                if (website in content):
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        #opening the hosts file
        with open(hosts_path, 'r+') as file:
            #reading each line and storing it in a list labeled as content
            content = file.readline()
            #By applying the seek method, we are telling python to put the pointer at the beginning of the file, instead of the end which it defaults too.
            file.seek(0)
            #Iterating through each line in content
            for line in content:
                #If there is not any website in the line that we are looking at, look through each website in website_list and add it to the file.
                #If there is no website in the current line of the content list, then you write down that line in the host file. 
                if not any(website in line for website in website_list):
                    file.write(line)
            #The content that we had after the host file text will be deleted and then the loop will go on.
            file.truncate()
        print("Fun hours...")
    time.sleep(2)