#!/usr/bin/env python3

loginfail = 0 # counter to find how many login failures there are

keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r')

keystone_file_list = keystone_file.readlines()

for z in keystone_file_list:

    if "-----] Authorization failed" in z:
        print(z)
        loginfail = loginfail + 1
        print("The offending IP address was: ", z.split('. from ')[1])
print("Total number of login fails was: ", loginfail)

