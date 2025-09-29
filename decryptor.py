#!/usr/bin/env python3

from cryptography.fernet import Fernet
from colorama import Fore, Style

# banner
print(r"""
      
$$$$$$$\                                                     $$\                         
$$  __$$\                                                    $$ |                        
$$ |  $$ | $$$$$$\   $$$$$$$\  $$$$$$\  $$\   $$\  $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$ |  $$ |$$  __$$\ $$  _____|$$  __$$\ $$ |  $$ |$$  __$$\\_$$  _|  $$  __$$\ $$  __$$\ 
$$ |  $$ |$$$$$$$$ |$$ /      $$ |  \__|$$ |  $$ |$$ /  $$ | $$ |    $$ /  $$ |$$ |  \__|
$$ |  $$ |$$   ____|$$ |      $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |$$ |   $$ |
$$$$$$$  |\$$$$$$$\ \$$$$$$$\ $$ |      \$$$$$$$ |$$$$$$$  | \$$$$  |\$$$$$$  |$$ |      
\_______/  \_______| \_______|\__|       \____$$ |$$  ____/   \____/  \______/ \__|      
                                        $$\   $$ |$$ |                                   
                                        \$$$$$$  |$$ |                                   
                                         \______/ \__|                                                                     
      
                                                                                made by xk4libur                     
""")

try:
    key = input("Put the key: ").encode()
    cipher = Fernet(key)
    encrypted_message = input("Put the encrypted message here: ").encode()
    print("\n")
    decrypted_message = cipher.decrypt(encrypted_message)
    print(f"{Fore.LIGHTGREEN_EX}Decrypted message: {decrypted_message.decode()}{Style.RESET_ALL}")
    print("\n")

except KeyboardInterrupt:
    print(f"\n{Fore.LIGHTRED_EX}[!]Exiting...{Style.RESET_ALL}")
    exit(0)

except (ValueError, TypeError):
    print(f"{Fore.LIGHTRED_EX}Invalid key or message.{Style.RESET_ALL}")