import os
uselessnum = 0
name=input("Please Enter Your Username:")
print("Ok, Hi " + name)
while uselessnum== 0:
    cmd=input("$" + name + ":")
    if cmd == "stop":
        break
        quit()
    elif cmd == "Stop":
        break
        quit()
    os.system(cmd)
