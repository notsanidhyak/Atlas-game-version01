import time
import random
import pyfiglet

with open("countries.txt") as listofcountries:
	content=listofcountries.readlines()
content=[x.strip() for x in content]
reqlist=list(content)

banner=pyfiglet.figlet_format("              ATLAS ")

print("\033[1;36;40m_"*120)
print('\n')

print(banner)
print('''               \033[1;30;47m © S A N I D H Y A   K U M A R ''')
print('\n')
print('\033[1;36;40m_'*120)


while True:
	
	
	
	print('''
	\033[1;37;40m
◆ PRESS ( L ) TO LAUNCH NEW GAME  

◆ PRESS ( R ) FOR RATING US  

◆ PRESS ( A ) FOR ABOUT  

◆ PRESS ANY OTHER KEY TO EXIT 
''')
	print('\033[1;36;40m_'*120)
	gamestat=input(''' 
                        \033[1;32;40mENTER : ''')
            
	print('\033[1;36;40m_'*120)    

	#GAME SYSTEM
	
	if gamestat=="L" or gamestat=="l":
		#Loading
		time.sleep(0.1)
		print('''
				
       \033[1;31;40m C O N N E C T I N G   T O   D A T A B A S E \033[1;31;40m''',end="\r")
		time.sleep(1.5)
		print('''       \033[1;32;40m C O N N E C T I O N   S U C C E S S F U L L \033[1;31;40m       ''',end="\r")
		time.sleep(1.5)
		print('''               I M P O R T I N G   F I L E S              
      ''')				
		from alive_progress import alive_bar
		from time import sleep
		with alive_bar(100,bar="blocks") as bar:
			for i in range(100):
				sleep(0.05)
				bar()
		
		print('''   \033[1;32;40m
	        L A U N C H I N G   G A M E
	       ''')
				
		print('\033[1;36;40m_'*120)
		
		time.sleep(1)
		while True:
			with open ("highscore.txt") as tp:
				tp2=tp.read()
			hslist=list(tp2)
			print('''       		 
     	 	  \033[1;30;47m  H I G H S C O R E :''',max(hslist)," ")
			print('''\033[1;37;40m
• PRESS ( S ) TO START GAME

• PRESS ( I ) FOR INSTRUCTIONS

• PRESS ( P ) TO VIEW LIST OF ALL PLACES

• PRESS ( H ) TO VIEW SCORE HISTORY

• PRESS ANY OTHER KEY TO RETURN BACK TO MAIN MENU''')
			print('\033[1;36;40m_'*120)
			fr=str(input('''
                       \033[1;32;40mENTER : '''))
			print('\033[1;36;40m_'*120)
			print("\n")
			
			#MAIN GAME
			
			if fr=="s" or fr=="S":
				
							
				
				
				#Game starts
				
				templist=[]
				score=-1
				check2="b"
				check="a"
			
				
				while True:
					
					
					playerans=str(input('''\033[1;32;40mEnter your answer : \033[1;37;40m'''))
					if playerans:
						
						playerans0=str(playerans[0])
					
						if playerans0=="a" or playerans0=="A" or playerans0=="b" or playerans0=="B" or playerans0=="c" or playerans0=="C" or playerans0=="d" or playerans0=="D" or playerans0=="e" or playerans0=="E" or playerans0=="f" or playerans0=="F" or playerans0=="g" or playerans0=="G" or playerans0=="h" or playerans0=="H" or playerans0=="i" or playerans0=="I" or playerans0=="j" or playerans0=="J" or playerans0=="k" or playerans0=="K" or playerans0=="l" or playerans0=="L" or playerans0=="m" or playerans0=="M" or playerans0=="n" or playerans0=="N" or playerans0=="o" or playerans0=="O" or playerans0=="p" or playerans0=="P" or playerans0=="q" or playerans0=="Q" or playerans0=="r" or playerans0=="R" or playerans0=="s" or playerans0=="S" or playerans0=="t" or playerans0=="T" or playerans0=="u" or playerans0=="U" or playerans0=="v" or playerans0=="V" or playerans0=="w" or playerans0=="W" or playerans0=="x" or playerans0=="X" or playerans0=="y" or playerans0=="Y" or playerans0=="z" or playerans0=="Z":											
							if check2=="b" or (playerans not in templist):
						
								if ((check=="a") or ((playerans in reqlist) and (nextroundans==playerans0))):
									templist.append(playerans)
									
									lastchar=playerans[-1]
									list_of_comp_ans=[f for f in content if f[0].lower()==lastchar.lower()]
									ansposted=random.choice(list_of_comp_ans)
									if ansposted not in templist:
										templist.append(ansposted)
															  	
										nextroundans=str(ansposted[-1])								  
										print("\nComputer is thinking....",end="\r")
										time.sleep(1)
										print("\033[1;34;40mComputer's answer :\033[1;37;40m", ansposted,"\n") 
										check="no"
							
										score+=1
							
										check2="no"
									else:
										print("\033[1;36;40m_"*120)
										print("\033[1;31;40m\nCOMPUTER COULDN'T THINK MORE.\n\nYOU WON  :)")
										print("\033[1;36;40m_"*120)
										break							
								else:
									print("\033[1;36;40m_"*120)
									print("\033[1;31;40m\nOHH NO ! THATS NOT A PLACE STARTING WITH ",nextroundans,".\n\nBETTER LUCK NEXT TIME  :)")
									print("\033[1;36;40m_"*120)
									print('''
														\033[1;37;40m                   
			S C O R E : ''',score,'''
							
														''')
									print("\033[1;36;40m_"*120)
									hsf=open("highscore.txt","a")
									hsf.write("%d" %score)
									hsf.close()
							
									break
									
							else:
								
									print('''\033[1;31;40m
OOPS ! THAT PLACE WAS ALREADY DONE .
''')
								
						else:
							
							print('''
\033[1;31;40mDO NOT ENTER NUMBERS OR SPECIAL CHARACTERS
						''')
					else:
						print('''
\033[1;31;40mDO NOT ENTER NUMBERS OR SPECIAL CHARACTERS
						''')
						
						
						
						
						
					
					
					
				
			#INSTRUCTIONS
			
			elif fr=="i" or fr=="I":
				print('''                       \033[1;33;40m
                 I N S T R U C T I O N S 
''')
				print('''

\033[1;31;40m>> NOTE : 

Here 'place(s)' refers to ANY cities, districts, states, countries or continents across the globe but does not refer to local localities within a city.


\033[1;31;40m>> SIDENOTE BY CREATOR :
	
	
\033[1;31;40mI have tried to cover almost all the places known in world (over 3500 places), Even if the computer is unable to detect a valid place then i am really sorry for that. I request youto kindly write me at my contacts (present in ABOUT section)I will surely update that place :)


\033[1;32;40m____________________________________________________________

\033[1;32;40m>> THIS IS HOW ATLAS IS PLAYED : 
\033[1;32;40m____________________________________________________________


\033[1;33;40m◆ You enter ANY random word in your 1st chance.

◆ Computer guesses a name of a place starting with the last   letter of your entered word.

◆ Now its your turn. You have to enter a name of a place      (literally ANY place, even smaller less known places)       starting with the last letter of Computer's answer.

◆ Now again Computer will guess a name of a place starting    with the last letter of your previous answer. And the game  goes on like that.

◆ If you are unable to guess a name of a place starting with  the last letter of Computer's answer, you loose.


\033[1;32;40m____________________________________________________________

\033[1;32;40m>> THIS IS HOW A GAME WOULD LOOK LIKE :
\033[1;32;40m____________________________________________________________	

		
\033[1;33;40m   You : indi\033[1;37;40ma

  \033[1;33;40m Computer :\033[1;37;40m a\033[1;33;40mllahaba\033[1;35;40md

 \033[1;33;40m  You : \033[1;35;40md\033[1;33;40menmar\033[1;34;40mk

 \033[1;33;40m  Computer :\033[1;34;40m k\033[1;33;40mathmand\033[1;30;40mu

   \033[1;33;40mand so on....


\033[1;32;40m____________________________________________________________

\033[1;32;40m>> RULES FOR PLAYING THE GAME : 
\033[1;32;40m____________________________________________________________


\033[1;33;40m◆ You cannot enter a name of a place that is already said     earlier (either by you or computer) in that round.

◆ Spellings of name of the place you are entering have to be  correct.

◆ Spaces in name of a place has to be omitted (For example,   Hong Kong is to entered as "hongkong" instead of            "hong kong").

◆ You can type in any format, be it capital or small or       mixture of both.

◆ Special characters or Numbers are not to be entered.


\033[1;32;40m____________________________________________________________

\033[1;32;40m>> HOW THE GAME ENDS :
\033[1;32;40m____________________________________________________________	

		
\033[1;33;40m◆ If you are unable to guess a name of a place starting with  the last letter of Computer's answer, you LOOSE.

◆ If Computer is unable to guess a name of a place starting   with the last letter of your answer (which is very          unlikely), you WIN the game.

\033[1;36;40m________________________________________________________________________________________________________________________



\033[1;31;40m       SCROLL UP TO VIEW COMPLETE INSTRUCTIONS PAGE


\033[1;36;40m________________________________________________________________________________________________________________________
''')	
		
			elif fr=="p" or fr=="P":
				print("\033[1;33;40m>> HERE IS THE COMPLETE DATABASE OF PLACES : \n")
				for i in reqlist:
					print (i)
				print("\033[1;36;40m_"*120)
			
			elif fr=="h" or fr=="H":
				print("\033[1;33;40m>> HERE IS THE COMPLETE HISTORY OF GAMES PLAYED : \n")
				print("• HIGHSCORE : ",max(hslist))
				print("\n• TOTAL NO OF GAMES PLAYED : ",len(hslist))
				print("\n• SCORECARD : \n")
				print(hslist,sep=" , ")
				print('''
'''+"\033[1;36;40m_"*120)
				
			#RETURN BACK 
			
			else:
				print('''                    \033[1;30;47m  M A I N   M E N U  ''')
				break
				
	#RATING SYSTEM
	
	elif gamestat=="R" or gamestat=="r":
		fed=str(input("\n\n\033[1;35;40mPLEASE RATE US OUT OF 5 : "))
		if fed=="2":
				print("\033[1;35;40m\nHOPE YOU HAVE A BETTER EXPERIENCE NEXT TIME !\n ")
		elif fed=="3" or fed=="4":
				print("\033[1;32;40m\nTHANK YOU FOR YOUR VALUABLE FEEDBACK !\n ")
		elif fed=="0" or fed=="1":
				print("\033[1;31;40m\nWE ARE REALLY SORRY TO HEAR THAT.\nHOPE YOU HAVE A BETTER EXPERIENCE NEXT TIME ! \n")
		elif fed=="5":
				print("\033[1;32;40m\nOHH ! THAT WAS GREAT.\nTHANK YOU :) \n")
		else:
				print("\033[1;31;40m\nKINDLY ENTER VALID RESPONSE NEXT TIME :)\n ")
		
		print("\033[1;36;40m_"*120)
				
	#ABOUT SYSTEM
	
	elif gamestat=="A" or gamestat=="a":
		print('''
		
\033[1;35;40mTHIS \033[1;36;40mATLAS \033[1;35;40mGAME IS SOLELY CREATED BY \033[1;32;40mSANIDHYA KUMAR.
\033[1;35;40mREPLICATION OF THIS GAME IN ANY FORM WITHOUT PRIOR
PERMISSION OF THE CREATOR IS A PUNISHABLE OFFENCE UNDER
INTELLECTUAL PROPERTY RIGHTS ACT (IPR)

FOR FEEDBACK / CONTACT :
• EMAIL : kumarsanidhya.31@gmail.com
• PHONE : 7875536529
''')
		print('''               \033[1;30;47m © S A N I D H Y A   K U M A R 
		''')
		print("\033[1;36;40m_"*120)
	
	#EXIT SYSTEM
	
	else:
		print('''

          \033[1;30;47m  T H A N K S   F O R   P L A Y I N G  \033[1;36;40m
                    ''')
		print("\033[1;36;40m_"*120)
		print("\033[1;30;40m")
		break