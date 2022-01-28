# Importing all the packages we need for programme
from playsound import playsound
from depe import MyMod as fi
import json as jo

# Making classes for different varable
# Class for directories
class dir:
    def __init__(self, name, sub_dir_or_mus, location):
        self.sub_dir_mus = sub_dir_or_mus
        self.nam = name
        self.location = location

    def showadd(self):
        print(self.location)

    def showname(self):
        print(self.nam)

    def showopt(self):
        print(self.sub_dir_mus)


# Class1 for music file
class musfil:
    def __init__(self, name, location):
        self.nam = name
        self.address = location

    def shownam(self):
        print(self.nam)

    def showaddress(self):
        print(self.address)
    def play(self):
        print(f"\nName: {self.nam}\nLocation: {self.address}")
        playsound(self.address)

#Global varables
#Configuration file
try:
    data = jo.load(open(__file__.replace("musplayer.py","depe\\paths.json")))
    dir_alan_path = data["Alan_Walker"]
    dir_neha_path = data["Neha_Kakkar"]
except FileNotFoundError:
    data = jo.load(open(__file__.replace("musplayer.py","paths.json")))
    dir_alan_path = data["Alan_Walker"]
    dir_neha_path = data["Neha_Kakkar"]

# Some extra settings before main code
usr_run = True
# this is objects of class0
Alan_walker = dir("Alan_Walker", ['all_falls_down', 'alone', 'faded', 'lily', 'sing_me_to_sleep', 'spectre'],
                  dir_alan_path)
Neha_kakkar = dir("Neha_Kakkar", ['dil_ko_karaar_aaya', 'garmi', 'taaron_ke_shehar', 'yaad_piya_ki_aane_lagi'],
                  dir_neha_path)
# this is objects of class1
# Alan_Walker
all_falls_down = musfil("all_falls_down",(dir_alan_path.__add__('\\all_falls_down.wav')))
alone = musfil("alone",(dir_alan_path.__add__('\\alone.wav')))
faded = musfil("faded",(dir_alan_path.__add__('\\faded.wav')))
lily = musfil("lily",(dir_alan_path.__add__('\\lily.wav')))
sing_me_to_sleep = musfil("sing_me_to_sleep",(dir_alan_path.__add__('\\sing_me_to_sleep.wav')))
spectre = musfil("spectre",(dir_alan_path.__add__('\\spectre.wav')))
# Neha kakkar
dil_ko_karaar_aaya = musfil("dil_ko_karaar_aaya",(dir_neha_path.__add__('\\dil_ko_karaar_aaya.wav')))
garmi = musfil("garmi",(dir_neha_path.__add__('\\garmi.wav')))
taaron_ke_shehar = musfil("taaron_ke_shehar",(dir_neha_path.__add__('\\taaron_ke_shehar.wav')))
yaad_piya_ki_aane_lagi = musfil("yaad_piya_ki_aane_lagi",(dir_neha_path.__add__('\\yaad_piya_ki_aane_lagi.wav')))
dire = ["alan_walker", ',', "neha_kakkar"]
musfile = [all_falls_down, alone, faded, lily, sing_me_to_sleep, spectre, dil_ko_karaar_aaya, garmi, taaron_ke_shehar,
           yaad_piya_ki_aane_lagi]
musfile1 = ["all_falls_down", "alone", "faded", "lily", "sing_me_to_sleep", "spectre", "dil_ko_karaar_aaya", "garmi",
            "taaron_ke_shehar", "yaad_piya_ki_aane_lagi"]
dirs = ["alan_walker", "neha_kakkar"]
# Programme files and directories
# Giving some instructions to user about programme(how to give input, how it works, what they haven't to do)
print("MUSPLAYER\n", "GENERAL INSTRUCTIONS\n", ">>1. You don't have to give input in shortform/longform\n",
      ">>2. You only have to give input according to instruction you gave before giving input\n",
      ">>3. if you give input in wrong way the program could be stop running\n",
      ">>4. instruction will given in a bracket '{}' with '~'\n",
      ">>5. If you want to quite from any particular section then enter 'quit'\n",
      ">>6. warning is written in square bracket '[]' with '~'\n",
      "////////////////////~~ MUSPLAYER ~~\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")

# program start
while usr_run == True:
    fir1 = input(
        "what you want to do? you have options:- search directory(enter searchdir, search song & play(enter playsong){~enter either searchdir or showdirs for search song directorys / enter playsong if you know any song name in the directory to play directly}\n ")
    fir1 = fi.myFilter(fir1)
    usr_run1 = True
    if fir1 == "searchdir" or fir1 == "showdirs":
        while usr_run1 != False:
            inp = input(
                'Enter which directory you want to search.{~Enter the directory name which you want to see. if it present in list , and if you want to quit this session then enter "quit", if you dont know how huch dirs it contains then enter "showdirs"}\n')
            inp = fi.myFilter(inp)
            if inp in dire:
                # if they do input for alan walker dir
                if inp == "alan_walker":
                    print("Name:-\n", Alan_walker.nam, "\n", "Contain:-\n", Alan_walker.sub_dir_mus, "\n",
                          "Location:-\n", Alan_walker.location, "\n")
                # if they do input for neha kakkar dir
                elif inp == "neha_kakkar":
                    print("Name:-\n", Neha_kakkar.nam, "\n", "Contain:-\n", Neha_kakkar.sub_dir_mus, "\n",
                          "Location:-\n", Neha_kakkar.location, "\n")
            elif inp == "showdirs":
                print(f"num of dir are:-\n {len(dirs)}\n", f"they are:-\n {dirs}\n")
            elif inp == "quit":
                usr_run1 = False
            else:
                print("Directory not found\n", "'", inp, "'", "not found\n")
    elif fir1 == "playsong":
        while usr_run1 != False:
            inp = input(
                'Enter which song you want to lisine.{~Enter the song name which you want to lisin. if it present in list it will open, and if you want to quit this session the enter "quit", if you dont know how much songs it contains and what are they, then enter "showsongslist"}\n')
            inp = fi.myFilter(inp)
            if inp in musfile1 or inp == "quit" or inp == "showsongslist":
                if inp == "all_falls_down":
                    print("Name:-\n", all_falls_down.nam, "\n","Location:-\n", all_falls_down.address)
                    playsound(all_falls_down.address)
                elif inp == "alone":
                    print("Name:-\n", alone.nam,"\n","Location:-\n",alone.address)
                    playsound(alone.address)
                elif inp == "faded":
                    print("Name:-\n", faded.nam,"\n","Loction:-\n", faded.address)
                    playsound(faded.address)
                elif inp == "lily":
                    print("Name:-\n", lily.nam,"\n","Loction:-\n", lily.address, "\n")
                    playsound(lily.address)
                elif inp == "sing_me_to_sleep":
                    print("Name:-\n", sing_me_to_sleep.nam,"\n","Loction:-\n", sing_me_to_sleep.address, "\n")
                    playsound(sing_me_to_sleep.address)
                elif inp == "spectre":
                    print("Name:-\n", spectre.nam,"\n","Loction:-\n", spectre.address,"\n")
                    playsound(spectre.address)
                elif inp == "dil_ko_karaar_aaya":
                    print("Name:-\n", dil_ko_karaar_aaya.nam,"\n","Loction:-\n", dil_ko_karaar_aaya.address, "\n")
                    playsound(dil_ko_karaar_aaya.address)
                elif inp == "garmi":
                    print("Name:-\n", garmi.nam,"\n", "Loction:-\n", garmi.address, "\n")
                    playsound(garmi.address)
                elif inp == "taaron_ke_shehar":
                    print("Name:-\n", taaron_ke_shehar.nam,"\n", "Loction:-\n", taaron_ke_shehar.address, "\n")
                    playsound(taaron_ke_shehar.address)
                elif inp == "yaad_piya_ki_aane_lagi":
                    print("Name:-\n", yaad_piya_ki_aane_lagi.nam, "\n","Loction:-\n", yaad_piya_ki_aane_lagi.address, "\n")
                    playsound(yaad_piya_ki_aane_lagi.address)
                elif inp == "showsongslist":
                    print(f"the number of songs are:-\n {len(musfile1)}\n They are:-\n {musfile1}")
                elif inp == "quit":
                    usr_run1 = False
                else:
                    print("Some thing wents wrong")
            elif inp not in musfile and inp != "quit":
                print("This song in not in list\n", inp, "is not in list")
            else:
                print("Some thing wents wrong")
    elif fir1 == "quit":
        break
    else:
        print("something wents wrong")
