## Multiplayer Snake Game - For Educative purposes

Here you can find **interactive multiplayer browser snage game**.

## Content
Application will consist of:
* Client
* Server for:
  * getting clinet code
  * communication with other clients in real-time
  
Each will be described better in the following.

Othen than desciption of application parts, there will be instruction how to run it in your local network.

## Cleint

Client is written in pure `HTML`, `CSS` and `JavaScript`. 
> TODO

## Server for client code

Server for client code is written in `python`.
> TODO

## Poslužitelj za komunikaciju s drugim klijentima u stvarnom vremenu

Server for real-time communication with other clients is written in `python`.
> TODO

## Running the app

### Dependencies
In order for the app to be run, it is required that you have `Python 3.*` installed.
Additionally, it is necessary to install library for `websocket` with `python` command:
```
pip install git+https://github.com/dpallot/simple-websocket-server.git
```
and to install server library `HTTP` with command:
```
pip install six
```

### Running the app
1. Connect two machines into the same local network and make sure that machine A can `ping` machine B trough IP_B address. 
    - it's enough to connect them P2P (_peer to peer_) with ethernet cable or over WiFi using ad hoc method and allow in `firewall` enable outgoing port.

2.On machine B open `index.html` with text editor and change line 31: 
 ```
var webSocketLink = "ws://localhost:8001/";
```
into
```
var webSocketLink = "ws://<IP_B>:8001/";
```
where <IP_B> is IP address of machine B which can be retreived with command `ipconfig` or `ifconfig`.
3. On machine B start the server with following command in cmd.exe:  
```
python posluzitelj.py
```
Start server for real-time communication in cmd.exe with following command:
```
python komunikacija.py
```
4. Open following address in both browsers: `<IP_B>:8000`
5. Play the video game with your friend! :video_game: :smile:
