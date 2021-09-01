personalInformation ={
    "name": "" ,
    "lastname" : "",
    "age" : 0 ,
    "city" : "",
    "gender" : "",
    "phonenumber" : 0,
     "birthday" : {
        "day" : 0,
        "month" : 0,
        "year" : 0
     },
    "social media" : []
}

skillsInformation = []
careerInformation = []

login = {
   "Email" : "",
   "Username" : "",
   "Password" : "",
}

def mainMenu() :
  while 1==1 :
    print("welcome to CV builder")
    print("1) lets make your personal CV ")
    print("2) view profile")
    print("3) Exit")
    chioce = input()
    if chioce == "1" :
        signup()
        CVmaker()
    elif chioce == "2" :
        logIn()  
    elif chioce == "3" :
        print("good bye ^ _ ^")

def signup() :
        login["Email"] = input("Email : ")
        login["Username"] = input("Username : ")
        login["Password"] = input("password : ")
        while 1==1 :
          loginPassword=input("enter your password again : ")
          if loginPassword in login["Password"] :
             break
          else :
           print("its wrong !")
           print("1) try again")
           print("2) i cant remeber !" +"\n"+"lets sign up again ")
           chioce = input()
           if chioce == "2" :
              signup()
 
def CVmaker() :
   print("1) personal information")
   print("2) skilles information")
   print("3) career information")
   print("4) main menu")
   chioce = input()
   if chioce == "1" : personal_info()
   elif chioce == "2" : skilles_info()    
   elif chioce == "3" : career_info()  
   elif chioce == "4" : mainMenu()
   else : CVmaker()

def personal_info() :
   print("---------------------------------------")
   for key in  personalInformation :
      if key == "age" :
          detail=int(input(key + ':'))
          personalInformation[key]= detail
      elif key == "phonenumber" :
          detail= int(input(key + ':'))
          personalInformation[key]= detail
      elif key == "birthday" :
            print("birthday information")
            year=int(input("year :"))
            personalInformation["birthday"]["year"] = year
            while 1==1 :
               month = int(input("month :"))
               if month <1 and month > 12 :
                  print("invalid number try again !")
               else :
                  personalInformation["birthday"]["month"]=month
                  break
            while 1==1 :  
               day=int(input("day :"))
               if personalInformation["birthday"]["month"] <7 :
                  if day > 31 and day <1 :
                     print("invalid number try again !")
                  else :
                     personalInformation["birthday"]["day"] = day
                     break 
               elif personalInformation["birthday"]["month"] > 6 and personalInformation["birthday"]["month"] < 12 :
                  if day > 30 and day <1 : 
                     print("invalid number try again !")
                  else :
                     personalInformation["birthday"]["day"] = day
                     break      
               else :
                   if day > 29 and day <1 : 
                     print("invalid number try again !")
                   else :
                     personalInformation["birthday"]["day"] = day 
                     break   
      elif key == "social media" :
        while 1 == 1 :
         personalInformation[key].append(input(key + ':'))
         print("do you want to enter other social media ?") 
         print("1) yes")
         print("etc. no") 
         choice = int(input())
         if choice != 1 :
          break       
      else :
          detail=input(key + ':')
          personalInformation[key]= detail
   print("---------------------------------------")
   CVmaker()
def skilles_info() :
        print("---------------------------------------")
        while 1 == 1 :
         skillsInformation.append(input("new skill : "))
         print("do you want to enter other skill ?") 
         print("1) yes")
         print("etc. no") 
         choice = int(input())
         if choice != 1 :
             break 
        print("---------------------------------------")
        CVmaker()
def career_info() :
         print("---------------------------------------")
         while 1 == 1 :
          careerInformation.append(input("new career : "))
          print("do you want to enter other career ?") 
          print("1) yes")
          print("etc. no") 
          choice = int(input())
          if choice != 1 :
              break
         print("---------------------------------------")               
         CVmaker()
def logIn() :
   
   while 1==1 :
          loginemail=input("Email : ")
          if loginemail in login["Email"] :
             break
          else :
           print("its wrong !")
   
   while 1==1 :
          loginusername=input("User name : ")
          if loginusername in login["Username"] :
             break
          else :
           print("its wrong !")
      
   while 1==1 :
          loginPassword=input("password : ")
          if loginPassword in login["Password"] :
             break
          else :
           print("its wrong !")

   profilemenu()

showInformation = 0
def profilemenu() :
   print("1) view informations")
   print("2) edit informations")
   print("3) main menu")
   chioce = int(input())
   if chioce == 1 : 
      showInformation=1
      viewInformations()     
   elif chioce == 2 : 
      showInformation = 0
      editInformations()     
   elif chioce == 3 : mainMenu()
   else : profilemenu()
      
def viewInformations() :
     print("---------------------------------------")
     n=1
     print("Personal informations :")
     for key in personalInformation.keys() :
        print(f"{n}) {key} : {personalInformation[key]}")
        n-=-1
     print("\n"+"Skills informations :")
     n=1   
     for item in skillsInformation :
        print(f"{n}) {item}")
        n-=-1
     print("\n"+"Career informations :")
     n=1   
     for item in careerInformation :
        print(f"{n}) {item}")
        n-=-1
     print("---------------------------------------")
     profilemenu()


def editInformations() :
   while 1 == 1 :
      print("1) change Personal informations") 
      print("2) Skills informations") 
      print("3) Career informations")
      print("4) Exit") 
      choice = int(input())
      if choice == 1 : personalEdit()
      elif choice == 2 : skillesEdit()
      elif choice == 3 : careerEdit()
      elif choice==4 : profilemenu()

def personalEdit() :
   print("---------------------------------------")
   print("Personal informations :")
   n=1
   for keys in personalInformation.keys() :
        print(f"{n}) {keys} : {personalInformation[keys]}")
        n-=-1
   print("---------------------------------------")
   while 1==1 :
     key=input('please enter your changing subject : ')
     if key in personalInformation.keys() : break
     else : print("its wrong !")
   
   if key == "age" :
          detail=int(input(key + ':'))
          personalInformation[key]= detail
   elif key == "phonenumber" :
          detail= int(input(key + ':'))
          personalInformation[key]= detail
   elif key == "birthday" :
            print("birthday information")
            year=int(input("year :"))
            personalInformation["birthday"]["year"] = year
            while 1==1 :
               month = int(input("month :"))
               if month <1 and month > 12 :
                  print("invalid number try again !")
               else :
                  personalInformation["birthday"]["month"]=month
                  break
            while 1==1 :  
               day=int(input("day :"))
               if personalInformation["birthday"]["month"] <7 :
                  if day > 31 and day <1 :
                     print("invalid number try again !")
                  else :
                     personalInformation["birthday"]["day"] = day
                     break 
               elif personalInformation["birthday"]["month"] > 6 and personalInformation["birthday"]["month"] < 12 :
                  if day > 30 and day <1 : 
                     print("invalid number try again !")
                  else :
                     personalInformation["birthday"]["day"] = day
                     break      
               else :
                   if day > 29 and day <1 : 
                     print("invalid number try again !")
                   else :
                     personalInformation["birthday"]["day"] = day 
                     break   
   elif key == "social media" :
        while 1 == 1 :
         personalInformation[key].append(input(key + ':'))
         print("do you want to enter other social media ?") 
         print("1) yes")
         print("etc. no") 
         choice = int(input())
         if choice != 1 :
          break       
   else :
          detail=input(key + ':')
          personalInformation[key]= detail 
   print("1) Edit another subject") 
   print("Else keybord : Exit") 
   choice = input()
   if choice == "1" : personalEdit()
   else : editInformations()

def skillesEdit() :
   print("1) New skill")
   print("2) Edit skills")
   print("3) Remove skills")
   print("4) Exit")
   choice = input()
   if choice == "1" : skilles_info()
   elif choice == "2" : editSkills()
   elif choice == "3" : removeSkills()
   elif choice == "4" :  editInformations()
   else :skillesEdit()

def editSkills() :
     print("---------------------------------------")
     print("\n"+"Skills informations :")
     n=1   
     for item in skillsInformation :
        print(f"{n}) {item}")
        n-=-1
     print("---------------------------------------")
     choise = int(input("which one do you want to change ? (choose number) \n"))
     choise-=1
     print(f"pleas enter your new text : \n previous skill text : {skillsInformation[choise]}")
     skillsInformation[choise] = input()
     print(f"new text : {skillsInformation[choise]}")
     print("1) Edit an other Skill") 
     print("Else keybord : Exit") 
     choice = input()
     if choice == "1" : editSkills()
     else : skillesEdit()

def removeSkills() :
     print("---------------------------------------")
     print("\n"+"Skills informations :")
     n=1   
     for item in skillsInformation :
        print(f"{n}) {item}")
        n-=-1
     print("---------------------------------------")
     choise = int(input("Which one do you want to remove ? (choose number) \n"))
     choise-=1
     print(f"Skill text : {skillsInformation[choise]}")
     print("Aare you sure ? \n1. yes\netc.no")
     sure = input()
     if sure == "1" : 
       skillsInformation.pop(choise)
       print("text has been removed")
       print("\n"+"Skills informations :")
       n=1   
       for item in skillsInformation :
         print(f"{n}) {item}")
         n-=-1
     print("1) Edit an other Skill") 
     print("Else keybord : Exit") 
     choice = input()
     if choice == "1" : removeSkills()
     else : skillesEdit()


def careerEdit() :
   print("1) New carear")
   print("2) Edit skills")
   print("3) Remove skills")
   print("4) Exit")
   choice = input()
   if choice == "1" : editCareer()
   elif choice == "2" : editCareer()
   elif choice == "3" : removeCareer()
   elif choice == "4" :  editInformations()
   else :careerEdit()

def editCareer() :
     print("---------------------------------------")
     print("\n"+"Career informations :")
     n=1   
     for item in careerInformation :
        print(f"{n}) {item}")
        n-=-1
     print("---------------------------------------")
     choise = int(input("which one do you want to change ? (choose number) \n"))
     choise-=1
     print(f"pleas enter your new text : \n previous career text : {careerInformation[choise]}")
     careerInformation[choise] = input()
     print(f"new text : {careerInformation[choise]}")
     print("1) Edit an other Skill") 
     print("Else keybord : Exit") 
     choice = input()
     if choice == "1" : editCareer()
     else : careerEdit()

def removeCareer() :
     print("---------------------------------------")
     print("\n"+"Career informations :")
     n=1   
     for item in careerInformation :
        print(f"{n}) {item}")
        n-=-1
     print("---------------------------------------")
     choise = int(input("Which one do you want to remove ? (choose number) \n"))
     choise-=1
     print(f"Creer text : {careerInformation[choise]}")
     print("Aare you sure ? \n1. yes\netc.no")
     sure = input()
     if sure == "1" : 
       careerInformation.pop(choise)
       print("text has been removed")
       print("\n"+"Skills informations :")
       n=1   
       for item in careerInformation :
         print(f"{n}) {item}")
         n-=-1
     print("1) Edit an other Skill") 
     print("Else keybord : Exit") 
     choice = input()
     if choice == "1" : removeCareer()
     else : careerEdit()

mainMenu()        
