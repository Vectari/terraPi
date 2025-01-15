# terraPi

3. Połącz się z Raspberry Pi z VS Code:

- W VS Code kliknij ikonę Remote Explorer w lewym panelu lub otwórz paletę poleceń (Ctrl+Shift+P) i wpisz Remote-SSH: Connect to Host.

- Wybierz host raspberrypi (lub dowolną nazwę skonfigurowaną w pliku config).

- Połącz się. Jeśli to pierwsze połączenie, VS Code może poprosić o zainstalowanie serwera zdalnego na Raspberry Pi. Zgódź się na to.

____________________________________
1. source myenv/bin/activate (deactivate)
2. pip freeze > requirements.txt 
3. pip install -r requirements.txt
4. python app.py
