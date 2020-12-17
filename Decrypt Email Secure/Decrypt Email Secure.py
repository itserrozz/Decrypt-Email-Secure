import time
from colorama import Fore , init , Style
init()
user=open('list.txt','r').read().splitlines()
save=open("result.txt", "a")
digital = "1 2 3 4 5 6 7 8 9 0"
def Decrypt_email_Secure():
    for user_email in user:
        username = user_email.split(":")[0]
        fusername = user_email.split(":")[0][0]
        f2username = user_email.split(":")[0][1:]
        lusername = user_email.split(":")[0][-1]
        allemail = user_email.split(":")[1]
        email = user_email.split(":")[1].split("@")[0]
        domain = user_email.split(":")[1].split("@")[1]
        femail = user_email.split(":")[1].split("@")[0][0]
        lemail = user_email.split(":")[1].split("@")[0][-1]
        if fusername == femail and lusername == lemail:
            res = f"{username}@{domain}"
            if len(allemail) == len(res):
                print(f"{username}:{username}@{domain}")
                save.write(f"{username}:{username}@{domain}\n")
        if len(username * 2) == len(email):
            print(f"{username}:{fusername}{f2username}{username}@{domain}")
            save.write(f"{username}:{fusername}{f2username}{username}@{domain}\n")
        if lusername != str(lemail):
            if lemail in digital:
                if lemail == "3":
                    if len(username) + 3 == len(email):
                        print(f"{username}:{username}123@{domain}")
                        save.write(f"{username}:{username}123@{domain}\n")
                elif lemail == "4":
                    if len(username) + 4 == len(email):
                        print(f"{username}:{username}1234@{domain}\n")
                        save.write(f"{username}:{username}1234@{domain}\n")
                elif lemail == "5":
                    if len(username) + 5 == len(email):
                        print(f"{username}:{username}12345@{domain}\n")
                        save.write(f"{username}:{username}12345@{domain}\n")
    save.close()
    input("[+] Finished Decrypted Click Enter to exit .. ")
print(Fore.RED,r'''   .------------------------------------------------. 
    | .--------------------------------------------. |
    | |              .--.                          | |
    | |             /.-. '----------.              | |
    | |             \'-' .--"--""-"-'              | |
    | |              '--'                          | |
    | |          Decrypt Email Secure              | |
    | |   =====================================    | |
    | |        [ Codded By : @404.erroz ]          | |
    | |                                            | |
    | '--------------------------------------------' |
    '------------------------------------------------' ''',)
input("[+] Click Enter To Start Tool ! ")
time.sleep(0.2)
print("[!] Starting 3",end="\r")
time.sleep(1)
print("[!] Starting 2",end="\r")
time.sleep(1)
print("[!] Starting 1",end="\r")
time.sleep(1)
print('[!] Started ..',Style.RESET_ALL)
time.sleep(0.7)
Decrypt_email_Secure()