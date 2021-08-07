print("Welcome to AI store!")
print('This store is totally managed by the computer')
class grocery:
    def __init__(self,cardNo,name):
        self.cardNo=cardNo
        self.name=name
    
    def integers(self):
         print("Please choose what you would like to purchase:")
         print("1)Vegetables 2)Fruits 3)Other")
         activity=int(input("Enter activity number: "))
         if(activity==1):
            print("Clean Eats currently has in stock:")
            print("1)Tomatoes 2)Potatoes 3)Carrots 4)Eggplants 5)Bell peppers")
            answerV=int(input("Please enter the number  example 1 ,here 1 refers to tomatoes: "))
            if(answerV==1):
             print("You have purchased "+str(answerV)+')Tomatoes')
             print('The Tomatoes are available in the below measures:')
             print('Type 1 for buying 500g of Tomatoes. That would be Rs.10')
             print('Type 2 for buying 1Kg of Tomatoes. That would be Rs.20')
             print('Type 3 for buying 1.500Kg of Tomatoes. That would be Rs.30')
             print('Type 4 for buying 2Kg of Tomatoes. That would be Rs.40')
             print('Type 5 for buying 2.500Kg of Tomatoes. That would be Rs.50')
             weightTomatoes = int(input('Please enter the amount of tomatoes you wanted to buy: '))
             if(weightTomatoes==1):
              print('you have bought '+str(weightTomatoes) +')500g of tomatoes')  
              print('That would be Rs.10 as given') 
              amount=int(input("Pay: "))
              if amount<10:
                print("Insufficient funds!")
                repayamount=int(input("Please pay again: "))
                if repayamount<10:
                  print("Insufficient funds!")
                  print('You are not having sufficient funds...Visit again Later...')
                elif repayamount>10:
                  new_amount=repayamount-10
                  print( "Thank you. Your change is Rs."+str(new_amount))
                  print('You may expect your delivery within an hour.') 
                else:
                   print('You may expect your delivery within an hour')
                   print('Thank you! visit again...')
              elif amount>10:
                    new_amount=amount-10
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print('You may expect your delivery within an hour.')
              else:
                print('Thank you! you may expect your delivery within an hour')
                print('Visit again Later...') 
             if(weightTomatoes==2):
                 print('you have bought '+str(weightTomatoes)+')1Kg of tomatoes')     
                 print('That would be Rs.20 as given')
                 amount=int(input("Pay: "))
                 if amount<20:
                  print("Insufficient funds!")
                  repayamount=int(input("Please pay again: "))
                  if repayamount<20:
                    print("Insufficient funds!")
                    print('You are not having sufficient funds...Visit again Later...')
                  elif repayamount>20:
                    new_amount=repayamount-20
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print('You may expect your delivery within an hour.') 
                  else:
                    print('You may expect your delivery within an hour')
                    print('Thank you! visit again later...')         
                 elif amount>20:
                    new_amount=amount-20
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print('You may expect your delivery within 1-2 hours.')
                 else:
                    print('You may expect your delivery within 1-2 hours.')
                    print('Thank you! visit again later...')
             if(weightTomatoes==3):
                 print('you have bought '+str(weightTomatoes)+')1.500Kg of tomatoes')     
                 print('That would be Rs.30 as given')
                 amount=int(input("Pay: "))
                 if amount<30:
                  print("Insufficient funds!")
                  repayamount=int(input("Please pay again: "))
                  if repayamount<30:
                    print("Insufficient funds!")
                    print('You are not having sufficient funds...Visit again Later...')
                  elif repayamount>30:
                    new_amount=repayamount-30
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print('You may expect your delivery within an hour.') 
                  else:
                   print('You may expect your delivery within 2-3 hour')
                   print('Thank you! visit again...')        
                 elif amount>30:
                    new_amount=amount-30
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print('You may expect your delivery within 2-3 hours.')
                 else:
                    print('You may expect your delivery within 2-3 hours.')
                    print('Thank you! visit again later...')
             if(weightTomatoes==4):
                 print('you have bought '+str(weightTomatoes)+')2Kg of tomatoes')     
                 print('That would be Rs.40 as given')
                 amount=int(input("Pay: "))
                 if amount<40:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<40:
                     print("Insufficient funds!")
                     print('You are not having sufficient funds...Visit again Later...') 
                    elif repayamount>40:
                     new_amount=repayamount-40
                     print('Thank you. Your change is Rs.'+str(new_amount))
                    else:
                      print('You may expect your delivery within 3-4 hours')
                      print('Thank you! visit again Later...')  
                 elif amount>40:
                    new_amount=amount-40
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print('You may expect your delivery within 3-4 hours.')
                 else:
                    print("Thank you! You may expect your delivery within 3-4 hours.")
             if(weightTomatoes==5):
                 print('you have bought '+str(weightTomatoes)+')2.500Kg of tomatoes')     
                 print('That would be Rs.50 as given')
                 amount=int(input("Pay: "))
                 if amount<50:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<50:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...') 
                    elif repayamount>50:
                        new_amount=amount-50
                        print('Thank you! your change is Rs.'+str(new_amount))
                        print('You may expect your delivery within 4-5 hours.')   
                    else:
                        print('You may expect your delivery within 4-5 hours.')
                        print('Thank you! visit again later...')
                 elif amount>50:
                    new_amount=amount-50
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print('You may expect your delivery within 4-5 hours.')
                 else:
                    print("Thank you! You may expect your delivery within 4-5 hours.")
                    print('visit again Later...')
             if(weightTomatoes>5):
                   print('Oops! You can only buy upto 2.500kg of tomatoes')
                   print('Sorry! Visit again Later...') 
            if(answerV==2):
             print("You have purchased "+str(answerV) +')Potatoes') 
             print('The Tomatoes are available in the below measures:')
             print('Type 1 for buying 500g of Potatoes. That would be Rs.15')
             print('Type 2 for buying 1Kg of Potatoes. That would be Rs.30')
             print('Type 3 for buying 1.500Kg of Potatoes. That would be Rs.45')
             print('Type 4 for buying 2Kg of Potatoes. That would be Rs.60')
             print('Type 5 for buying 2.500Kg of Potatoes. That would be Rs.75')
             weightPotatoes = int(input('Please enter the amount of potatoes you wanted to buy: '))
             if(weightPotatoes==1):
              print('you have bought '+str(weightPotatoes)+')500g of potatoes')  
              print('That would be Rs.15 as given') 
              amount=int(input("Pay: "))
              if amount<15:
                print("Insufficient funds!")
                repayamount=int(input("Please pay again: "))
                if repayamount<15:
                    print("Insufficient funds!")
                    print('You are not having sufficient funds...Visit again Later...')
                elif repayamount>15:
                    new_amount=repayamount-15
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within an hour.")
                else:
                    print('Thank you! You may expect your delivery within an hour.')
              elif amount>15:
                    new_amount=amount-15
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within an hour.")
              else:
                   print("Thank you! You may expect your delivery within an hour.")     
             if(weightPotatoes==2):
                 print('you have bought '+str(weightPotatoes)+')1Kg of potatoes')     
                 print('That would be Rs.30 as given')
                 amount=int(input("Pay: "))
                 if amount<30:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<30:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                    elif repayamount>30:
                       new_amount=repayamount-30
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print("Thank you! You may expect your delivery within 1-2 hours.")     
                    else:
                       print("Thank you! You may expect your delivery within 1-2 hours.")    
                 elif amount>30:
                    new_amount=amount-30
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 1-2 hours.")
                 else:
                    print("Thank you! You may expect your delivery within 1-2 hours.")
             if(weightPotatoes==3):
                 print('you have bought '+str(weightPotatoes)+')1.500Kg of potatoes')     
                 print('That would be Rs.45 as given')
                 amount=int(input("Pay: "))
                 if amount<45:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<45:
                      print("Insufficient funds!")
                      print('You are not having sufficient funds...Visit again Later...') 
                    elif repayamount>45:
                     new_amount=repayamount-45
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print("Thank you! You may expect your delivery within 2-3 hours.")   
                    else:
                     print('Thank you! You may expect your delivery within 2-3 hours.')      
                 elif amount>45:
                    new_amount=amount-45
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 2-3 hours.")
                 else:
                    print("Thank you! You may expect your delivery within 2-3 hours.")
             if(weightPotatoes==4):
                 print('you have bought '+str(weightPotatoes)+')2Kg of potatoes')     
                 print('That would be Rs.40 as given')
                 amount=int(input("Pay: "))
                 if amount<60:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<60:
                     print("Insufficient funds!")
                     print('You are not having sufficient funds...Visit again Later...')
                    elif repayamount>60:
                     new_amount=repayamount-60
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print("Thank you! You may expect your delivery within 3-4 hours.")
                    else:
                     print('Thank you! You may expect your delivery within 3-4 hours.')           
                 elif amount>60:
                    new_amount=amount-60
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 3-4 hours.")
                 else:
                    print("Thank you! You may expect your delivery within 3-4 hours.")
             if(weightPotatoes==5):
                 print('you have bought '+str(weightPotatoes)+')2.500Kg of potatoes')     
                 print('That would be Rs.75 as given')
                 amount=int(input("Pay: "))
                 if amount<75:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<75:
                      print("Insufficient funds!")
                      print('You are not having sufficient funds...Visit again Later...')
                    elif repayamount>75:
                     new_amount=repayamount-75
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print("Thank you! You may expect your delivery within 4-5 hours.")
                    else:
                     print('Thank you! You may expect your delivery within 4-5 hours.')         
                 elif amount>75:
                    new_amount=amount-75
                    print( "Thank you. Your change is Rs."+str(new_amount))
                 else:
                    print("Thank you! You may expect your delivery within 4-5 hours.")
             if(weightPotatoes>5):
                   print('Oops! You can only buy upto 2.500kg of potatoes')
                   print('Sorry! Visit again Later...') 
            if(answerV==3):
                print("You have purchased "+str(answerV) +')Carrots') 
                print('The Carrots are available in the below measures:')
                print('Type 2 for buying 1Kg of Carrots. That would be Rs.30')
                print('Type 3 for buying 1.500Kg of Carrots. That would be Rs.45')
                print('Type 4 for buying 2Kg of Carrots. That would be Rs.60')
                print('Type 5 for buying 2.500Kg of Carrots. That would be Rs.75')
                weightCarrots = int(input('Please enter the amount of Carrots you wanted to buy: ')) 
                if(weightCarrots==1):
                    print('you have bought '+str(weightCarrots)+')500g of Carrots')  
                    print('That would be Rs.15 as given') 
                    amount=int(input("Pay: "))
                    if amount<15:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<15:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...') 
                       elif repayamount>15:
                         new_amount=repayamount-15
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print("Thank you! You may expect your delivery within an hour.")
                       else:
                         print("Thank you! You may expect your delivery within an hour.")
                elif amount>15:
                    new_amount=amount-15
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within an hour.")
                else:
                   print("Thank you! You may expect your delivery within an hour.")
                if(weightCarrots==2):
                  print('you have bought '+str(weightCarrots)+')1Kg of Carrots')     
                  print('That would be Rs.30 as given')
                  amount=int(input("Pay: "))
                  if amount<30:
                     print("Insufficient funds!")
                     repayamount=int(input("Please pay again: "))
                     if repayamount<30:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...') 
                     elif repayamount>30:
                       new_amount=repayamount-30
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print("Thank you! You may expect your delivery within 1-2 hours.")
                     else:
                       print("Thank you! You may expect your delivery within 1-2 hours.")        
                  elif amount>30:
                    new_amount=amount-30
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 1-2 hours.")
                  else:
                    print("Thank you! You may expect your delivery within 1-2 hours.")
                if(weightCarrots==3):
                   print('you have bought '+str(weightCarrots)+')1.500Kg of Carrots')     
                   print('That would be Rs.45 as given')
                   amount=int(input("Pay: "))
                   if amount<45:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<45:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')  
                      elif repayamount>45:
                        new_amount=repayamount-45
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print("Thank you! You may expect your delivery within 2-3 hours.")
                      else:
                        print("Thank you! You may expect your delivery within 2-3 hours.")        
                   elif amount>45:
                    new_amount=amount-45
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 2-3 hours.")
                   else:
                    print("Thank you! You may expect your delivery within 2-3 hours.")
                if(weightCarrots==4):
                 print('you have bought '+str(weightCarrots)+')2Kg of Carrots')     
                 print('That would be Rs.40 as given')
                 amount=int(input("Pay: "))
                 if amount<60:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<60:
                      print("Insufficient funds!")
                      print('You are not having sufficient funds...Visit again Later...') 
                    elif repayamount>60:
                      new_amount=repayamount-60
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print("Thank you! You may expect your delivery within 3-4 hours.")
                    else:
                      print("Thank you! You may expect your delivery within 3-4 hours.")          
                 elif amount>60:
                    new_amount=amount-60
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 3-4 hours.")
                 else:
                    print("Thank you! You may expect your delivery within 3-4 hours.")
                if(weightCarrots==5):
                   print('you have bought '+str(weightCarrots)+')2.500Kg of Carrots')     
                   print('That would be Rs.75 as given')
                   amount=int(input("Pay: "))
                   if amount<75:
                     print("Insufficient funds!")
                     repayamount=int(input("Please pay again: "))
                     if repayamount<75:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                     elif repayamount>75:
                       new_amount=repayamount-75
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 4-5 hours')
                     else:
                       print("Thank you! You may expect your delivery within 4-5 hours.")
                   elif amount>75:
                       new_amount=amount-75
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 4-5 hours')
                   else:
                       print("Thank you! You may expect your delivery within 4-5 hours.") 
                if(weightCarrots>5):
                   print('Oops! You can only buy upto 2.500kg of carrots')
                   print('Sorry! Visit again Later...')       
            if(answerV==4):
                print("You have purchased "+str(answerV) +')EggPlants') 
                print('The EggPlants are available in the below measures:')
                print('Type 1 for buying 500g of EggPlants. That would be Rs.20')
                print('Type 2 for buying 1Kg of EggPlants. That would be Rs.40')
                print('Type 3 for buying 1.500Kg of EggPlants. That would be Rs.60')
                print('Type 4 for buying 2Kg of EggPlants. That would be Rs.80')
                print('Type 5 for buying 2.500Kg of EggPlants. That would be Rs.100')
                weightEggPlants = int(input('Please enter the amount of EggPlants you wanted to buy: ')) 
                if(weightEggPlants==1):
                    print('you have bought '+str(weightEggPlants)+')500g of EggPlants')  
                    print('That would be Rs.20 as given') 
                    amount=int(input("Pay: "))
                    if amount<20:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<20:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>20:
                         new_amount=repayamount-20
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print("Thank you! You may expect your delivery within an hour.")
                       else:
                         print("Thank you! You may expect your delivery within an hour.") 
                    elif amount>20:
                       new_amount=amount-20
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print("Thank you! You may expect your delivery within an hour.")
                    else:
                       print("Thank you! You may expect your delivery within an hour.")
                if(weightEggPlants==2):
                  print('you have bought '+str(weightEggPlants)+')1Kg of EggPlants')     
                  print('That would be Rs.40 as given')
                  amount=int(input("Pay: "))
                  if amount<40:
                     print("Insufficient funds!")
                     repayamount=int(input("Please pay again: "))
                     if repayamount<40:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                     elif repayamount>40:
                       new_amount=repayamount-40
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print("Thank you! You may expect your delivery within 1-2 hours.") 
                     else:
                       print("Thank you! You may expect your delivery within 1-2 hours.")         
                  elif amount>40:
                    new_amount=amount-40
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 1-2 hours.")
                  else:
                    print("Thank you! You may expect your delivery within 1-2 hours.")
                if(weightEggPlants==3):
                   print('you have bought '+str(weightEggPlants)+')1.500Kg of EggPlants')     
                   print('That would be Rs.60 as given')
                   amount=int(input("Pay: "))
                   if amount<60:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<60:
                          print("Insufficient funds!")
                          print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>60:
                          new_amount=repayamount-60
                          print( "Thank you. Your change is Rs."+str(new_amount))
                          print("Thank you! You may expect your delivery within 2-3 hours.")
                      else:
                          print("Thank you! You may expect your delivery within 2-3 hours.")        
                   elif amount>60:
                      new_amount=amount-60
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print("Thank you! You may expect your delivery within 2-3 hours.")
                   else:
                      print("Thank you! You may expect your delivery within 2-3 hours.")
                if(weightEggPlants==4):
                 print('you have bought '+str(weightEggPlants)+')2Kg of EggPlants')     
                 print('That would be Rs.80 as given')
                 amount=int(input("Pay: "))
                 if amount<80:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<80:
                      print("Insufficient funds!")
                      print('You are not having sufficient funds...Visit again Later...')
                    elif repayamount>80:
                      new_amount=repayamount-80
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print("Thank you! You may expect your delivery within 3-4 hours.")
                    else:
                      print("Thank you! You may expect your delivery within 3-4 hours.")        
                 elif amount>80:
                    new_amount=amount-80
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 3-4 hours.")
                 else:
                    print("Thank you! You may expect your delivery within 3-4 hours.")
                if(weightEggPlants==5):
                   print('you have bought '+str(weightEggPlants)+')2.500Kg of EggPlants')     
                   print('That would be Rs.100 as given')
                   amount=int(input("Pay: "))
                   if amount<100:
                     print("Insufficient funds!")
                     repayamount=int(input("Please pay again: "))
                     if repayamount<100:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                     elif repayamount>100:
                       new_amount=repayamount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))  
                       print('Thank you! you may expect your delivery within 4-5 hours')
                     else:
                        print('Thank you! you may expect your delivery within 4-5 hours')       
                   elif amount>100:
                       new_amount=amount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('Thank you! you may expect your delivery within 4-5 hours')
                   else:
                       print("Thank you! You may expect your delivery within 4-5 hours.") 
                if(weightEggPlants>5):
                   print('Oops! You can only buy upto 2.500kg of Eggplants')
                   print('Sorry! Visit again Later...')           
            if(answerV==5):
                print("You have purchased "+str(answerV) +')Bell Peppers') 
                print('The Bell Peppers are available in the below measures:')
                print('Type 1 for buying 500g of Bell Peppers. That would be Rs.20')
                print('Type 2 for buying 1Kg of Bell Peppers. That would be Rs.40')
                print('Type 3 for buying 1.500Kg of Bell Peppers. That would be Rs.60')
                print('Type 4 for buying 2Kg of Bell Peppers. That would be Rs.80')
                print('Type 5 for buying 2.500Kg of Bell Peppers. That would be Rs.100')
                weightBellPeppers = int(input('Please enter the amount of Bell Peppers you wanted to buy: ')) 
                if(weightBellPeppers==1):
                    print('you have bought '+str(weightBellPeppers)+')500g of BellPeppers')  
                    print('That would be Rs.20 as given') 
                    amount=int(input("Pay: "))
                    if amount<20:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<20:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>20:
                         new_amount=repayamount-20
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print("Thank you! You may expect your delivery within an hour.") 
                       else:
                         print("Thank you! You may expect your delivery within an hour.") 
                    elif amount>20:
                       new_amount=amount-20
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print("Thank you! You may expect your delivery within an hour.")
                    else:
                       print("Thank you! You may expect your delivery within an hour.")
                if(weightBellPeppers==2):
                  print('you have bought '+str(weightBellPeppers)+')1Kg of BellPeppers')     
                  print('That would be Rs.40 as given')
                  amount=int(input("Pay: "))
                  if amount<40:
                     print("Insufficient funds!")
                     repayamount=int(input("Please pay again: "))
                     if repayamount<40:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...') 
                     elif repayamount>40:
                       new_amount=repayamount-40
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print("Thank you! You may expect your delivery within 1-2 hours.") 
                     else:
                       print('Thank you! You may expect your delivery within 1-2 hours.')       
                  elif amount>40:
                    new_amount=amount-40
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 1-2 hours.")
                  else:
                    print("Thank you! You may expect your delivery within 1-2 hours.")
                if(weightBellPeppers==3):
                   print('you have bought '+str(weightBellPeppers)+')1.500Kg of BellPeppers')     
                   print('That would be Rs.60 as given')
                   amount=int(input("Pay: "))
                   if amount<60:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<60:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>60:
                        new_amount=repayamount-60
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print("Thank you! You may expect your delivery within 2-3 hours.")
                      else:
                        print("Thank you! You may expect your delivery within 2-3 hours.")          
                   elif amount>60:
                     new_amount=amount-60
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print("Thank you! You may expect your delivery within 2-3 hours.")
                   else:
                     print("Thank you! You may expect your delivery within 2-3 hours.")
                if(weightBellPeppers==4):
                 print('you have bought '+str(weightBellPeppers)+')2Kg of BellPeppers')     
                 print('That would be Rs.80 as given')
                 amount=int(input("Pay: "))
                 if amount<80:
                    print("Insufficient funds!")
                    repayamount=int(input("Please pay again: "))
                    if repayamount<80:
                      print("Insufficient funds!")
                      print('You are not having sufficient funds...Visit again Later...')   
                    elif repayamount>80:
                      new_amount=repayamount-80
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print("Thank you! You may expect your delivery within 3-4 hours.")
                    else:
                      print("Thank you! You may expect your delivery within 3-4 hours.")     
                 elif amount>80:
                    new_amount=amount-80
                    print( "Thank you. Your change is Rs."+str(new_amount))
                    print("Thank you! You may expect your delivery within 3-4 hours.")
                 else:
                    print("Thank you! You may expect your delivery within 3-4 hours.")
                if(weightBellPeppers==5):
                   print('you have bought '+str(weightBellPeppers)+')2.500Kg of BellPeppers')     
                   print('That would be Rs.100 as given')
                   amount=int(input("Pay: "))
                   if amount<100:
                     print("Insufficient funds!")
                     repayamount=int(input("Please pay again: "))
                     if repayamount<100:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                     elif repayamount>100:
                       new_amount=repayamount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 4-5 hours.')
                     else:
                       print('Thank you! You may expect your delivery within 4-5 hours.')        
                   elif amount>100:
                       new_amount=amount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                   else:
                       print("Thank you! You may expect your delivery within 4-5 hours.") 
                if(weightBellPeppers>5):
                   print('Oops! You can only buy upto 2.500kg of bellpeppers')
                   print('Sorry! Visit again Later...')     
            if(answerV>5):
                print('Oops! We dont have any other veggies...')
                print('Sorry!')
         elif(activity==2): 
            print("Clean Eats currently has in stock:")
            print("1)Oranges 2)Apples 3)Bananas 4)Mangoes 5)Grapes")
            answer=int(input("Please enter the number (example 1 ,here 1 refers to Oranges):"))
            if(answer==1):
                 print("You have purchased "+str(answer)+')Oranges')
                 print('The Oranges are available in the below measures:')
                 print('Type 1 for buying 500g of Oranges. That would be Rs.50')
                 print('Type 2 for buying 1Kg of Oranges. That would be Rs.100')
                 print('Type 3 for buying 1.500Kg of Oranges. That would be Rs.150')
                 print('Type 4 for buying 2Kg of Oranges. That would be Rs.200')
                 print('Type 5 for buying 2.500Kg of Oranges. That would be Rs.250')
                 weightOranges = int(input('Please enter the amount of oranges you wanted to buy: '))
                 if(weightOranges==1):
                    print('you have bought '+str(weightOranges) +')500g of Oranges')  
                    print('That would be Rs.50 as given') 
                    amount=int(input("Pay: "))
                    if amount<50:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<50:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>50:
                        new_amount=repayamount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.') 
                       else:
                        print('You may expect your delivery within an hour.') 
                    elif amount>50:
                        new_amount=amount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                    else:
                        print("Thank you! You may expect your delivery within an hour..")
                 if(weightOranges==2):
                    print('you have bought '+str(weightOranges)+')1Kg of Oranges')     
                    print('That would be Rs.100 as given')
                    amount=int(input("Pay: "))
                    if amount<100:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<100:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...') 
                      elif repayamount>100:
                       new_amount=repayamount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')
                      else:
                        print('Thank you! You may expect your delivery within 1-2 hours')      
                    elif amount>100:
                       new_amount=amount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')
                    else:
                       print('Thank you! You may expect your delivery within 1-2 hours.')
                 if(weightOranges==3):
                    print('you have bought '+str(weightOranges)+')1.500Kg of Oranges')     
                    print('That would be Rs.150 as given')
                    amount=int(input("Pay: "))
                    if amount<150:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<150:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>150:
                       new_amount = repayamount-150
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 2-3 hours.') 
                      else:
                       print('Thank you! you may expect your delivery within 2-3 hours')         
                    elif amount>150:
                      new_amount=amount-150
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 2-3 hours.')
                    else:
                      print('You may expect your delivery within 2-3 hours.')
                 if(weightOranges==4):
                    print('you have bought '+str(weightOranges)+')2Kg of Oranges')     
                    print('That would be Rs.200 as given')
                    amount=int(input("Pay: "))
                    if amount<200:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<200:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>200:
                        new_amount=repayamount-200
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 3-4 hours.')
                      else:
                         print("Thank you! You may expect your delivery within 3-4 hours.")          
                    elif amount>200:
                      new_amount=amount-200
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 3-4 hours.')
                    else:
                      print("Thank you! You may expect your delivery within 3-4 hours.")
                 if(weightOranges==5):
                    print('you have bought '+str(weightOranges)+')2.500Kg of Oranges')     
                    print('That would be Rs.250 as given')
                    amount=int(input("Pay: "))
                    if amount<250:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<250:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>250:
                         new_amount=repayamount-250
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within 4-5 hours.') 
                       else:
                         print("Thank you! You may expect your delivery within 4-5 hours.")          
                    elif amount>250:
                      new_amount=amount-250
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 4-5 hours.')
                    else:
                      print("Thank you! You may expect your delivery within 4-5 hours.")
                 if(weightOranges>5):
                   print('Oops! You can only buy upto 2.500kg of oranges')
                   print('Sorry! Visit again Later...') 
            if(answer==2):
                 print("You have purchased "+str(answer)+')Apples')
                 print('The Apples are available in the below measures:')
                 print('Type 1 for buying 500g of Apples. That would be Rs.50')
                 print('Type 2 for buying 1Kg of Apples. That would be Rs.100')
                 print('Type 3 for buying 1.500Kg of Apples. That would be Rs.150')
                 print('Type 4 for buying 2Kg of Apples. That would be Rs.200')
                 print('Type 5 for buying 2.500Kg of Apples. That would be Rs.250')
                 weightApples = int(input('Please enter the amount of Apples you wanted to buy: '))
                 if(weightApples==1):
                    print('you have bought '+str(weightApples) +')500g of Apples')  
                    print('That would be Rs.50 as given') 
                    amount=int(input("Pay: "))
                    if amount<50:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<50:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>50:
                        new_amount=repayamount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.') 
                       else:
                         print("Thank you! You may expect your delivery within an hour..")
                    elif amount>50:
                        new_amount=amount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                    else:
                        print("Thank you! You may expect your delivery within an hour..")
                 if(weightApples==2):
                    print('you have bought '+str(weightApples)+')1Kg of Apples')     
                    print('That would be Rs.100 as given')
                    amount=int(input("Pay: "))
                    if amount<100:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<100:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>100:
                       new_amount=repayamount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')
                      else:
                       print('You may expect your delivery within 1-2 hours.')         
                    elif amount>100:
                       new_amount=amount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')
                    else:
                       print('You may expect your delivery within 1-2 hours.')
                 if(weightApples==3):
                    print('you have bought '+str(weightApples)+')1.500Kg of Apples')     
                    print('That would be Rs.150 as given')
                    amount=int(input("Pay: "))
                    if amount<150:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<150:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>150:
                       new_amount=repayamount-150
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 2-3 hours.')  
                      else:
                       print('You may expect your delivery within 2-3 hours.')       
                    elif amount>150:
                      new_amount=amount-150
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 2-3 hours.')
                    else:
                      print('You may expect your delivery within 2-3 hours.')
                 if(weightApples==4):
                    print('you have bought '+str(weightApples)+')2Kg of Apples')     
                    print('That would be Rs.200 as given')
                    amount=int(input("Pay: "))
                    if amount<200:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<200:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>200:
                        new_amount=repayamount-200
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 3-4 hours.') 
                      else:
                        print("Thank you! You may expect your delivery within 3-4 hours.")        
                    elif amount>200:
                      new_amount=amount-200
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 3-4 hours.')
                    else:
                      print("Thank you! You may expect your delivery within 3-4 hours.")
                 if(weightApples==5):
                    print('you have bought '+str(weightApples)+')2.500Kg of Apples')     
                    print('That would be Rs.250 as given')
                    amount=int(input("Pay: "))
                    if amount<250:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<250:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...') 
                       elif repayamount>250:
                         new_amount=repayamount-250
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within 4-5 hours.') 
                       else:
                         print("Thank you! You may expect your delivery within 4-5 hours.")        
                    elif amount>250:
                        new_amount=amount-250
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 4-5 hours.')
                    else:
                        print("Thank you! You may expect your delivery within 4-5 hours.")
                 if(weightApples>5):
                   print('Oops! You can only buy upto 2.500kg of apples')
                   print('Sorry! Visit again Later...') 
            if(answer==3):
                 print("You have purchased "+str(answer)+')Bananas')
                 print('The Bananas are available in the below measures:')
                 print('Type 1 for buying 500g of Bananas. That would be Rs.50')
                 print('Type 2 for buying 1Kg of Bananas. That would be Rs.100')
                 print('Type 3 for buying 1.500Kg of Bananas. That would be Rs.150')
                 print('Type 4 for buying 2Kg of Bananas. That would be Rs.200')
                 print('Type 5 for buying 2.500Kg of Bananas. That would be Rs.250')
                 weightBananas = int(input('Please enter the amount of Bananas you wanted to buy: '))
                 if(weightBananas==1):
                    print('you have bought '+str(weightBananas) +')500g of Bananas')  
                    print('That would be Rs.50 as given') 
                    amount=int(input("Pay: "))
                    if amount<50:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<50:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>50:
                        new_amount=repayamount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                       else:
                        print("Thank you! You may expect your delivery within an hour..") 
                    elif amount>50:
                        new_amount=amount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                    else:
                        print("Thank you! You may expect your delivery within an hour..")
                 if(weightBananas==2):
                    print('you have bought '+str(weightBananas)+')1Kg of Bananas')     
                    print('That would be Rs.100 as given')
                    amount=int(input("Pay: "))
                    if amount<100:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<100:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>100:
                       new_amount=repayamount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')
                      else:
                       print('You may expect your delivery within 1-2 hours.')          
                    elif amount>100:
                       new_amount=amount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')
                    else:
                       print('You may expect your delivery within 1-2 hours.')
                 if(weightBananas==3):
                    print('you have bought '+str(weightBananas)+')1.500Kg of Bananas')     
                    print('That would be Rs.150 as given')
                    amount=int(input("Pay: "))
                    if amount<150:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<150:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>150:
                       new_amount=repayamount-150
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 2-3 hours.') 
                      else:
                        print('You may expect your delivery within 2-3 hours.')      
                    elif amount>150:
                      new_amount=amount-150
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 2-3 hours.')
                    else:
                      print('You may expect your delivery within 2-3 hours.')
                 if(weightBananas==4):
                    print('you have bought '+str(weightBananas)+')2Kg of Bananas')     
                    print('That would be Rs.200 as given')
                    amount=int(input("Pay: "))
                    if amount<200:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<200:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...') 
                      elif repayamount>200:
                        new_amount=repayamount-200
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 3-4 hours.') 
                      else:
                         print("Thank you! You may expect your delivery within 3-4 hours.")       
                    elif amount>200:
                      new_amount=amount-200
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 3-4 hours.')
                    else:
                      print("Thank you! You may expect your delivery within 3-4 hours.")
                 if(weightBananas==5):
                    print('you have bought '+str(weightBananas)+')2.500Kg of Bananas')     
                    print('That would be Rs.250 as given')
                    amount=int(input("Pay: "))
                    if amount<250:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<250:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>250:
                         new_amount=repayamount-250
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within 4-5 hours.') 
                       else:
                         print("Thank you! You may expect your delivery within 4-5 hours.")       
                    elif amount>250:
                        new_amount=amount-250
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 4-5 hours.')
                    else:
                        print("Thank you! You may expect your delivery within 4-5 hours.")
                 if(weightBananas>5):
                   print('Oops! You can only buy upto 2.500kg of bananas')
                   print('Sorry! Visit again Later...') 
            if(answer==4):
                 print("You have purchased "+str(answer)+')Mangoes')
                 print('The Mangoes are available in the below measures:')
                 print('Type 1 for buying 500g of Mangoes. That would be Rs.50')
                 print('Type 2 for buying 1Kg of Mangoes. That would be Rs.100')
                 print('Type 3 for buying 1.500Kg of Mangoes. That would be Rs.150')
                 print('Type 4 for buying 2Kg of Mangoes. That would be Rs.200')
                 print('Type 5 for buying 2.500Kg of Mangoes. That would be Rs.250')
                 weightMangoes = int(input('Please enter the amount of Mangoes you wanted to buy: '))
                 if(weightMangoes==1):
                    print('you have bought '+str(weightMangoes) +')500g of Mangoes')  
                    print('That would be Rs.50 as given') 
                    amount=int(input("Pay: "))
                    if amount<50:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<50:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>50:
                        new_amount=repayamount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                       else:
                        print("Thank you! You may expect your delivery within an hour..") 
                    elif amount>50:
                        new_amount=amount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                    else:
                        print("Thank you! You may expect your delivery within an hour..")
                 if(weightMangoes==2):
                    print('you have bought '+str(weightMangoes)+')1Kg of Mangoes')     
                    print('That would be Rs.100 as given')
                    amount=int(input("Pay: "))
                    if amount<100:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<100:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>100:
                       new_amount=repayamount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.') 
                      else:
                        print('You may expect your delivery within 1-2 hours.')        
                    elif amount>100:
                       new_amount=amount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')
                    else:
                       print('You may expect your delivery within 1-2 hours.')
                 if(weightMangoes==3):
                    print('you have bought '+str(weightMangoes)+')1.500Kg of Mangoes')     
                    print('That would be Rs.150 as given')
                    amount=int(input("Pay: "))
                    if amount<150:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<150:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>150:
                       new_amount=repayamount-150
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 2-3 hours.')   
                      else:
                        print('You may expect your delivery within 2-3 hours.')      
                    elif amount>150:
                      new_amount=amount-150
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 2-3 hours.')
                    else:
                      print('You may expect your delivery within 2-3 hours.')
                 if(weightMangoes==4):
                    print('you have bought '+str(weightMangoes)+')2Kg of Mangoes')     
                    print('That would be Rs.200 as given')
                    amount=int(input("Pay: "))
                    if amount<200:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<200:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>200:
                        new_amount=repayamount-200
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 3-4 hours.')  
                      else:
                        print("Thank you! You may expect your delivery within 3-4 hours.")        
                    elif amount>200:
                      new_amount=amount-200
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 3-4 hours.')
                    else:
                      print("Thank you! You may expect your delivery within 3-4 hours.")
                 if(weightMangoes==5):
                    print('you have bought '+str(weightMangoes)+')2.500Kg of Mangoes')     
                    print('That would be Rs.250 as given')
                    amount=int(input("Pay: "))
                    if amount<250:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<250:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>250:
                         new_amount=repayamount-250
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within 4-5 hours.') 
                       else:
                         print("Thank you! You may expect your delivery within 4-5 hours.")         
                    elif amount>250:
                        new_amount=amount-250
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 4-5 hours.')
                    else:
                        print("Thank you! You may expect your delivery within 4-5 hours.")
                 if(weightMangoes>5):
                   print('Oops! You can only buy upto 2.500kg of Mangoes')
                   print('Sorry! Visit again Later...') 
            if(answer==5):
                 print("You have purchased "+str(answer)+')Grapes')
                 print('The Grapes are available in the below measures:')
                 print('Type 1 for buying 500g of Grapes. That would be Rs.50')
                 print('Type 2 for buying 1Kg of Grapes. That would be Rs.100')
                 print('Type 3 for buying 1.500Kg of Grapes. That would be Rs.150')
                 print('Type 4 for buying 2Kg of Grapes. That would be Rs.200')
                 print('Type 5 for buying 2.500Kg of Grapes. That would be Rs.250')
                 weightGrapes = int(input('Please enter the amount of Grapes you wanted to buy: '))
                 if(weightGrapes==1):
                    print('you have bought '+str(weightGrapes) +')500g of Grapes')  
                    print('That would be Rs.50 as given') 
                    amount=int(input("Pay: "))
                    if amount<50:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<50:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>50:
                        new_amount=repayamount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                       else:
                        print("Thank you! You may expect your delivery within an hour..") 
                    elif amount>50:
                        new_amount=amount-50
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                    else:
                        print("Thank you! You may expect your delivery within an hour..")
                 if(weightGrapes==2):
                    print('you have bought '+str(weightGrapes)+')1Kg of Grapes')     
                    print('That would be Rs.100 as given')
                    amount=int(input("Pay: "))
                    if amount<100:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<100:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>100:
                       new_amount=repayamount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')  
                      else:
                       print('You may expect your delivery within 1-2 hours.')       
                    elif amount>100:
                       new_amount=amount-100
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 1-2 hours.')
                    else:
                       print('You may expect your delivery within 1-2 hours.')
                 if(weightGrapes==3):
                    print('you have bought '+str(weightGrapes)+')1.500Kg of Grapes')     
                    print('That would be Rs.150 as given')
                    amount=int(input("Pay: "))
                    if amount<150:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<150:
                       print("Insufficient funds!")
                       print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>150:
                       new_amount=repayamount-150
                       print( "Thank you. Your change is Rs."+str(new_amount))
                       print('You may expect your delivery within 2-3 hours.')
                      else:
                       print('You may expect your delivery within 2-3 hours.')        
                    elif amount>150:
                      new_amount=amount-150
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 2-3 hours.')
                    else:
                      print('You may expect your delivery within 2-3 hours.')
                 if(weightGrapes==4):
                    print('you have bought '+str(weightGrapes)+')2Kg of Grapes')     
                    print('That would be Rs.200 as given')
                    amount=int(input("Pay: "))
                    if amount<200:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))
                      if repayamount<200:
                        print("Insufficient funds!")
                        print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>200:
                        new_amount=repayamount-200
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 3-4 hours.')  
                      else:
                        print("Thank you! You may expect your delivery within 3-4 hours.")         
                    elif amount>200:
                      new_amount=amount-200
                      print( "Thank you. Your change is Rs."+str(new_amount))
                      print('You may expect your delivery within 3-4 hours.')
                    else:
                      print("Thank you! You may expect your delivery within 3-4 hours.")
                 if(weightGrapes==5):
                    print('you have bought '+str(weightGrapes)+')2.500Kg of Grapes')     
                    print('That would be Rs.250 as given')
                    amount=int(input("Pay: "))
                    if amount<250:
                       print("Insufficient funds!")
                       repayamount=int(input("Please pay again: "))
                       if repayamount<250:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                       elif repayamount>250:
                         new_amount=repayamount-250
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within 4-5 hours.')
                       else:
                         print("Thank you! You may expect your delivery within 4-5 hours.")          
                    elif amount>250:
                        new_amount=amount-250
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within 4-5 hours.')
                    else:
                        print("Thank you! You may expect your delivery within 4-5 hours.")
                 if(weightGrapes>5):
                   print('Oops! You can only buy upto 2.500kg of grapes')
                   print('Sorry! Visit again Later...') 
            if(answer>5):
               print('Oops! we dont have any other fruits')
               print('Sorry! visit again Later...')
         elif(activity==3):
             print('Some of the stationary things are in stock')
             print('1)Pen and Pencils 2)Acrylic Paint and Brushes 3)Crayons and brushPens 4)Notepad and paperclip 5)Gum and cellotape')
             answer=int(input("Please enter the number (example 1 ,here 1 refers to Pen and Pencils): "))
             if(answer==1):
                print('You have purchased'+str(answer)+')Pen and Pencils')
                print('The pen and pencils are available in the following brands')
                print('Type 1 for Doms Pen and pencils. They are available in Rs.10')
                print('Type 2 for Classmate Pen and pencils. They are available in Rs.15')
                print('Type 3 for Camlin Pen and Pencils. They are available in Rs.20 ')   
                print('Type 4 for Faber-Castell Pen and Pencils. They are available in Rs.20')
                print('Type 5 for Apsara Max Pen and Pencils. They are available in Rs.25') 
                brand = int(input('Enter the brand number (example 1 - Here 1 refers to Doms brand): '))
                if (brand==1):
                   print('You have purchased '+str(brand)+')Doms Pen and Pencils')
                   print('That would be Rs.10 as given')
                   amount= int(input('Pay: '))
                   if amount<10:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))  
                      if repayamount<10:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>10:
                        new_amount=repayamount-10
                        print( "Thank you. Your change is Rs."+str(new_amount))
                        print('You may expect your delivery within an hour.')
                      else:
                        print('Thank you! You may expect your delivery within an hour')
                   elif amount>10:
                     new_amount=amount-10
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print('You may expect your delivery within an hour.')
                   else:
                      print('Thank you! You may expect your delivery within an hour')
                if (brand==2):
                    print('You have purchased '+str(brand)+')Classmate Pen and Pencils')
                    print('That would be Rs.15 as given')
                    amount = int(input('Pay: '))
                    if amount<15:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<15 :
                          print('Insufficient funds!')
                          print('You are not having suffiecient funds...Visit again Later...')
                       elif repayamount>15:
                          new_amount = repayamount-15
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 1-2 hours')
                       else:
                          print('Thank you! you may expect your delivery within 1-2 hours') 
                    elif amount>15:
                       new_amount = amount-15
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 1-2 hours')
                    else:
                       print('Thank you! you may expect your delivery within 1-2 hours')
                if(brand==3):
                    print('You have purchased'+str(brand)+')Camlin Pen and Pencils')
                    print('That would be Rs.20 as given')
                    amount = int(input('Pay: '))
                    if amount<20:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<20:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>20:
                          new_amount = repayamount-20
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours') 
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours')
                    elif amount>20:
                       new_amount = amount-20
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==4):
                    print('You have purchased'+str(brand)+')Faber-Castell Pen and Pencils')
                    print('That would be Rs.20 as given')
                    amount = int(input('Pay: '))
                    if amount<20:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<20:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>20:
                          new_amount = repayamount-20
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours') 
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours')
                    elif amount>20:
                       new_amount = amount-20
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==5):
                   print('You have purchased'+str(brand)+')Apsara Max Pen and Pencils')
                   print('That would be Rs.25 as given')
                   amount = int(input('Pay: '))
                   if amount<25:
                      print("Insufficient funds!")
                      repayamount = int(input('please Pay again: '))
                      if repayamount<25:
                         print('Insufficient funds!')
                         print('You are not having sufficient funds... visit again Later...')
                      elif repayamount>25:
                         new_amount = repayamount-25
                         print('Thank you. Your change is Rs.'+str(new_amount))
                         print('You may expect your delivery within 3-4 hours') 
                      else:
                         print('Thank you! you may expect your delivery within 3-4 hours')
                   elif amount>25:
                      new_amount = amount-25
                      print('Thank you. Your change is Rs.'+str(new_amount))
                      print('You may expect your delivery within 3-4 hours') 
                   else:
                      print('Thank you! you may expect your delivery within 3-4 hours')
                if(brand>5):
                   print('Oops! we dont have any other brand things in our shop...')
                   print('Sorry! Visit again Later...')       
             if(answer==2):
                print('You have purchased'+str(answer)+')Acrylic paint and brushes')
                print('The  are available in the following brands')
                print('Type 1 for Doms Acrylic paint and brushes. They are available in Rs.20')
                print('Type 2 for Classmate Acrylic paint and brushes. They are available in Rs.30')
                print('Type 3 for Camlin Acrylic paint and brushes. They are available in Rs.40 ')   
                print('Type 4 for Faber-Castell Acrylic paint and brushes. They are available in Rs.50')
                print('Type 5 for Fevicryl Acrylic paint and brushes. They are available in Rs.60') 
                brand = int(input('Enter the brand number (example 1 - Here 1 refers to Doms brand): '))  
                if (brand==1):
                   print('You have purchased '+str(brand)+')Doms Acrylic paint and brushes')
                   print('That would be Rs.20 as given')
                   amount= int(input('Pay: '))
                   if amount<20:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))  
                      if repayamount<20:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>20:
                         new_amount=repayamount-20
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within an hour.')
                      else:
                         print('Thank you! You may expect your delivery within an hour')
                   elif amount>20:
                     new_amount=amount-20
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print('You may expect your delivery within an hour.')
                   else:
                      print('Thank you! You may expect your delivery within an hour')
                if (brand==2):
                    print('You have purchased'+str(brand)+')Classmate Acrylic paint and brushes')
                    print('That would be Rs.30 as given')
                    amount = int(input('Pay: '))
                    if amount<30:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<30:
                          print('Insufficient funds!')
                          print('You are not having suffiecient funds...Visit again Later...')
                       elif repayamount>30:
                          new_amount = repayamount-30
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 1-2 hours')
                       else:
                          print('Thank you! you may expect your delivery within 1-2 hours') 
                    elif amount>30:
                       new_amount = amount-30
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 1-2 hours')
                    else:
                       print('Thank you! you may expect your delivery within 1-2 hours')
                if(brand==3):
                    print('You have purchased'+str(brand)+')Camlin Acrylic paint and brushes')
                    print('That would be Rs.40 as given')
                    amount = int(input('Pay: '))
                    if amount<40:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<40:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>40:
                          new_amount = repayamount-40
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours')
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours')
                    elif amount>40:
                       new_amount = amount-40
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==4):
                    print('You have purchased'+str(brand)+')Faber-Castell Acrylic paint and brushes')
                    print('That would be Rs.50 as given')
                    amount = int(input('Pay: '))
                    if amount<50:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<50:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>50:
                          new_amount = repayamount-50
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours')
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours') 
                    elif amount>50:
                       new_amount = amount-50
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==5):
                   print('You have purchased'+str(brand)+')Fevicryl Acrylic paint and brushes')
                   print('That would be Rs.60 as given')
                   amount = int(input('Pay: '))
                   if amount<60:
                      print("Insufficient funds!")
                      repayamount = int(input('please Pay again: '))
                      if repayamount<60:
                         print('Insufficient funds!')
                         print('You are not having sufficient funds... visit again Later...')
                      elif repayamount>60:
                         new_amount = repayamount-60
                         print('Thank you. Your change is Rs.'+str(new_amount))
                         print('You may expect your delivery within 3-4 hours')
                      else:
                         print('Thank you! you may expect your delivery within 3-4 hours')    
                   elif amount>60:
                      new_amount = amount-60
                      print('Thank you. Your change is Rs.'+str(new_amount))
                      print('You may expect your delivery within 3-4 hours') 
                   else:
                      print('Thank you! you may expect your delivery within 3-4 hours') 
                if(brand>5):
                   print('Oops! we dont have any other brand things in our shop...')
                   print('Sorry! Visit again Later...')            
             if(answer==3):
                print('You have purchased'+str(answer)+')Crayons and brushpens')
                print('The Crayons and brushpens are available in the following brands')
                print('Type 1 for Doms Crayons and brushpens. They are available in Rs.25')
                print('Type 2 for Classmate Crayons and brushpens. They are available in Rs.30')
                print('Type 3 for Camlin Crayons and brushpens. They are available in Rs.40 ')   
                print('Type 4 for Faber-Castell Crayons and brushpens. They are available in Rs.50')
                print('Type 5 for Kokuyo Crayons and brushpens. They are available in Rs.60') 
                brand = int(input('Enter the brand number (example 1 - Here 1 refers to Doms brand): '))  
                if (brand==1):
                   print('You have purchased '+str(brand)+')Doms Acrylic Crayons and brushpens')
                   print('That would be Rs.25 as given')
                   amount= int(input('Pay: '))
                   if amount<25:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))  
                      if repayamount<25:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>25:
                         new_amount=repayamount-25
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within an hour.')
                      else:
                         print('Thank you! You may expect your delivery within an hour')
                   elif amount>25:
                     new_amount=amount-25
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print('You may expect your delivery within an hour.')
                   else:
                      print('Thank you! You may expect your delivery within an hour')
                if (brand==2):
                    print('You have purchased'+str(brand)+')Classmate Crayons and brushpens')
                    print('That would be Rs.30 as given')
                    amount = int(input('Pay: '))
                    if amount<30:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<30:
                          print('Insufficient funds!')
                          print('You are not having suffiecient funds...Visit again Later...')
                       elif repayamount>30:
                          new_amount = repayamount-30
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 1-2 hours')
                       else:
                          print('Thank you! you may expect your delivery within 1-2 hours')
                    elif amount>30:
                       new_amount = amount-30
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 1-2 hours')
                    else:
                       print('Thank you! you may expect your delivery within 1-2 hours')
                if(brand==3):
                    print('You have purchased'+str(brand)+')Camlin Crayons and brushpens')
                    print('That would be Rs.40 as given')
                    amount = int(input('Pay: '))
                    if amount<40:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<40:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>40:
                          new_amount = repayamount-40
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours') 
                       else:
                         print('Thank you! you may expect your delivery within 2-3 hours')
                    elif amount>40:
                       new_amount = amount-40
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==4):
                    print('You have purchased'+str(brand)+')Faber-Castell Crayons and brushpens')
                    print('That would be Rs.50 as given')
                    amount = int(input('Pay: '))
                    if amount<50 :
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<50:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>50:
                          new_amount = repayamount-50
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours')
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours') 
                    elif amount>50:
                       new_amount = amount-50
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==5):
                   print('You have purchased'+str(brand)+')kokuyo Crayons and brushpens')
                   print('That would be Rs.60 as given')
                   amount = int(input('Pay: '))
                   if amount<60:
                      print("Insufficient funds!")
                      repayamount = int(input('please Pay again: '))
                      if repayamount<60:
                         print('Insufficient funds!')
                         print('You are not having sufficient funds... visit again Later...')
                      elif repayamount>60:
                         new_amount = repayamount-60
                         print('Thank you. Your change is Rs.'+str(new_amount))
                         print('You may expect your delivery within 3-4 hours')
                      else:
                         print('Thank you! you may expect your delivery within 3-4 hours') 
                   elif amount>60:
                      new_amount = amount-60
                      print('Thank you. Your change is Rs.'+str(new_amount))
                      print('You may expect your delivery within 3-4 hours') 
                   else:
                      print('Thank you! you may expect your delivery within 3-4 hours')     
                if(brand>5):
                   print('Oops! we dont have any other brand things in our shop...')
                   print('Sorry! Visit again Later...')         
             if(answer==4):
                print('You have purchased'+str(answer)+')Notepads and paperclips')
                print('The Notepads and paperclips are available in the following brands')
                print('Type 1 for Doms Notepads and paperclips. They are available in Rs.10')
                print('Type 2 for Classmate Notepads and paperclips. They are available in Rs.20')
                print('Type 3 for Camlin Notepads and paperclips. They are available in Rs.30 ')   
                print('Type 4 for Faber-Castell Notepads and paperclips. They are available in Rs.40')
                print('Type 5 for Kokuyo Notepads and paperclips. They are available in Rs.50') 
                brand = int(input('Enter the brand number (example 1 - Here 1 refers to Doms brand): '))  
                if (brand==1):
                   print('You have purchased '+str(brand)+')Doms Notepads and paperclips')
                   print('That would be Rs.10 as given')
                   amount= int(input('Pay: '))
                   if amount<10:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))  
                      if repayamount<10:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>10:
                         new_amount=repayamount-10
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within an hour.')
                      else:
                         print('Thank you! You may expect your delivery within an hour') 
                   elif amount>10:
                     new_amount=amount-10
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print('You may expect your delivery within an hour.')
                   else:
                      print('Thank you! You may expect your delivery within an hour')
                if (brand==2):
                    print('You have purchased'+str(brand)+')Classmate Notepads and paperclips')
                    print('That would be Rs.20 as given')
                    amount = int(input('Pay: '))
                    if amount<20:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<20:
                          print('Insufficient funds!')
                          print('You are not having suffiecient funds...Visit again Later...')
                       elif repayamount>20:
                          new_amount = repayamount-20
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 1-2 hours')
                       else:
                          print('Thank you! you may expect your delivery within 1-2 hours')
                    elif amount>20:
                       new_amount = amount-20
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 1-2 hours')
                    else:
                       print('Thank you! you may expect your delivery within 1-2 hours')
                if(brand==3):
                    print('You have purchased'+str(brand)+')Camlin Notepads and paperclips')
                    print('That would be Rs.30 as given')
                    amount = int(input('Pay: '))
                    if amount<30:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<30:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>30:
                          new_amount = repayamount-30
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours')
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours') 
                    elif amount>30:
                       new_amount = amount-30
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==4):
                    print('You have purchased'+str(brand)+')Faber-Castell Notepads and paperclips')
                    print('That would be Rs.50 as given')
                    amount = int(input('Pay: '))
                    if amount<40:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<40:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>40:
                          new_amount = repayamount-40
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours') 
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours')
                    elif amount>40:
                       new_amount = amount-40
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==5):
                   print('You have purchased '+str(brand)+' )kokuyo Notepads and paperclips')
                   print('That would be Rs.50 as given')
                   amount = int(input('Pay: '))
                   if amount<50:
                      print("Insufficient funds!")
                      repayamount = int(input('please Pay again: '))
                      if repayamount<50:
                         print('Insufficient funds!')
                         print('You are not having sufficient funds... visit again Later...')
                      elif repayamount>50:
                         new_amount = repayamount-50
                         print('Thank you. Your change is Rs.'+str(new_amount))
                         print('You may expect your delivery within 3-4 hours') 
                      else:
                         print('Thank you! you may expect your delivery within 3-4 hours')
                   elif amount>50:
                      new_amount = amount-50
                      print('Thank you. Your change is Rs.'+str(new_amount))
                      print('You may expect your delivery within 3-4 hours') 
                   else:
                      print('Thank you! you may expect your delivery within 3-4 hours')
                if brand>5:
                   print('Oops! we dont have any other brand things in our shop...')
                   print('Sorry! Visit again Later...')       
             if(answer==5):
                print('You have purchased'+str(answer)+')Gum and cellotape')
                print('The Gum and cellotape are available in the following brands')
                print('Type 1 for Doms Gum and cellotape. They are available in Rs.10')
                print('Type 2 for Classmate Gum and cellotape. They are available in Rs.20')
                print('Type 3 for Camlin Gum and cellotape. They are available in Rs.30 ')   
                print('Type 4 for Faber-CastellGum and cellotape. They are available in Rs.40')
                print('Type 5 for Kokuyo Gum and cellotape. They are available in Rs.50') 
                brand = int(input('Enter the brand number (example 1 - Here 1 refers to Doms brand): '))  
                if (brand==1):
                   print('You have purchased '+str(brand)+')Doms Gum and cellotape')
                   print('That would be Rs.10 as given')
                   amount= int(input('Pay: '))
                   if amount<10:
                      print("Insufficient funds!")
                      repayamount=int(input("Please pay again: "))  
                      if repayamount<10:
                         print("Insufficient funds!")
                         print('You are not having sufficient funds...Visit again Later...')
                      elif repayamount>10:
                         new_amount=repayamount-10
                         print( "Thank you. Your change is Rs."+str(new_amount))
                         print('You may expect your delivery within an hour.')
                      else:
                         print('Thank you! You may expect your delivery within an hour')
                   elif amount>10:
                     new_amount=amount-10
                     print( "Thank you. Your change is Rs."+str(new_amount))
                     print('You may expect your delivery within an hour.')
                   else:
                      print('Thank you! You may expect your delivery within an hour')
                if (brand==2):
                    print('You have purchased'+str(brand)+')ClassmateGum and cellotape')
                    print('That would be Rs.20 as given')
                    amount = int(input('Pay: '))
                    if amount<20:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<20:
                          print('Insufficient funds!')
                          print('You are not having suffiecient funds...Visit again Later...')
                       elif repayamount>20:
                          new_amount = repayamount-20
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 1-2 hours')
                       else:
                          print('Thank you! you may expect your delivery within 1-2 hours')
                    elif amount>20:
                       new_amount = amount-20
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 1-2 hours')
                    else:
                       print('Thank you! you may expect your delivery within 1-2 hours')
                if(brand==3):
                    print('You have purchased'+str(brand)+')Camlin Gum and cellotape')
                    print('That would be Rs.30 as given')
                    amount = int(input('Pay: '))
                    if amount<30:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<30:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>30:
                          new_amount = repayamount-30
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours')
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours') 
                    elif amount>30:
                       new_amount = amount-30
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==4):
                    print('You have purchased'+str(brand)+')Faber-Castell Gum and cellotape')
                    print('That would be Rs.50 as given')
                    amount = int(input('Pay: '))
                    if amount<40:
                       print('Insufficient funds!')
                       repayamount = int(input('Please pay again: '))
                       if repayamount<40:
                          print('Insufficient funds')
                          print('You are not having sufficient funds... visit again Later...')
                       elif repayamount>40:
                          new_amount = repayamount-40
                          print('Thank you. Your change is Rs.'+str(new_amount))
                          print('You may expect your delivery within 2-3 hours')
                       else:
                          print('Thank you! you may expect your delivery within 2-3 hours')
                    elif amount>40:
                       new_amount = amount-40
                       print('Thank you. Your change is Rs.'+str(new_amount))
                       print('You may expect your delivery within 2-3 hours') 
                    else:
                       print('Thank you! you may expect your delivery within 2-3 hours')
                if(brand==5):
                   print('You have purchased '+str(brand)+')kokuyo Gum and cellotape')
                   print('That would be Rs.50 as given')
                   amount = int(input('Pay: '))
                   if amount<50:
                      print("Insufficient funds!")
                      repayamount = int(input('please Pay again: '))
                      if repayamount<50:
                         print('Insufficient funds!')
                         print('You are not having sufficient funds... visit again Later...')
                      elif repayamount>50:
                         new_amount = repayamount-50
                         print('Thank you. Your change is Rs.'+str(new_amount))
                         print('You may expect your delivery within 3-4 hours') 
                      else:
                         print('Thank you! you may expect your delivery within 3-4 hours')
                   elif amount>50:
                      new_amount = amount-50
                      print('Thank you. Your change is Rs.'+str(new_amount))
                      print('You may expect your delivery within 3-4 hours') 
                   else:
                      print('Thank you! you may expect your delivery within 3-4 hours')
                if(brand>5):
                   print('Oops! we dont have any other brand things in our shop...')
                   print('Sorry! Visit again Later...') 
             if(answer>5):
                print('Oops! we dont have any other stationary things in our shop...')
                print('Sorry! Visit again Later...')           
         elif(activity>3):
             print('Oops! we dont have any other things in our shop...')
             print('Sorry! Visit again Later...')
    
def main():
    name=input("Enter name: ")
    card_number=input("Insert card number: ")
    print("Welcome "+name+"!")
    new_user=grocery(card_number, name)

    if card_number.strip().isdigit():
        new_user.integers()
        
    else:
        print("Please only enter numbers! If you enter a letter again, the app will lock you for 5 minutes.")
        card_number=input("Insert card number: ")
        if card_number.strip().isdigit():
            new_user.integers()

    
if __name__=="__main__":
    main()