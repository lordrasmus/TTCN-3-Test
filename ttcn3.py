
"""TTCN-3 Python Test Module"""

import libcwebui, json

from pprint import pprint


print("")
print("  Python TTCN-3 Test Script " )
print("")

#
#	Variablen initialisieren
#
def init():
	libcwebui.setSessionVar( "STORE_NORMAL", "value", 0 )
	libcwebui.setSessionVar( "STORE_NORMAL", "operator", 1 )
	libcwebui.setSessionVar( "STORE_NORMAL", "operand", 0 )
	libcwebui.setSessionVar( "STORE_NORMAL", "erg", "" )

	libcwebui.send( json.dumps( { "STATUS" : "OK", "VALUE": "INIT_VALUES_SET"	} ) )

#
#	Berechnung starten
#

def calc():
	operator = int( libcwebui.getSessionVar( "STORE_NORMAL", "operator" ))
	operand  = int( libcwebui.getSessionVar( "STORE_NORMAL", "operand"  ))
	value    = int( libcwebui.getSessionVar( "STORE_NORMAL", "value"    ))

	erg = None
	if operator == 1:
		erg = value + operand
	if operator == 2:
		erg = value - operand
	if operator == 3:
		erg = value / operand
	if operator == 4:
		erg = value * operand

	libcwebui.setSessionVar( "STORE_NORMAL", "erg", erg )

	libcwebui.send( json.dumps( { "STATUS" : "OK", "VALUE": "CALCULATED", "ERG": erg} ) )


#
#	AJAX Hook
#
def ttcn_3_ajax( a ):

	# action parameter lesen
	action = libcwebui.getURLParameter("action")
	if action == None:
		libcwebui.send( json.dumps( { "STATUS": "ERROR" , "VALUE": "NO_ACTION" } ) )
		return

	if action == "init":
		init()
		return

	# pruefen ob Variablen initialisiert sind
	if None == libcwebui.getSessionVar( "STORE_NORMAL", "value" ):
		libcwebui.send( json.dumps( { "STATUS": "ERROR" , "VALUE": "INIT_NOT_CALLED" } ) )
		return

	# operator setzen
	if action == "set_operator":
		libcwebui.setSessionVar( "STORE_NORMAL", "operator", libcwebui.getURLParameter("operator") )
		libcwebui.send( json.dumps( { "STATUS" : "OK", "VALUE": "OPERATOR_SET"	} ) )
		return

	# operand setzen
	if action == "set_operand":
		libcwebui.setSessionVar( "STORE_NORMAL", "operand", libcwebui.getURLParameter("operand") )
		libcwebui.send( json.dumps( { "STATUS" : "OK", "VALUE": "OPERAND_SET" } ) )
		return

	# berechnung starten
	if action == "calc":
		calc()
		return

	# letzes ergebniss als value speichern
	if action == "store":
		erg = libcwebui.getSessionVar( "STORE_NORMAL", "erg" )
		libcwebui.setSessionVar( "STORE_NORMAL", "value", erg )
		libcwebui.setSessionVar( "STORE_NORMAL", "erg", "" )

		with open("/tmp/value","w") as f:
			f.write( str( erg ) )

		libcwebui.send( json.dumps( { "STATUS" : "OK", "VALUE": "ERG_STORED_AS_VALUE", "ERG": erg} ) )
		return


	# fehlermeldung bei unbekannter action senden
	libcwebui.send( json.dumps( { "STATUS" : "ERROR", "VALUE": "UNKNOWN_ACTION" , "ACTION": action } ) )


libcwebui.set_plugin_name("TTCN-3")
libcwebui.register_function( ttcn_3_ajax )
