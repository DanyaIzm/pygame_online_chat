# Онлайн чат на Pygame
Серверная и клиентская части онлайн чата.

Клиент написан на библиотеке Pygame, сервер на стандартных сокетах (socket).

----
## Использование
### Клиент:
##### Windows
```powershell
python -m venv venv;
venv\Scripts\activate;
cd .\client;
python main.py
```

##### Linux
```sh
python -m venv venv &&
source venv/Scripts/activate &&
cd ./client &&
python main.py
```

При подключении вводится IP адрес устройства, на котором запущен сервер. После этого вводится имя пользователя **_(оно не может повторяться с тем, кто уже подлючен к чату в данный момент)_**.

### Сервер
##### Windows
```powershell
cd .\server;
python main.py
```

##### Linux
```sh
cd ./server &&
python main.py
```
