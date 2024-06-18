#raspberry network scanner
#reference https://t.me/bluberry_hacking
#per qualunque domanda @g3genius su telegram

#per installare raspbian utilizzate il imager writer ufficiale sellezionando il vostro modello di scheda e il sistema operativo Raspbian OS Lite
#non dimenticarti di impostare una password e un nome utente con ssh abilitato per accedere

#PRIMA DI FARE QUALUNQUE COSA SULLA SHELL DI RASPBIAN ESEGUIRE I SEGUENTI COMANDI

# $sudo apt upgrade
# $sudo apt update
# $sudo pip3 install scapy
# $sudo apt install nmap

#creare lo script per questo tool è veramente semplice
#dovremo creare 2 file: uno che verifichi la connessione a una rete e uno che esegua l'effettiva scansione
#per testare la connessione a una rete cabmata utilizzeremo il comando ipconfig

import os

def ceckconn():
	data = os.popen("ipconfig")
	if "eth0" in data:
		return True
	else:
		return False
		
#questo script non funziona nel caso la vostra interfaccia cablata, quando connessa, prenda un nome diverso (rarissimo).
#per sistemare questo problema è sufficente cambiare il nome "eth0" con il nome corretto nel vostro ambiente linux.
#per eseguire l'altro script utilizzate la chiamata di sistema os.system("path/del/tuo/script")

def startscanscript():
	os.system("/scripts/scan.py")
	
#lo script di scansione avrà il compito di trovare gli host connessi alla rete e eseguire un port scan utilizzando nmap
#per fare la scansione utilizzeremo il protocollo ARP molto più affidabile di ICMP
#per capire di cosa si parla guarda questo video
#https://www.youtube.com/watch?v=H-rANwaumfM

from scapy import arping

def devicescan(network):
	devices = []
	data = arping(network)
	for device in data:
		devices.append(device[1].psrc)
		
#la variabile network deve essere una stringa con questa formattazione "xxx.xxx.xxx.0/24"
#nel caso tu voglia provare a raggiungere ti basterà ampliare la tua netmask
#per capire di cosa si sta parlando guarda questo video
#https://www.youtube.com/watch?v=F-VUUO7S_zw

def getnetwork(ip):
	ip = ip.split(".")
	ip.pop(-1)
	ip.append("0/24")
	ip = ".".join(ip)
	return ip
	
#per eseguire la scansione avendo la lista degli indirizzi ip sarà sufficente creare una chiamata di sistema a nmap passandogli i parametri e gli indirizzi.

from datetime import now

def startscan(devices)
	ips = ""
	for ip in devices:
		ips = ips + ip
	os.system("nmap -Sv " + ips + " > " + now.strftime("%d/%m/%Y-%H:%M:%S") + ".txt")
	
#queste erano le principali cose che potrebbero servirvi per sviluppare lo script.



#per l'esecuzione automatica dello script è necessario creare un servizio del systema operativo
#l'operazione è piuttosto semplice, basterà incollare i seguenti comandi nella shell del sistema operativo

# $touch /etc/systemd/system/scan-tool.service
# $nano /etc/systemd/system/scan-tool.service

#incollate il seguente testo facendo attenzione a non lasciare gli hashtag

	#[Unit]
	#Description=scan tool listener
	#After=network.target
	#
	#[Service]
	#Type=simple
	#User=root
	#Restart=always
	#ExecStart=/scripts/start.py
	#
	#[Install]
	#WantedBy=multi-user.target

#sostituisci la directory /scripts/start.py con il path del tuo script di avvio 
#per salvare premete ctrl + x, poi 2 volte invio

# $systemctl daemon-reload
# $systemctl enable scan-tool

#eseguendo queste operazioni il vostro script verrà eseguito automaticamente al boot di linux

# per spostare il vostro script dal pc alla vostra scheda vi consiglio di collegarlo a una rete per  potervi collegare tramite ssh e utilizzare tool come filezilla o il comando scp di windows

#AVVERTENZE

#se importi la libreria scapy prima di essere connesso a una rete riscontrerai vari errori
#la chiamata di sistema os.system aspetterà la fine dell'esecuzione del programma da te avviato mentre os.popen andrà direttamente all'istruzione successiva

#DISCLAMER
#NON MI PRENDO NESSUNA RESPONSABILITA DI CIO CHE FARETE CON QUESTA GUIDA
#RICORDATEVI SEMPRE CHE IL REATO DI INTRUSIONE IN SISTEMA INFORMATICO è PUNITO DALLA LEGGE ITALIANA CON 3 ANNI DI RECLUSIONE