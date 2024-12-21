#Jeriah Oliverasfair Full Stack Dev MR.Forlenza class 
# This is my Text based adventure game called eldrich adventure with merchants 

print(""" _______      __                         ___    __                                          
 |  ___) \    / _)                       / _ \  / _)                                         
 | |_   \ \   \ \   ___  ___   ___ __   | |_| | \ \  _________ ___ _  _____ _   _  ___  ___  
 |  _)   > \ / _ \ / _ \| \ \ / / '_ \  |  _  |/ _ \(  _____  ) __) |/ (   ) | | |/ _ \/ __) 
 | |___ / ^ ( (_) ) |_) ) |\ v /| | | | | | | ( (_) ) |_/ \_| > _)| / / | || |_| | |_) > _)  
 |_____)_/ \_\___/|  __/ \_)> < |_| | | |_| |_|\___/ \___^___/\___)__/   \_)\___/|  __/\___) 
                  | |      / ^ \    | |                                          | |         
                  |_|     /_/ \_\   |_|                                          |_|          
""")
# This prints the title art for the text based adventure game


from time import sleep
#this imports the sleep function that i use for the type function that i use for a typewriter effect

def type(text):
  for i in text:
    print(i, end = "")
    sleep(.1)
  print("")
# define fuction type allows whatever text i type using the function to have a typewriter effect


print()
print()
print()
print()
# This allows me to make spaces and start the the game without interfearing with the title of of the game 

type("Welcome to Eldirich Adventure With Merchants")
type("plss enjoy")
# This types the text being showed above this comment and after the last comment

print()
print()
print()


type("you wake up in a foreign eldritch land")
print()
type("your realy confused but you dont question it")
# This types the start of the story

print()
print()
#extra spacing
type("you oddly feel a sudden hunger to be rich by selling something")
# types the text
print()
#extra spacing
type("idk? i dont make the rules")
#types the text 

print()
print()
print()
# more spacing for organization

type("you see a forest with three pathways Left, Middle ,and Right")
# This types out the circumstance and lists out your writable options 
def start():
  Forest_choice
# This is the start of the start function
Forest_choice = input("which pathway would you like to go on ?")
# This shows a a prompt for the user to choose wich option they want to choose

def Left():
  type("you get deeper in the forest and now your lost your never going to get out and your journey ends HAHA")
  print()
  print()
  print("hit Run to start again")
if Forest_choice == "Left":
  Left()
# This define fuction and if statement cover the otcomes of the left choice


def Right():
  print()
  type("you Go Right and you see a scary eldrich cosmic eyball ")
  print("""           ___________
            .-=d88888888888b=-.
        .:d8888pr"|\|/-\|'rq8888b.
      ,:d8888P^//\-\/_\ /_\/^q888/b.
    ,;d88888/~-/ .-~  _~-. |/-q88888b,
   //8888887-\ _/    (#)  \\-\/Y88888b\
   \8888888|// T      `    Y _/|888888 o
    \q88888|- \l           !\_/|88888p/
     'q8888l\-//\         / /\|!8888P'
       'q888\/-| "-,___.-^\/-\/888P'
         `=88\./-/|/ |-/!\/-!/88='
            ^^"-------------"^    """)
  print()
  type("you are confused but you realize you are an adventurer and you can fight")
  print()
  fight_eyball = input("will you consider fighting the eyeball Yes or No")
  if fight_eyball == "NO":
    print()
    type("you run away in fear even though you made a statement on how you could fight ")
    print()
    type("you contemplate why you even considered the though of fighting it and you end your journey")
    print()
    type("your kind of an idiot")
  if fight_eyball == "Yes":
    print()
    type("you end up trying to fight this cosmic eyeball you cant quite full comprehend aaaaandddd you")
    type("die you absolutely die boo hoo too bad for you pookie")
    print()
    print("Hit run to restart")
if Forest_choice == "Right":
  Right()
# This define fuction and if statement cover the otcomes of the Right choice and the exterior choices associated with that choice
def middle():
  print()
  type("You end up getting out of the forest")
  print()
  print()
  continue_adventure = input("do you wanna coninue your adventure Yes or No ?")
  if continue_adventure == "No":
    print()
    type("you sit there contemplating why you even started you adventure in the first place why even continue you feel a sense of emptiness ass your journey ends")
  if continue_adventure == "Yes":
    print()
    type("you continue your crazy whacky journey through this scary eldrich world")
    print()
    type("you come across a shiny object on your dark scary trail")
    print()
    pick_it_up = input("do you want to pick it up Yes or No?")
    if pick_it_up == "No":
      print()
      type("you sit there contemplating why you even started you adventure in the first place why even continue you feel a sense of emptiness ass your journey ends")
      print()
    if pick_it_up == "Yes":
      print()
      type("you found a creepy looking artifact")
      print()
      print("""⣠⡤⠶⡄⠀⠀⠀⠀⠀⠀⠀⢠⠶⣦⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⡟⠀⠈⣀⣾⣝⣯⣿⣛⣷⣦⡀⠀⠈⢿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⡇⠀⢼⣿⣽⣿⢻⣿⣻⣿⣟⣷⡄⠀⢸⣿⣿⣾⣄⠀⠀⠀
⠀⠀⣞⣿⣿⣿⣿⣷⣤⣸⣟⣿⣿⣻⣯⣿⣿⣿⣿⣀⣴⣿⣿⣿⣿⣯⣆⠀⠀
⠀⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⡆⠀
⢠⣟⣯⣿⣿⣿⣷⢿⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣟⠿⣿⣿⣿⣿⡷⣾⠀
⢸⣯⣿⣿⡏⠙⡇⣾⣟⣿⡿⢿⣿⣿⣿⣿⣿⢿⣟⡿⣿⠀⡟⠉⢹⣿⣿⢿⡄
⢸⣯⡿⢿⠀⠀⠱⢈⣿⢿⣿⡿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣀⠃⠀⢸⡿⣿⣿⡇
⢸⣿⣇⠈⢃⣴⠟⠛⢉⣸⣇⣹⣿⣿⠚⡿⣿⣉⣿⠃⠈⠙⢻⡄⠎⠀⣿⡷⠃
⠈⡇⣿⠀⠀⠻⣤⠠⣿⠉⢻⡟⢷⣝⣷⠉⣿⢿⡻⣃⢀⢤⢀⡏⠀⢠⡏⡼⠀
⠀⠘⠘⡅⠀⣔⠚⢀⣉⣻⡾⢡⡾⣻⣧⡾⢃⣈⣳⢧⡘⠤⠞⠁⠀⡼⠁⠀⠀
⠀⠀⠀⠸⡀⠀⢠⡎⣝⠉⢰⠾⠿⢯⡘⢧⡧⠄⠀⡄⢻⠀⠀⠀⢰⠁⠀⠀⠀
⠀⠀⠀⠀⠁⠀⠈⢧⣈⠀⠘⢦⠀⣀⠇⣼⠃⠰⣄⣡⠞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢤⠼⠁⠀⠀⠳⣤⡼⠀⠀⠀⠀⠀⠀""")
      print()
      print()
      type("it looks odly familiar you think you may have seen it inside of a book")
      print()
      type("wait you have its cthulu ya know the HP lovecraft book if your playing this game i shouldnt have to explain")
      print()
      type("you suddenly feel kind of ill after holding it for a good minute you realize you have to sell it or give it to some unfortunate person")
      print()
      type("you continue walking and you come across a merchant ")
      print()
      type("you jump up and glee because you can finally sell this cthulu artifact and stop being ill")
      sell_it = input("do you sell it to the merchant Yes or No ?")
      if sell_it == "No":
        print()
        type("idk why you would choose this but you get even more sick due to the illness from the statue and you die plss try again idiot")
        print()
      if sell_it == "Yes":
        print()
        type("you sell the cthulu artifact to the merchant and get alot of riches your pretty rich now yayyyy")
        print()
        type("the merchant quickly dies as he was old and the illness from the cthulu artifact instantly effected him")
        print()
        type("you contemplate stealing the rest of the old man merchants riches and settling down in this world as a rich adventurer")
        steal_from_dead_merchant = input("do you wanna steal from the dead merchant Yes or No")
        if steal_from_dead_merchant == "No":
          print()
          type("you end your adventure without being a thief of the dead and live in a hotel living off of selling random artifacts for a living")
          print()
          type("hit run to restart and get alternate ending")
        if steal_from_dead_merchant == "Yes":
          print()
          type("you steal from the dead merchant and you go on to live you end your journey and settle dow as a rich adventurer ")
          print()
if Forest_choice == "Middle":
  middle()
#this define and if statement covers the outcome of the middle choice and the choices that come with it 

start() 

