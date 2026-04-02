import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def premium_look():
    clear()
    print("\033[1;36m")
    print("   █████╗ ███████╗██╗  ██╗██╗   ██╗    ███████╗██╗██╗  ██╗")
    print("  ██╔══██╗██╔════╝██║  ██║██║   ██║    ██╔════╝██║╚██╗██╔╝")
    print("  ███████║███████╗███████║██║   ██║    █████╗  ██║ ╚███╔╝ ")
    print("  ██╔══██║╚════██║██╔══██║██║   ██║    ██╔══╝  ██║ ██╔██╗ ")
    print("  ██║  ██║███████║██║  ██║╚██████╔╝    ██║     ██║██╔╝ ██╗")
    print("  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝")
    print("\033[1;32m" + "═"*65)
    print("                 👑 PREMIUM BOT LAUNCHER 👑")
    print("               Secured & Compiled Bot Engine")
    print("═"*65 + "\033[0m\n")

def main():
    premium_look()
    
    if not os.path.exists("bot_data.txt"):
        print("\033[1;31m[!] Configuration Not Found!\033[0m\n")
        token = input("\033[1;32m[+] Enter Your Bot Token: \033[0m").strip()
        admin_id = input("\033[1;32m[+] Enter Admin Chat ID: \033[0m").strip()
        
        with open("bot_data.txt", "w") as f:
            f.write(f"{token}\n{admin_id}")
        
        print("\n\033[1;36m[✓] Details Saved Successfully!\033[0m")
        time.sleep(1)
        premium_look()
        
    print("\033[1;32m[*] Initializing Core Engine...\033[0m")
    time.sleep(1)
    
    try:
        import igashu
        igashu.start_bot()
    except ImportError:
        print("\033[1;31m\n[!] Error: 'igashu.so' file missing!\033[0m")
        print("\033[1;33mPlease make sure igashu.so is in the same folder.\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
