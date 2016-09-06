#this program generates a fill-in-the-blanks paragraph from a string and a list of key words
#then it displays the texts with blank words and it prompts the user for the right words

easytext = "There was a young lady of Lynn,\nWho was so excessively thin, \nThat when she essayed To drink lemonade\nShe slipped through the straw and fell in. "
easyanswers = ['thin','drink','slipped']
mediumtext = "Pong is the very first sports arcade video game. It is a table tennis\nsports game featuring simple two-dimensional graphics.  Pong was one of \nthe first to reach mainstream popularity. The aim is to defeat an \nopponent in a simulated table-tennis game by earning a higher score.\nThe game was originally manufactured by Atari, which released it in\n 1972. Allan Alcorn created Pong as a training exercise assigned to him\n by Atari co-founder Nolan Bushnell. Bushnell based the idea on an \nelectronic ping-pong game included in the very first console, the Magnavox \nOdyssey, which later resulted in a lawsuit against Atari. Surprised by the \nquality of Alcorn's work, Bushnell and Atari co-founder Ted Dabney \ndecided to manufacture it. "
mediumanswers = ["video","graphics","Atari","Odyssey","lawsuit"]
#medium level content  has been picked from wikipedia at https://en.wikipedia.org/wiki/Pong
hardtext = "Radiocarbon dating (also referred to as carbon dating or\n carbon-14 dating) is a method for determining the age of an\n object containing organic material by using the properties of\n radiocarbon (C-14), a radioactive isotope of carbon. The method\n was developed by Willard Libby in the late 1940s and soon\n became a standard tool for archaeologists. Libby received the\n Nobel Prize for his work in 1960. The radiocarbon dating method\n is based on the fact that radiocarbon is constantly being\n created in the atmosphere by the interaction of cosmic rays\n with atmospheric nitrogen. The resulting radiocarbon combines\n with atmospheric oxygen to form radioactive carbon dioxide,\n which is incorporated into plants by photosynthesis; animals\n then acquire C-14 by eating the plants. When the animal or\n plant dies, it stops exchanging carbon with its environment, and\n from that point onwards the amount of C-14 it contains begins to\n decrease as the C-14 undergoes radioactive decay. Measuring the amount\n of C-14 in a sample from a dead plant or animal such as a\n piece of wood or a fragment of bone provides information that\n can be used to calculate when the animal or plant died. The\n older a sample is, the less C-14 there is to be detected, and\n because the half-life of C-14 (the period of time after which\n half of a given sample will have decayed) is about 5,730 years,\n the oldest dates that can be reliably measured by radiocarbon\n dating are around 50,000 years ago, although special\n preparation methods occasionally permit dating of older\n samples. The idea behind radiocarbon dating is straightforward,\n but years of work were required to develop the technique to the\n point where accurate dates could be obtained. Research has been\n ongoing since the 1960s to determine what the proportion of C-14\n in the atmosphere has been over the past fifty thousand years.\n The resulting data, in the form of a calibration curve, is now\n used to convert a given measurement of radiocarbon in a sample\n into an estimate of the sample's calendar age. Other\n corrections must be made to account for the proportion of C-14\n in different types of organisms (fractionation), and the\n varying levels of C-14 throughout the biosphere (reservoir\n effects). Additional complications come from the burning of\n fossil fuels such as coal and oil, and from the above-ground\n nuclear tests done in the 1950s and 1960s. Because the time it\n takes to convert biological materials to fossil fuels is\n substantially longer than the time it takes for its C-14 to\n decay below detectable levels, they contain almost no C-14, and\n as a result there was a noticeable drop in the proportion of\n C-14 in the atmosphere beginning in the late 19th century.\n\n Conversely, nuclear testing increased the amount of C-14 in the\n atmosphere, which attained a maximum in 1963 of almost twice\n what it had been before the testing began.Measurement of\n radiocarbon was originally done by beta-counting devices, which\n counted the amount of beta radiation emitted by decaying\n C-14 atoms in a sample. More recently, accelerator mass spectrometry\n has become the method of choice; it counts all the C-14 atoms in\n the sample and not just the few that happen to decay during the\n measurements; it can therefore be used with much smaller\n samples (as small as individual plant seeds), and gives results\n much more quickly. The development of radiocarbon dating has\n had a profound impact on archaeology. In addition to permitting\n more accurate dating within archaeological sites than previous\n methods, it allows comparison of dates of events across great\n distances. Histories of archaeology often refer to its impact\n as the radiocarbon revolution. Radiocarbon dating has allowed\n key transitions in prehistory to be dated, such as the end of\n the last ice age, and the beginning of the Neolithic and Bronze\n Age in different regions."

hardanswers=['dating','age','organic','isotope','Nobel','decrease','calculate','half-life','fossil','drop','radiation','archaeology','prehistory','ice','Neolithic','Bronze']
#text taken from wikipedia at the url: https://en.wikipedia.org/wiki/Radiocarbon_dating

def punc_stripper(string):
    """this function accepts one string as input.
    it will return be the same string withouth the
    symbols specified in the list punctutationlist
    """
    stripped = ""
    punctutationlist = [',','.','\n','(',')']
    for character in string:
        if character not in punctutationlist:
            stripped = stripped + character
    return stripped


def homemade_Split(string):
    """This function accepts one string as input
    It will split the input string into a list using space (" ") as delimiter
    It will return the generated list
    """
    splitted = []
    word = ''
    for character in string:
        if character != " ":
            word = word + character
        else:
            splitted.append(word)
            word = ""
    return splitted


def blanker(text,listofkeywords):
    """This function requires 2 inputs: string and a list.
    The function will return a string similar to the input string but
    the words contained in the input list will be replaced by numbered labels"""
    textlist = homemade_Split(text)
    blanked = []
    for element in textlist:
        coreword = punc_stripper(element)
        if coreword not in listofkeywords:
            blanked.append(element)
        else:
            labelno = listofkeywords.index(coreword) + 1  #index will be reference to label numbers, we add 1 to comply with the label standard
            label = "__"+str(labelno)+"__"
            element = element.replace(coreword,label)    #we replace the core word leaving any potential punctuation in element
            blanked.append(element)
    blanked = " ".join(blanked)+"\n"
    return blanked

def game(text,listofkeywords):
    """This function runs the main game loops that contains the logic of the game
    This function requires two inputs: a text and a list. It will also expect user inputs
    the function will print the text and will compare the user input to the input list
    depending on the game events the gamer status will change and eventually will either print
    YOU WON or it will halt the program"""
    for keyword in listofkeywords:
        tries_left,warning,game_over = 5,1,0 #define gamer status depending on the games left
        print "you have "+str(tries_left)+" tries left\n\nThe current paragraph is:"
        while True:
            print "\n",blanker(text,listofkeywords)
            user_input = raw_input("What is the correct answer for __"+str(listofkeywords.index(keyword)+1)+"__?").lower()   #lower method used on input and keyword
            if keyword.lower() == user_input:
                listofkeywords[listofkeywords.index(keyword)] = None #When answer is right the list of keywords must be modified so the function prints the revealed anwsers
                break
            else:
                tries_left = tries_left - 1
                if tries_left == game_over:
                    exit()
                elif tries_left == warning:
                    print "Atention, you only have one TRY LEFT!"
                else:
                    print "\nThat is not the correct answer, lets try again\nYou still have "+str(tries_left)+" tries left\n"
    print "YOU WON !"
def game_selektor():
    """This function does not require preexisting input since it starts the game
    It prompts the user for an input
    depending on the input it will call the game function
    with the right set of inputs, which depend on the difficulty level"""
    user_input = ""
    while user_input not in ["easy","medium","hard"]:
        user_input = raw_input("Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard. ").lower()
        if user_input == "easy":
            print "\nYou have choosen easy\n"
            game(easytext,easyanswers)
        elif user_input == "medium":
            print "\nYou have choosen medium\n"
            game(mediumtext,mediumanswers)
        elif user_input == "hard":
            print "\nYou have choosen hard\n"
            game(hardtext,hardanswers)
        else:
            print "\nThat is not an option\n"
#lets start the game!
game_selektor()
