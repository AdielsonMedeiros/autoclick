import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

DELAY = 0.03
BUTTON = Button.left
TOGGLE_KEY = KeyCode(char='s')
EXIT_KEY = KeyCode(char='e')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = threading.Event()
        self.program_running = threading.Event()
        self.program_running.set()

    def start_clicking(self):
        self.running.set()
        print("[STATUS] AutoClicker ATIVADO.")

    def stop_clicking(self):
        self.running.clear()
        print("[STATUS] AutoClicker PAUSADO.")

    def exit(self):
        self.stop_clicking()
        self.program_running.clear()
        print("[STATUS] Encerrando programa...")

    def run(self):
        mouse = Controller()
        while self.program_running.is_set():
            while self.running.is_set():
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

def main():
    click_thread = ClickMouse(DELAY, BUTTON)
    click_thread.start()

    def on_press(key):
        if key == TOGGLE_KEY:
            if click_thread.running.is_set():
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
        elif key == EXIT_KEY:
            click_thread.exit()
            listener.stop()

    print("=========================================")
    print("      PYTHON AUTOCLICKER     ")
    print("=========================================")
    print(f"Teclas de Atalho:")
    print(f"  [{TOGGLE_KEY.char.upper()}] -> Iniciar / Parar")
    print(f"  [{EXIT_KEY.char.upper()}] -> Encerrar Programa")
    print(f"Configuração:")
    print(f"  Delay: {DELAY} seg")
    print(f"  Botão: {BUTTON.name}")
    print("-----------------------------------------")
    print("Aguardando comando...")

    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
