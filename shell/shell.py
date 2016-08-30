# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-08-25 00:02:23
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-08-29 13:21:24

import os
import textwrap
import readline
import colorama
import sys
import socket
import subprocess

from colors.colors import *
from save_engine.save_engine import SaveEngineClass
from lessons.lesson_book import LessonBookClass

class TrainingWheelsShellClass():

	def __init__( self ):


		self.SaveEngine = SaveEngineClass( parent = self )
		self.LessonBook = LessonBookClass( parent = self )


		self.using_time = False
		self.time_on = False

		self.entered_input = ""

		self.commands = {
			"@help" 		: 		self.do_help,		
			"@lessons" 		:	 	self.LessonBook.select_lesson,
			"@concepts" 	:	 	self.LessonBook.select_concept,
		}

		self.special_cases = {
			"quit": self.say_goodbye,	}


	def do_help( self ):

		print \
		textwrap.dedent('''

	@help:		View this help message.
	@lessons:	Select from a menu of lessons what to study from.
	@concepts:	Choose a concept from the lesson that you are on.

	TO ADD: @setspeed

		''' )


	def error( self, e ):
		print colorama.Back.BLACK + R("Oh no! I hit an error!")
		print r("\n" + str(e.__repr__())), colorama.Back.RESET
		print r("\n" + e.child_traceback), colorama.Back.RESET



	def prompt( self ):

		if ( self.LessonBook.using_time and self.LessonBook.time_on ):
			self.LessonBook.time_on = False


		ps1 = "".join([	colorama.Fore.GREEN, colorama.Style.BRIGHT, 
						os.environ['USER'], '@', socket.gethostname(), 
						colorama.Fore.BLUE,
						" ", os.getcwd(), " $ ", 
						colorama.Style.NORMAL, colorama.Fore.RESET,
					  ]).replace( os.environ["HOME"], "~" )
		


		self.entered_input = raw_input(  ps1 ).strip()
		readline.add_history( self.entered_input )

	def say_goodbye( self ):

		print C("\n\nGoodbye!") 
		print B("_" * 78 + "\n")
		exit()



	def process( self ):

		
		if self.entered_input == "": return
		if self.entered_input in self.special_cases.iterkeys():
			# Run the corresponding function that follows the 
			self.special_cases[self.entered_input]()
			return True
		if self.entered_input in self.commands.iterkeys():
			# Run the corresponding function that follows the 
			self.commands[self.entered_input]()
			return 
		


		''' If they actually entered something, treat it as a command '''
		try:
			p = subprocess.Popen(	self.entered_input.split(), 
									stdout = subprocess.PIPE, 
									stdin=subprocess.PIPE
								)

			while ( p ):
				try:
					sys.stdout.write( self.LessonBook.something_to_say_inbetween )
					sys.stdout.write( p.stdout.next() )
				except StopIteration:
					break

		except OSError as e:
			print self.entered_input + ": command not found"



	def run( self ):
		''' The main loop of the program is here, creating the shell...'''


		if (not self.SaveEngine.load() ):

			self.LessonBook.select_lesson()
			self.LessonBook.select_concept()


		while ( True ):

			try:
				
				self.LessonBook.go()

			except KeyboardInterrupt:

				sys.stdout.write("^C\n")
				continue

			except Exception as e:
				self.error(e)