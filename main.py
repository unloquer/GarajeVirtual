#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
from tools.tools import readtxtline , writetxt ,getAuthFile
from tools.googlemeet import gmailLogin
from telegram import Update
import re
from telegram.ext import Updater, CommandHandler, CallbackContext
TOKENPATH = "files/token.txt"
MEETPATH = "files/meetactual.txt"
AUTHPATH = "files/auth.txt"
def helpbot(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('''Comandos\n
		-\t /help \t pide ayuda 
		-\t /test \t comprueba si el bot funciona
		-\t /nueva <enlace a la nueva reunion de google meets>\t comunica una reunion a los usuarios del bot y al garaje 
		-\t /reconectar \t intetara conectarse al enlace actual
		-\t /actual \t responde si hay una reunion en este momento 
		-\t /fin \t acaba la reunion actual para permitir otras 
    	''')
def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Hola! Bienvenid@ \n si nesesitas ayuda usa el comando /help')
def test(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Probando 1 2 3...  {update.effective_user.first_name} si me escuchas funciona')
def newMeet(update: Update, context) -> None:
	meetlink = update.message.text[7:]
	writetxt(MEETPATH,meetlink)
	update.message.reply_text("conectandose a "+meetlink+" en proceso", parse_mode='Markdown')
	auth = getAuthFile(AUTHPATH)
	gmailLogin(auth[0],auth[1],meetlink)
def actualMeet(update: Update, context: CallbackContext) -> None:
	enlaceReunion = readtxtline(MEETPATH)
	if enlaceReunion == "":
		update.message.reply_text('no hay ninguna reunion ahora')
	else:
		update.message.reply_text('la reunion actual es:\n'+enlaceReunion)
def re(update: Update, _: CallbackContext) -> None:
	meetlink = readtxtline(MEETPATH)
	update.message.reply_text("re-conectandose a "+meetlink+" en proceso", parse_mode='Markdown')
	auth = getAuthFile(AUTHPATH)
	gmailLogin(auth[0],auth[1],meetlink)
def endMeet(update: Update, context: CallbackContext) -> None:
	enlaceReunion = readtxtline(MEETPATH)
	writetxt(MEETPATH,"")
	update.message.reply_text('eliminar reunion:\n'+enlaceReunion+"\nReunion eliminada")
updater = Updater(readtxtline(TOKENPATH))

updater.dispatcher.add_handler(CommandHandler('test', test))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', helpbot))
updater.dispatcher.add_handler(CommandHandler('nueva', newMeet ,pass_args=True))
updater.dispatcher.add_handler(CommandHandler("reconectar", re))
updater.dispatcher.add_handler(CommandHandler("actual", actualMeet))
updater.dispatcher.add_handler(CommandHandler("fin", endMeet))


updater.start_polling()
updater.idle()