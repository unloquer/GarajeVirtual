# proceso

## 0 como usar Garaje Virtual
chateando con el bot de telegram de GarajeVirtual

	/help 		-pide ayuda 
	/test  		-comprueba si el bot funciona
	/nueva <enlace a la nueva reunion de google meets> comunica una reunion a los usuarios del bot y al garaje 
	/reconectar	-intetara conectarse al enlace actual
	/actual 	-responde si hay una reunion en este momento 
	/fin 		-acaba la reunion actual para permitir otras 

## 1 humano pide reunion 
la persona genera una reunion en google meets en su maquina 
la envia por el bot de telegram de garajevirtual
	
	 /nueva https://meet.google.com/xxx-xxxx-xxx
la rpi que esta en Un/loquer se conectara desde una cuenta de gmail que esta configurada en script/files/auth.txt

#### ¿para que se conecta desde Un/loquer?
para hablar con los que estan en el garaje o interactuar con el espacio

## 2 otro humano quiere acceder

	se ineta que sea notificado entregandole el link
	puede notificar en el grupo o invidual mente < no se sabe si va notificar de forma general hasta este momento no se a podido probar lo suficiente>

#### ¿como se si hay alguna reunion?

puedes usar el comando /actual 

## 3 problemas en el proceso proceso

	 no te preocupes si no funciona , preocupate si funciona ;-)
	 
#### problemas muy complejos

definicion : problemas en los que hay que ir al garaje , formatear la rpi ...
donde se acceda para arreglar de forma fisica

**la mejor opcion para arreglar este tipo de problemas**: es ir y camellarles

#### problemas no tan complejos

definicion : problemas que se pueden resolver en casa sin affectar el hardware
 
**¿que se puede hacer?**

- intentar debuguiar desde el bot de telgram con comandos como

		/help 		-pide ayuda 
		/test  		-comprueba si el bot funciona
		/reconectar	-intetara conectarse al enlace actual
		/actual 	-responde si hay una reunion en este momento 

- esperar a que vuelva a instalar 