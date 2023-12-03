from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import requests

class MyHandler(FileSystemEventHandler):
    def __init__(self, extract_url):
        self.extract_url = extract_url
        self.processed_files = set()

    def on_created(self, event):
        if event.is_directory:
            return
        time.sleep(1)  # Attendez un peu pour permettre la fin du processus de création
        client_id = str(event.src_path).split("\\")[1].split(".")[0]
        print(f'le client numéro {client_id} a fait une nouvelle demande.')
        self.processed_files.add(event.src_path)
        print("listener.py : appelle de service d'extraction: trigger_extract_service")
        self.trigger_extract_service(client_id)

    def trigger_extract_service(self, file_name):

        extract_url = f"{self.extract_url}/extract/informations/{file_name}"

        # Utilisez requests pour envoyer une requête POST au service extract
        response = requests.post(extract_url)

        # Vérifiez la réponse si nécessaire
        if response.status_code == 200:
            print(f"Service extract déclenché avec succès pour le fichier : {file_name}")
            information_dict = response.json()
            print("Contenu du dictionnaire 'information':")
            print(information_dict)
        else:
            print(f"Erreur lors du déclenchement du service extract : {response.status_code}")



if __name__ == "__main__":
    # Remplacez l'URL par l'URL réelle de votre service extract
    extract_service_url = "http://127.0.0.1:8001"

    event_handler = MyHandler(extract_service_url)
    observer = Observer()
    observer.schedule(event_handler, path='demandes', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()