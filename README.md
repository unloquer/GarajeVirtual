# GarajeVirtual
GarajeVirtual is script for interact with a virtual meeting to linking the physical space with virtual space 
adding participation of the physical space via a telegram bot and an email account.

is to not depend on asking for a meeting with those who are there, it is a greater independence and greater participation. 

## how it works ?
user proposes a meeting with google meets  links to telegram bot with 
	
	 /nueva https://meet.google.com/xxx-xxxx-xxx
in raspberry pi in physical space (aka Un/loquer) to meet with people in there 

we use raspberry pi in the physical space like server. in server we have anydesk for remote configurations beacuse we have dificults for use ssh for internet provider reasons , and this script's to conect physical space with virtual meeting.

### what i need? (hardware)

- internet
- raspberry pi
- speeker 
- microphone
- headphone splitter
- camera (not is nessary)


### what i need? (software)

- python
- python-telegram-bot
- selenium
- google chrome
- google account
- telegram 
- bash (not is nessary)
- anydesk (not is nessary)
- crontab (not is nessary)

### install
clone repo

	 git clone https://github.com/unloquer/GarajeVirtual.git

run if you wanna install with anydesk and google chorme (google chorme  is nessary )

	bash scripts/installscript

run if you  dont need anydesk
	
	python setup.py install
# screenshots
![bot](https://wiki.unloquer.org/_media/personas/2021-05-04-210311_672x255_scrot.png)

# you can be frist to test this ;-)
