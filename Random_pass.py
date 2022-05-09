import time
import winsound
import random
Time = time.localtime()
paWs_H = str(Time.tm_hour)
paWs_M = str(Time.tm_min)
Pasww = paWs_H + paWs_M
print ('Is Locked')
Entry_PasWW = str(input('Enter the PassWord : >>>      ' ))
if Entry_PasWW == Pasww :
    print('')
    print('Is Open Now')
    print('')
    winsound.MessageBeep()
    time.sleep(8888)
elif Entry_PasWW != Pasww :
    print('')
    print('Worng Password')
    print('')
    winsound.Beep(9000 , 500)
    time.sleep(8888)





