from testes import hora_agora
from time import sleep
import os


current_path = os.getcwd()
path_to_sound = os.path.join(current_path, "audio_alarm.wav")


quando_ativar = input("""Quando deseja ativar o alarme?
Exemplo do formato => 18:00

> """)

if len(quando_ativar) < 5:
    quando_ativar1 = quando_ativar[0:2]
    quando_ativar2 = quando_ativar[2:4]
    quando_ativar = f'{quando_ativar1}:{quando_ativar2}'
elif len(quando_ativar) > 5:
    quando_ativar = input("""Quando deseja ativar o alarme?
    Exemplo do formato => 18:00

    > """)


while True:
    if hora_agora() == quando_ativar:
        os.startfile(path_to_sound)
        print("Done!")
        break
    else:
        print(f"Ainda são {hora_agora()}, previsto para {quando_ativar}")
        sleep(5)
        continue
