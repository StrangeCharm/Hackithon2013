#Imports/Initializationv
import os, time, sys, random
def typer(what_you_want_to_type):
  for letter in what_you_want_to_type:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(random.random()*0.2)
#word banks are levels in the game
  print ""
secrets = 0
wordbank1=["a","all","am","and","at","ball","be","bed","big","book","box","boy","but","came","can","car","cat","come","cow","dad","day","did","do","dog","fat","for","fun","get","go","good","got","had","hat","he","hen","here","him","his","home","hot","I","if","in","into","is","it","its","let","like","look","man","may","me","mom","my","no","not","of","oh","old","on","one","out","pan","pet","pig","play","ran","rat","red","ride","run","sat","see","she","sit","six","so","stop","sun","ten","the","this","to","top","toy","two","up","us","was","we","will","yes","you","Butt"]
wordbank2=["about","add","after","ago","an","any","apple","are","as","ask","ate","away","baby","back","bad","bag","base","bat","bee","been","before","being","best","bike","bill","bird","black","blue","boat","both","bring","brother","brown","bus","buy","by","cake","call","candy","change","child","city","clean","club","coat","cold","coming","corn","could","cry","cup","cut","daddy","dear","deep","deer","doing","doll","door","down","dress","drive","drop","dry","duck","each","eat","eating","egg","end","fall","far","farm","fast","father","feed","feel","feet","fell","find","fine","fire","first","fish","five","fix","flag","floor","fly","food","foot","four","fox","from","full","funny","game","gas","gave","girl","give","glad","goat","goes","going","gold","gone","grade","grass","green","grow","hand","happy","hard","has","have","hear","help","here","hill","hit","hold","hole","hop","hope","horse","house","how","ice","inch","inside","job","jump","just","keep","king","know","lake","land","last","late","lay","left","leg","light","line","little","live","lives","long","looking","lost","lot","love","mad","made","make","many","meat","men","met","mile","milk","mine","miss","moon","more","most","mother","move","much","must","myself","nail","name","need","new","next","nice","night","nine","north","now","nut","off","only","open","or","other","our","outside","over","page","park","part","pay","pick","plant","playing","pony","post","pull","put","rabbit","rain","read","rest","riding","road","rock","room","said","same","sang","saw","say","school","sea","seat","seem","seen","send","set","seven","sheep","ship","shoe","show","sick","side","sing","sky","sleep","small","snow","some","soon","spell","start","stay","still","store","story","take","talk","tall","teach","tell","than","thank","that","them","then","there","they","Butt"]
wordbank3=["able","above","afraid","afternoon","again","age","air","airplane","almost","alone","along","already","also","always","animal","another","anything","around","art","aunt","balloon","bark","barn","basket","beach","bear","because","become","began","begin","behind","believe","below","belt","better","birthday","body","bones","born","bought","bread","bright","broke","brought","busy","cabin","cage","camp","can't","care","carry","catch","cattle","cave","children","class","close","cloth","coal","color","corner","cotton","cover","dark","desert","didn't","dinner","dishes","does","done","don't","dragon","draw","dream","drink","early","earth","east","eight","even","ever","every","everyone","everything","eyes","face","family","feeling","felt","few","fight","fishing","flower","flying","follow","forest","forgot","form","found","fourth","free","Friday","friend","front","getting","given","grandmother","great","grew","ground","guess","hair","half","having","head","heard","he's","heat","hello","high","himself","hour","hundred","hurry","hurt","I'd","I'll","I'm","inches","isn't","it's","I've","kept","kids","kind","kitten","knew","knife","lady","large","largest","later","learn","leave","let's","letter","life","list","living","lovely","loving","lunch","mail","making","maybe","mean","merry","might","mind","money","month","morning","mouse","mouth","Mr.","Mrs.","Ms.","music","near","nearly","never","news","noise","nothing","number","often","oil","once","orange","order","own","pair","paint","paper","party","pass","past","penny","people","person","picture","place","plan","plane","please","pocket","point","poor","race","reach","reading","ready","real","rich","right","river","rocket","rode","round","rule","running","salt","says","sending","sent","seventh","sew","shall","short","shot","should","sight","sister","sitting","sixth","sled","smoke","soap","someone","something","sometime","song","sorry","sound","south","space","spelling","spent","sport","spring","stairs","stand","state","step","stick","stood","stopped","stove","street","strong","study","such","sugar","summer","Sunday","supper","table","taken","taking","talking","teacher","team","teeth","tenth","that's","their","these","thinking","third","those","thought","throw","tonight","trade","trick","trip","trying","turn","twelve","twenty","uncle","under","upon","wagon","wait","walking","wasn't","watch","water","weather","we're","west","wheat","where","which","wife","wild","win","window","winter","without","woman","won","won't","wool","word","working","world","would","write","wrong","yard","year","yesterday","you're","Butt"]
wordbank4=["across","against","answer","awhile","between","board","bottom","breakfast","broken","build","building","built","captain","carried","caught","charge","chicken","circus","cities","clothes","company","couldn't","country","discover","doctor","doesn't","dollar","during","eighth","else","enjoy","enough","everybody","example","except","excuse","field","fifth","finish","following","good-by","group","happened","harden","haven't","heavy","held","hospital","idea","instead","known","laugh","middle","minute","mountain","ninth","ocean","office","parent","peanut","pencil","picnic","police","pretty","prize","quite","radio","raise","really","reason","remember","return","Saturday","scare","second","since","slowly","stories","student","sudden","suit","sure","swimming","though","threw","tired","together","tomorrow","toward","tried","trouble","truly","turtle","until","village","visit","wear","we'll","whole","whose","women","wouldn't","writing","written","wrote","yell","young","Butt"]
wordbank5=["although","America","among","arrive","attention","beautiful","countries","course","cousin","decide","different","evening","favorite","finally","future","happiest","happiness","important","interest","piece","planet","present","president","principal","probably","problem","receive","sentence","several","special","suddenly","suppose","surely","surprise","they're","through","usually","Butt"]
lives = 10
#Intro for the game
print '''
##############################################################################
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                            _       _   _        _                          #
#                    \    / |_  |   /   / \ |\/| |_                          #
#                     \/\/  |_  |__ \_  \_/ |  | |_                          #
#                                ___   _                                     #
#                                 |   / \                                    #
#                                 |   \_/                                    #
#                              _        _                                    #
#                         |   |_  \  / |_  |                                 #
#                         |__ |_   \/  |_  |__                               #
#                                (LEVEL)                                     #
#                                                                            #
#                                                                            #
#                                                                            #
##############################################################################
'''
time.sleep(3)
print '''
##############################################################################
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            # 
#                    A word will appear here for you to type.                #
#                If you spell it correctly, you get more points.             #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#               Decide if you want to use a custom word bank,                #
#               then choose your difficulty level from 1-10.                 #
#                                                                            #
#                                                                            #
##############################################################################
'''
print '''This is your points.          These are the mistakes that you have left.
           |                                    |
           V                                    V
         Points: ???                        Mistakes left: ???
'''
#This is the base for each level
keepGoing = True
GAMEPLAY = True
while GAMEPLAY:
  data = raw_input("Would you like to use a custom word bank? (y/n)")
  adding_word_bank = True
  custom_word_bank_check = False
  if data == "y":
    custom_word_bank_check = True
    custom_word_bank = []
    print '''Type your custom word bank here
Make sure to type it in one word at a time, and press enter in between each word.
Type "end" once you are done inputting all of your words'''
    while adding_word_bank:
      customword = raw_input()
      if customword == "end":
        adding_word_bank = False
      else:
        custom_word_bank.append(customword)
  lives = 10
  data=raw_input("Choose your difficulty level!")
  if data == "Up Up Down Down Left Right Left Right B A Start":
	lives = 101
  if data == "1":
	lives = 10
  if data == "2":
	lives = 9
  if data == "3":
	lives = 8
  if data == "4":
	lives = 7
  if data == "5":
	lives = 6
  if data == "6":
	lives = 5
  if data == "7":
	lives = 4
  if data == "8":
	lives = 3
  if data == "9":
	lives = 2
  if data == "10":
	lives = 1
  else:
    print ""
  points=0
  while keepGoing:
    if points >= 0:
      word = random.choice(wordbank1)
    if points > 10:
      word = random.choice(wordbank2)
    if points > 30:
      word = random.choice(wordbank3)
    if points > 50:
      word = random.choice(wordbank4)
    if points > 70:
      word = random.choice(wordbank5)
    if custom_word_bank_check == True:
      word = random.choice(custom_word_bank)
    if points > 99:
      word = "You win!"
    y = 39
    for letter in word:
      y = y -1
    print '''
##############################################################################
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            # 
#                                                                            #
#                                  ''', word, y * " ", '''#
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
##############################################################################
'''
    print "Points: ", points, "           Mistakes left: ", lives * "* "
    data = raw_input()
    if data == "Up Up Down Down Left Right Left Right B A Start":
  	  print '''Thanks for playing our game form Hackathon 2013 
  	  From: Michael Jury and Drew Howells and Juan Carmona.
  	  
  	  We got secund prize for the over all award!!!!!'''
  	  time.sleep(3)
  	  secrets=secrets+1
    if data == word:
      if data == "You win!":
        points = 999999998
      points = points +1
    else:
      lives = lives -1
      if lives == 0:
          keepGoing = False
  print '''
  
##############################################################################
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #  
#                               You Lose!                                    #
#                         Better luck next time!                             #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
##############################################################################

'''
  data = raw_input('''Would you like to play again? (y/n)''')
  if data == "y":
    keepGoing = True
  else:
    GAMEPLAY = False
print '''

##############################################################################
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #  
#                               Goodbye!                                     #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
#                                                                            #
##############################################################################

'''
time.sleep(1)
