from colorama import Fore, Style, init
import os
def titulo():
    init(autoreset=True)

    os.system("cls" if os.name == "nt" else "clear")

    titulo = f"""
    {Fore.YELLOW}███████╗██████╗░██╗░░░██╗░██████╗░
    {Fore.YELLOW}██╔════╝██╔══██╗╚██╗░██╔╝██╔════╝░
    {Fore.YELLOW}█████╗░░██████╦╝░╚████╔╝░╚█████╗░░
    {Fore.YELLOW}██╔══╝░░██╔══██╗░░╚██╔╝░░░╚═══██╗░
    {Fore.YELLOW}██║░░░░░██████╦╝░░░██║░░░██████╔╝░
    {Fore.YELLOW}╚═╝░░░░░╚═════╝░░░░╚═╝░░░╚═════╝░░
    {Style.RESET_ALL}
    """

    print(titulo)