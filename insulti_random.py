# insulti_random.py
######################################################################
#                  dag7 - 2020 - wtfpl License

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004
 
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
 
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

#  0. You just DO WHAT THE FUCK YOU WANT TO.#
######################################################################

import random
import time
import sys

def read_from_a_file(fparole):
    fd = open(fparole, "r")
    
    l_parole = list()
    
    for linea in fd.readlines():
        l_parole.append(linea.rstrip())
    
    fd.close()

    return l_parole

def generator(x):
    if x == 0:
        return

    if x == "inf":
        while True:
            print((random.choice(prefixes)).capitalize() + " " + 
            (random.choice(s)).capitalize() + " " + 
            random.choice(suffixes))
            
            time.sleep(1)

    print(random.choice(prefixes) + " " + random.choice(s) + " " + random.choice(suffixes))
    
    generator(x-1)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        s = read_from_a_file("s.txt")
        prefixes = read_from_a_file("prefixes.txt")
        suffixes = read_from_a_file("suffixes.txt")

        # genero il seed (necessario per la generazione casuale)
        random.seed(a=None, version=2)

        # controlli vari: se questi falliscono il programma non deve partire
        if(len(s) == 0):
            print("Errore: Inserisci almeno un soggetto nel file s.txt ! (es. la persona che ti ha fatto sbroccare o il tuo vicino)")
            exit(1)

        if(len(prefixes) == 0):
            print("Errore: Inserisci almeno un prefisso nel file prefixes.txt (es. porco, cane, boia...)")
            exit(1)

        if(len(suffixes) == 0):
            print("Errore: Inserisci almeno un suffisso nel file suffixes.txt (ti consiglio un aggettivo brutto)")
            exit(1)
        
        if(sys.argv[1] == "inf"):
            generator("inf")
        else:
            generator(int(sys.argv[1]))
    else:
        print("Utilizzo: insulti_random.py numero_di_insulti\n" + 
        "          Inserisci inf anziche' un numero se vuoi insulti casuali continui")
