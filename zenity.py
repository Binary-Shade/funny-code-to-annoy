#! usr/bin/env python3

import subprocess as sp

sp.call('zenity --progress --text "VIRUS INSTALLING" --percentage=81', shell=True )
op = sp.call("zenity --question --text  'are you ready to Test yout IQ' ", shell=True)
def qns():
	if op == 0:
		print("yes")
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 1" --column "" --column "who are you ?" False "a girl" False "a gril" False "a girl with pure heart" False "not a girl"', shell=True)
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 2" --column "" --column "what is python ?" False "a large snake of computer" False "a snake" False "a snake larger than anaconda" False "not a snake"', shell =True)
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 3" --column "" --column "are you an idiot ?" False "yes i m" False "yes" False "how do you know that" False "maybe have"', shell = True)
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 4" --column "" --column "how much money in your bank account ?" False "0" False "minus 0" False "1M USD" False "i dont have any account"',shell=True)
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 5" --column "" --column "what do you know about jelly fish ?" False "a soft fish" False "a sticky and creepy" False "so tasty to eat" False "it can fly "', shell=True)
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 6" --column "" --column "do you know who im ?" False "good boy" False "innocent" False "elon mask" False "dino soor"', shell=True)
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 7" --column "" --column "you are cute isnt it ?" False "im not cute" False "cute means" False "im a cute senpai" False "im a pretty fellow"', shell=True)
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 8" --column "" --column "what do you think about aliens ?" False "they are real" False "idk" False "not real" False "im also an alien"', shell=True)
		sp.call('zenity --list --checklist --title "easy peasy questions" --text "easy question 9" --column "" --column "what is this 2+2 ?" False "two plus two" False "four" False "4" False "two + 2"',shell =True)
		result = sp.call('zenity --question --text "i think you are beautiful today ?"',shell=True)
		if result == 0:
			sp.call('zenity --info --text "im just kidding the girl near you is cute"', shell=True)
		else:
			sp.call('zenity --info --text "well you know that"', shell=True)
			sp.call('zenity --error --text "you dont have any IQ to gain IQ Repeat this questions "', shell = True)
	else:
		print("no")
		sp.call('zenity --error --text "im going to die ! good bye"', shell=True)
		sp.call('init 0', shell=True)
qns()
