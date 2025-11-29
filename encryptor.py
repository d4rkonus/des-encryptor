#!/usr/bin/env python3

from cryptography.fernet import Fernet
from colorama import Fore, Style  

# banner
print(r"""
      
$$$$$$$$\                                                    $$\                         
$$  _____|                                                   $$ |                        
$$ |      $$$$$$$\   $$$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$$$$\    $$  __$$\ $$  _____|$$  __$$\ $$ |  $$ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$\ 
$$  __|   $$ |  $$ |$$ /      $$ |  \__|$$ |  $$ |$$ /  $$ | $$ |    $$ /  $$ |$$ |  \__|
$$ |      $$ |  $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |      
$$$$$$$$\ $$ |  $$ |\$$$$$$$\ $$ |      \$$$$$$$ |$$$$$$$  | \$$$$  |\$$$$$$  |$$ |      
\________|\__|  \__| \_______|\__|       \____$$ |$$  ____/   \____/  \______/ \__|      
                                        $$\   $$ |$$ |                                   
                                        \$$$$$$  |$$ |                                   
                                         \______/ \__|                                     
                                                                            made by d4rkonus           
""")

try: 
    key = Fernet.generate_key() # generate the key
    cipher = Fernet(key) # create a padlock

    read = input("Give me the message to encode: ")
    print("\n")

    encode_message = cipher.encrypt(read.encode())
    print(f"{Fore.LIGHTGREEN_EX}[+] Encoded message: {encode_message.decode()}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLUE_EX}[-] Key: {key.decode()}{Style.RESET_ALL}\n")

except KeyboardInterrupt:
    print(f"\n{Fore.LIGHTRED_EX}[!] Exiting...{Style.RESET_ALL}")
    exit(0)

except (ValueError, TypeError):
    print(f"{Fore.LIGHTRED_EX}Invalid key or message.{Style.RESET_ALL}")
