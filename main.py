def cet_detail(k):
    if(k==1):
        print("Now fill the following details :")
        caste=input("Caste : ")
        gender=input("Gender(M/F) : ")
        print("Marks in CET")
        p=int(input("Physics : "))
        c=int(input("Chemistry : "))
        m=int(input("Maths : "))
        branch=input("Branch of your choise :")
        
        val=input("\nfor Cutoff according to category and branch, type YES else type NO : \n")
        if(val =='YES'):
            details(caste,gender,p+c+m,branch,n)
                
        elif(val =='NO'):
            final_admission(caste,gender,p+c+m,branch,n)

def prcnt_cutoff(prcnt):
    if(prcnt>=85):
        print("Congrats",n,"First criterion is fulfilled :)\n")
        sub_cutoff(math,phy,chem,eng,PE)
    else:
        print("admission canceled! your percentage is less than 85") 
    
def sub_cutoff(math,phy,chem,eng,PE):
    if(math>=75 or phy>=75 or chem>=75 or eng>=75 or PE>=75 ):
        print("Congrats",n,"Second criterion is fulfilled :)\n")
        k=1
        cet_detail(k)
    else:
        print("admission canceled! you have less than 75 marks is atleast one subject")

def prcnt(math,phy,chem,eng,PE):
    return (math+phy+chem+eng+PE)/5

def details(caste,gender,pcm,branch,n):
    print("\nFor GENERAL :\n")
    print("\t\tCSE : 280 marks , Mechanical : 260 marks , Chemical : 230 marks")
    print("   For girls :  CSE : 270 marks , Mechanical : 250 marks , Chemical : 220 marks")
    print("\nFor OBC :\n")
    print("\t\tCSE : 275 marks , Mechanical : 255 marks , Chemical : 230 marks")
    print("   For girls :  CSE : 265 marks , Mechanical : 245 marks , Chemical : 220 marks")
    print("\nFor SC/ST :\n")
    print("\t\tCSE : 230 marks , Mechanical : 200 marks , Chemical : 150 marks")
    print("   For girls :  CSE : 220 marks , Mechanical : 190 marks , Chemical : 140 marks")
    print("\nProceeding to final admission process....\n")
    final_admission(caste,gender,pcm,branch,n)

def final_admission(caste,gender,pcm,branch,n):
    if(caste=='GENERAL'):
        if(gender=='M'):
            if(branch=='CSE'):
                if(pcm>=280):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=260):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                elif(pcm>=230):
                    print("you can only get chemical branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='MECHANICAL'):
                if(pcm>=260):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=230):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='CHEMICAL'):
                if(pcm>=230):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                else:
                    print("Sorry! No Seats Available")

        if(gender=='F'):
            if(branch=='CSE'):
                if(pcm>=270):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=250):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                elif(pcm>=220):
                    print("you can only get chemical branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='MECHANICAL'):
                if(pcm>=250):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=220):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='CHEMICAL'):
                if(pcm>=220):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                else:
                    print("Sorry! No Seats Available")

    if(caste=='OBC'):
        if(gender=='M'):
            if(branch=='CSE'):
                if(pcm>=275):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=255):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                elif(pcm>=230):
                    print("you can only get chemical branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='MECHANICAL'):
                if(pcm>=255):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=230):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='CHEMICAL'):
                if(pcm>=230):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                else:
                    print("Sorry! No Seats Available")

        if(gender=='F'):
            if(branch=='CSE'):
                if(pcm>=265):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=245):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                elif(pcm>=220):
                    print("you can only get chemical branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='MECHANICAL'):
                if(pcm>=245):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=220):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='CHEMICAL'):
                if(pcm>=220):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                else:
                    print("Sorry! No Seats Available")

    if(caste=='SC'):
        if(gender=='M'):
            if(branch=='CSE'):
                if(pcm>=230):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=200):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                elif(pcm>=150):
                    print("you can only get chemical branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='MECHANICAL'):
                if(pcm>=200):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=150):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='CHEMICAL'):
                if(pcm>=150):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                else:
                    print("Sorry! No Seats Available")

        if(gender=='F'):
            if(branch=='CSE'):
                if(pcm>=220):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=190):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                elif(pcm>=140):
                    print("you can only get chemical branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='MECHANICAL'):
                if(pcm>=190):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                elif(pcm>=140):
                    print("You have not got branch of your choise, but you take admission in any lower branch")
                else:
                    print("Sorry! No Seats Available")

            if(branch=='CHEMICAL'):
                if(pcm>=140):
                    print("Congrats",n,"you have got admission in",branch,"branch")
                else:
                    print("Sorry! No Seats Available")

print("Welcome to admission process!\nplease answer the following :\n")

n=input("What is name?\n")

print("Now enter the marks in following subjects :\n")

math=int(input("Mathematics :"))
phy=int(input("Physics :"))
chem=int(input("Chemistry :"))
eng=int(input("English :"))
PE=int(input("PE :"))
k=0
prcnt=prcnt(math,phy,chem,eng,PE)
prcnt_cutoff(prcnt)
