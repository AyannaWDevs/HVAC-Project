#Ayanna Williams 12/7/23 ayannaWilliams_Project03
#Displays the title
def title_Display():
    disTitle = "Air Conditioning Window Unit Cooling Capacity"
    return disTitle
#calculates the area of the room 
def calc_Area(len,wid): 
    roomArea = len * wid 
    return roomArea
#accepts an integers that denotes the amount of shade and returns it as
#the string representation of the shade amount
def shade2String(s):
    if s==1:
        return "Little"
    elif s==2:
        return "Moderate" 
    elif s==3:
        return "Abundant"
 #accepts the area of a room and the amount of shade
 #a room gets and returns BTUs per hour needed to cool that room
def calculateBTUsPerHour(rmShd,u):
    if u=="Little":
        if rmShd<250:
                r=5500*0.15
                return 5500+r
        elif rmShd>=250 and rmShd<=500:
                r=10000*0.15
                return 10000+r
        elif rmShd>=501 and rmShd<=1000:
                r=17500*0.15
                return 17500+r
        elif rmShd>1000:
                r=24000*0.15
                return 24000+r

    elif u=="Moderate" :
        if rmShd<250:
            return 5500
        elif rmShd>=250 and rmShd<=500:
            return 10000
        elif rmShd>=501 and rmShd<=1000:
            return 17500
        elif rmShd>1000:
            return 24000

    elif u=="Abundant":
        if rmShd<250:
                r=5500*0.1
                return 5500-r
        elif rmShd>=250 and rmShd<=500:
                r=10000*0.1
                return 10000
        elif rmShd>=501 and rmShd<=1000:
                r=17500*0.1
                return  17500-r
        elif rmShd>1000:
                r=24000*0.1
                return 24000-r
#prints out the information for a single room
def roomInfoDisplay(strLine,nameRoom,rmShd,shadeAmount,hrBTU):   
        print()
        print(strLine)
        print("Room Name:", nameRoom)
        print("Room Area (in square feet):",rmShd)
        print("Amount of Shade: ",shadeAmount)
        print("BTU,s Per Hour needed: ",hrBTU)
        print()
 
def main():
    cnt = 0
    while True:
        cnt += 1
        roomName = input("Please enter the name of the room: ")
      
        rLen=float(input("Please enter the length of the room (in feet): "))
        while rLen<5:
            print("The length must be greater than 5, please enter again. ")
            rLen=float(input("Please enter the length of the room (in feet): "))
              
        rWid=float(input("Please enter the width of the room (in feet): "))
        while rWid<5:
            print("The width must be greater than 5, please enter again.")
            rWid=float(input("Please enter the width of the room (in feet): "))
              
        rmShd = calc_Area(rLen,rWid)
          
        print("What is the amount of shade that this room receives?")
          
        for i in range(1):
            print("1 - Little Shade")
            print("2 - Moderate Shade")
            print("3 - Abundant Shade")
            uInput=int(input("Please select from the options from above: "))
           
            defDisplay=title_Display()
                     
        shadeAmount = shade2String(uInput)
        hrlyBTU = calculateBTUsPerHour(rmShd,shadeAmount)
        display=roomInfoDisplay(defDisplay,roomName,rmShd,shadeAmount,hrlyBTU)
        anthrRm = input("Would you like to enter information for another room (Y/N)? ")
          
        if(anthrRm!='y' and anthrRm!='Y'):
            break 
    print("The total number of rooms processed was:", cnt)
       
call_main=main()  