import time

class Main:
    
    def start(self) -> None:
        while (True):
            print("Ejecutandose...")
            time.sleep(1)
    
main: Main = Main()

main.start()