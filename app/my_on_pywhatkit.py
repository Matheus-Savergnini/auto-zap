####essa API é a mesma do pywhatkit, apenas modelada para uso pessoal####
from time import time, sleep
import webbrowser as web
import pyautogui as pg
from extra import quote
from testes import hora_agora


def time_to_run_code(start, end):
    result = end - start
    print(result)


def send_zap_msg(destinatination, message):
    web.open(f"https://web.whatsapp.com/send?phone={destinatination}&text={quote(message)}")
    sleep(1)
    pg.press('f9')
    sleep(6)
    pg.click(900, 600, 1, button='left')
    sleep(4)
    pg.press("enter")
    sleep(1)
    pg.hotkey("ctrl", "w")


quando_ativar = '18:14'

start = time()

while True:
    if quando_ativar == hora_agora():
        send_zap_msg("+5527999109990", "Olá.\nMensagem automática, favor não responder.")
        break
    else:
        print(f'devo ativar apenas {quando_ativar}, ainda são {hora_agora()}')
        sleep(5)
        continue

end = time()

time_to_run_code(start, end)

####lista de números
#meu
#+5527999109990
##mae
#+5527999911353