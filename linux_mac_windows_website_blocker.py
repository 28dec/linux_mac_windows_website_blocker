import platform, os

SHOW_ALL = 1
ADD_NEW = 2
REMOVE_BLOCK = 3
EXIT = 0
REDIRECT = '127.0.0.1'
if platform.system() == 'Linux' or platform.system() == 'Darwin':
    print("[*] System detected -> {}".format(platform.system()))
    hosts_path = '/etc/hosts'
    cmd_clear = 'clear'
elif platform.system() == 'Windows':
    print("[*] System detected -> {}".format(platform.system()))
    hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    cmd_clear = 'cls'

def clear():
    os.system(cmd_clear)

def ReserveChoice(choice):
    clear()
    if choice == SHOW_ALL:
        print("The followed line are all entry in hosts file:")
        with open(hosts_path, 'r+') as f:
            for line in f:
                if line[0] == '#':
                    pass
                else:
                    print(line)
    elif choice == ADD_NEW:
        EXISTED = False
        cnt = 0
        target = input("Enter website url to block: ")
        print("Adding new entry to hosts: {} -> {}".format(target, REDIRECT))
        with open(hosts_path, 'r+') as f:
            for line in f:
                if (' ' + target) in line:
                    EXISTED = True
                    if REDIRECT in line[0:10]:
                        if line[0] == '#':
                            line = line[1:]
                        elif line[0:9] == REDIRECT:
                            print("[*] Website already blocked!")
                            return
        with open(hosts_path, 'a') as f:
            if EXISTED == False:
                cnt += 1
                f.write(REDIRECT + " " + target + "\n")
        print("DONE! {} entry added!".format(cnt))
    elif choice == REMOVE_BLOCK:
        cnt = 0
        target = input("Enter the blocked-website to unblock: ")
        with open(hosts_path, 'r+') as f:
            file_content = f.readlines()
            f.seek(0)
            for line in file_content:
                if " " + target in line:
                    cnt += 1
                    print("{} detected -> {}".format(target, line))
                else:
                    f.write(line)
            f.truncate()
        print("DONE! {} entry removed!".format(cnt))
    elif choice == EXIT:
        return False
    return True
def menu():
    print("[{}] Show all entry.".format(SHOW_ALL))
    print("[{}] Add new entry (Modify the existed entry preferred!).".format(ADD_NEW))
    print("[{}] Remove block website.".format(REMOVE_BLOCK))
    print("[{}] Exit".format(EXIT))
    try:
        choice = input("Enter your choice: ")
    except:
        return True
    if len(choice) > 0:
        choice = int(choice)
        return ReserveChoice(choice)
    else:
        return True

def main():
    while True:
        if menu() == False: break
        print("\n\n\n")
    return

if __name__ == '__main__':
    main()
