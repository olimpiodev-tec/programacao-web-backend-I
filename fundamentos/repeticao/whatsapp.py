import webbrowser
import pyautogui
import time

nome = "Contato"
telefone = 12121212
link = f"https://web.whatsapp.com/send?phone={telefone}"
webbrowser.open(link)
time.sleep(10)
pyautogui.typewrite(f"Olá {nome}, tudo bem 😀, mensagem feita com python")
pyautogui.press('enter')

