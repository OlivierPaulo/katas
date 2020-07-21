def dna_to_rna(dna):
    
    rna = ""                          #initiate a empty string that will return rna string
    for letter in dna:                #looping through each character of dna string
            if letter == "T":         #testing if each letter of dna is a "T"
                    rna += "U"        #if yes, put the letter "U" inside rna string
            else:
                    rna += letter     #else, put the letter of dna inside rna string
    return rna                        #return the rna string
