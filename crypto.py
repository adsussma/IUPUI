#-------------------------------------------------------------------------------
# Name:        crypto.py
# Purpose:     encrypting / decrypting
#
# Author:      asussman
#
# Created:     20/06/2016
# Copyright:   (c) asussman 2016
#-------------------------------------------------------------------------------

def Encryption():

    choice = raw_input("WOULD YOU LIKE TO:" +
                        '\n' + "(E)NCRYPT" +
                        '\n' + "(D)ECRYPT" +
                        '\n' + "(Q)uit" + '\n')
    i = 0
    newString = ''

    while(True):

        encryptList = "LAKSJDHFGMZNXBCVPQOWIEURYT "
        decryptList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
################################################################################
        if choice.upper() == "E":
            toEncrypt = raw_input("PHRASE TO ENCRYPT: " + '\n')
            upEncrypt = toEncrypt.upper()
                                                                                #MAKE INPUT UPPER TO AVOID ERRORS
            if upEncrypt.isalpha() :
                while i < len(upEncrypt):                                       #WHILE THERE ARE LETTERS TO ENCRYPT,
                    eachLetter = upEncrypt[i]                                   #FOR EACH LETTER IN INPUT FIND ITS
                    b = decryptList.index(eachLetter)                           #POSITION IN 'decryptList' AND REPLACE
                    char = encryptList[b]                                       #IT WITH THE LETTER IN 'encryptList'
                    newString = newString + char                                #WITH THE SAME INDEX. THEN ITERATE TO THE
                    i = i + 1                                                   #NEXT LETTER
                placeholder = raw_input("ENCRYPTED PHRASE: %s" %newString)
                Encryption()
            else:
                pass
################################################################################
        if choice.upper() == "D":
            toDecrypt = raw_input("PHRASE TO DECRYPT: " + '\n')
            upDecrypt = toDecrypt.upper()

            if upDecrypt.isalpha():
                while i < len(upDecrypt):
                    eachLetter = upDecrypt[i]
                    a = encryptList.index(eachLetter)
                    char = decryptList[a]
                    newString = newString + char
                    i = i + 1
                placeholder = raw_input("DECRYPTED PHRASE: %s" %newString)
                Encryption()
            else:
                pass
################################################################################
        if choice.upper() == "Q":
            print "THANKS FOR USING CRYPTO.PY" + '\n'
            raw_input()
            False
            exit()
################################################################################
        else:
            placeholder = raw_input("NOT A VALID RESPONSE, TRY AGAIN" + '\n')          #PREVENT USER FROM ERRORS
            Encryption()
################################################################################
if __name__ == "__main__":
    Encryption()
                                                                                #INITIALIZE FUNCTION

