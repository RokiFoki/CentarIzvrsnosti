## Centar Izvrsnosti - Zmija

Na ovom će se mjestu nalaziti svi matierijali za **iterativnu multiplayer igru preko Web sučelja** koja će se raditi u sklopu Centra Izvrsnosti u Splitu.
sasadsdas

## Sadržaj
sa
Aplikacija se sastoji od:
* Klijenta
* Poslužitelja za:
  * dohvaćanje klijentskog koda
  * komunikaciju s drugim klijentima u stvarnom vremenu
  
i svaki će od njih biti detaljnije objašnjeni u nastavku.

Osim dijelova aplikacije biti će detaljno obješnjeno pokretanje iste na lokalnom računalu unutar lokalne mreže.

## Klijent

Klijent je napisan u običnom `HTML`-u, `CSS`-u i `JavaScript`-u. 
> TODO

## Poslužitelj za dohvaćanje klijentskog koda

Poslužitelj za dohvaćanje klijentskog koda napisan je u `python`-u.
> TODO

## Poslužitelj za komunikaciju s drugim klijentima u stvarnom vremenu

Poslužitelj za komunikaciju s drugim klijentima u stvarnom vremenu napisan je u `python`-u
> TODO

## Pokretanje

### Preduvjeti za pokretanje
Da bi se aplikacija mogla pokrenuti potrebno je imati instaliran `Python 3.*`. 
Dodatno potrebno je instalirati bibilioteku za `websocket` za `python` komandom:
```
pip install git+https://github.com/dpallot/simple-websocket-server.git
```
i instalirati biblioteku za jednostavan `HTTP` server komandom
```
pip install six
```

### Pokretanje aplikacije

1. Spojiti dva računala u istu lokalnu mrežu i osigurati da računalo A može `ping`-at računalo B preko adrese IP_B
    - dovoljno ih je spojit P2P (engl. _peer to peer_) pomoću ethernet kabela ili preko wifija-ad hoc i `firewall`-u dopustiti pristup portu

2. Na računalu B otvoriti `index.html` s uređivaćem teksta i izmijeniti liniju 31: 
	 ```
   var webSocketLink = "ws://localhost:8001/";
   ```
	 u
   ```
   var webSocketLink = "ws://<IP_B>:8001/";
   ```
	gdje je <IP_B> IP adresa računala B i može se dobiti komandom `ipconfig` ili (`ifconfig`)
3. Na računalu B pokrenuti server komandom u cmd.exe:  
	  ```
    python posluzitelj.py
    ```
	pokrenuti server za websocket u cmd.exe:
    ```
    python komunikacija.py
    ```
4. U pregledniku na oba računala upisati URL: `<IP_B>:8000`
5. Igraj :video_game: :smile:
