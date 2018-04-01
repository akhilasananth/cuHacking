def compare():
    notDone = True
    line = 1

    fileC = open("coach.txt", "r")
    fileT = open("trainee.txt", "r")

    roll = 0
    pitch = 0
    yaw = 0


    while(notDone):
        rollC = fileC.readline().strip().replace(" ", "")
        if rollC == '':
            notDone = False
        else:
            rollC = int(rollC)
          #  print("rollc", int(rollC))
    

        pitchC = fileC.readline().strip().replace(" ", "")
        if pitchC == '':
            notDone = False
          #  print("didnt get here", pitchC)
        else:
            pitchC = int(pitchC)
            #print("pitchC", int(pitchC))


        yawC = fileC.readline().strip().replace(" ", "")
        if yawC == '':
            notDone = False
        else:
            yawC = int(yawC)
           # print("yawC", int(yawC))


        rollT = fileT.readline().strip().replace(" ", "")
        if rollC == '':
            notDone = False
        else:
            rollT = int(rollT)
        #print("rollT", int(rollT))


        pitchT = fileT.readline().strip().replace(" ", "")
        if pitchT == '':
            notDone = False
        else:
            pitchT = int(pitchT)
       # print("pitchT", int(pitchT))


        yawT = fileT.readline().strip().replace(" ", "")
        if yawT == '':
            notDone = False
        else:
            yawT = int(yawT)
        #rint("yawT", int(yawT))
        
        roll = (roll + (rollC - rollT))/2
        pitch = (pitch + (pitchC - pitchT))/2
        yaw = (yaw + (yawC - yawT))/2
    

        line = line + 3


    accuracy = (18 - (roll + pitch + yaw)/3)/18
    print("You are ",accuracy, "% inaccurate from the coach")

    if roll == 0:
        print("You are perfect on your twist")
    else:
        if roll > 0:
            print("you are rolling your wrist too much to the right")
        else:
            print("you are rolling your wrist too much to the left")

    if pitch == 0:
        print("You are perfect on your swing")
    else:
        if pitch > 0:
            print("you are swinging too little")
        else:
            print("you are swinging too much")
    
    if yaw == 0:
        print("You are on point")
    else:
        if yaw > 0:
            print("you are too far right")
        else:
            print("you are too far left")  
        
