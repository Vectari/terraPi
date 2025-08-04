# terraPi

3. Połącz się z Raspberry Pi z VS Code:

- W VS Code kliknij ikonę Remote Explorer w lewym panelu lub otwórz paletę poleceń (Ctrl+Shift+P) i wpisz Remote-SSH: Connect to Host.

- Wybierz host raspberrypi (lub dowolną nazwę skonfigurowaną w pliku config).

- Połącz się. Jeśli to pierwsze połączenie, VS Code może poprosić o zainstalowanie serwera zdalnego na Raspberry Pi. Zgódź się na to.

____________________________________
1. source venv/bin/activate (deactivate)    --terminal I
2. python main.py    --terminal I
3. npm run dev (http://localhost:5173/)    --terminal II
4. python3 api/server.py (powinno działać na http://localhost:5000/api/temperature)    --terminal III
