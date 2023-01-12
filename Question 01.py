#Input (Enter a number and store it in a variable)
number=int(input("Enter a number   "))

#Define W and C
print("(If you want the number in word please input W/w and if you want the number in currency please input C/c) ")

#Ask a question from the user if he want the number in USD dollars or in word
opt=str(input("Please enter your Option (W/C)   "))
if (opt=="C" or opt=="c"):
    
#The given number in USD dollars
    x=format(number/200,".2f")
    print("USD",round(float(x)))

elif(opt=="W" or opt=="w"):

#process
#Take a one digit from the right hand side as our easy
    one_digit=number%10
    two_digit=number%100//10
    both_digit=abs(number)%100
    three_digit=number%1000//100
    four_digit=number%10000//1000
    four_digit1=number%10000//1000
    five_digit=number%100000//10000
    five_digit1=number%100000//10000
    four_five=number%100000//1000
    last_three=abs(number)%1000
    last_four=abs(number)%10000
    fourfive_digit=number%10000//1000

#count the length to allocate the places
    number_of_digits = len(str(number))


#Thousand numbers from 10 to 19
    if (four_five>=10 and four_five<20):
        if four_five==10:
            fifth_number=("Ten Thousand")
        if four_five==11:
            fifth_number=("Eleven Thousand")
        if four_five==12:
            fifth_number=("Twelve Thousand")    
        if four_five==13:
            fifth_number=("Thirteen Thousand")    
        if four_five==14:
            fifth_number=("Fourteen Thousand")
        if four_five==15:
            fifth_number=("Fifteen Thousand")
        if four_five==16:
            fifth_number=("Sixteen Thousand")
        if four_five==17:
            fifth_number=("Seventeen Thousand")
        if four_five==18:
            fifth_number=("Eighteen Thousand")
        if four_five==19:
            fifth_number=("Nineteen Thousand")
            
            
 #Thousand numbers from 20 to 90 with 10000's multiplication
    else:
        if (five_digit==2):
            fifth_number=("Twenty")
        if (five_digit==3):
            fifth_number=("Thirty")
        if (five_digit==4):
            fifth_number=("Fourty")
        if (five_digit==5):
            fifth_number=("Fifty")
        if (five_digit==6):
            fifth_number=("Sixty")
        if (five_digit==7):
            fifth_number=("Seventy")
        if (five_digit==8):
            fifth_number=("Eighty")
        if (five_digit==9):
            fifth_number=("Ninety")
            

#Thousand numbers from 20 to 90 with 10000's multiplication with "Thousand"
        if (five_digit1==2):
            fifth_number1=("Twenty Thousand")
        if (five_digit1==3):
            fifth_number1=("Thirty Thousand")
        if (five_digit1==4):
            fifth_number1=("Fourty Thousand")
        if (five_digit1==5):
            fifth_number1=("Fifty Thousand")
        if (five_digit1==6):
            fifth_number1=("Sixty Thousand")
        if (five_digit1==7):
            fifth_number1=("Seventy Thousand")
        if (five_digit1==8):
            fifth_number1=("Eighty Thousand")
        if (five_digit1==9):
            fifth_number1=("Ninety Thousand")
            
            
#Thousand numbers from 20 to 90 with 10000's multiplication without word "Thousand"
    if (fourfive_digit==2):
        fourfive_number=("Twenty")
    if (fourfive_digit==3):
        fourfive_number=("Thirty")
    if (fourfive_digit==4):
        fourfive_number=("Fourty")
    if (fourfive_digit==5):
        fourfive_number=("Fifty")
    if (fourfive_digit==6):
        fourfive_number=("Sixty")
    if (fourfive_digit==7):
        fourfive_number=("Seventy")
    if (fourfive_digit==8):
        fourfive_number=("Eighty")
    if (fourfive_digit==9):
        fourfive_number=("Ninety")

           
#Thousand numbers from 1 to 9 with "Thousand"
    if (four_digit==0):
        fouth_number=("")        
    if (four_digit==1):
        fouth_number=("One Thousand")
    if (four_digit==2):
        fouth_number=("Two Thousand")
    if (four_digit==3):
        fouth_number=("Three Thousand")
    if (four_digit==4):
        fouth_number=("Four Thousand")
    if (four_digit==5):
        fouth_number=("Five Thousand")
    if (four_digit==6):
        fouth_number=("Six Thousand")
    if (four_digit==7):
        fouth_number=("Seven Thousand")
    if (four_digit==8):
        fouth_number=("Eight Thousand")
    if (four_digit==9):
        fouth_number=("Nine Thousand")
        

    #Thousand numbers from 1 to 9 without "Thousand"
    if (four_digit1==0):
        fouth_number1=("")        
    if (four_digit1==1):
        fouth_number1=("One")
    if (four_digit1==2):
        fouth_number1=("Two")
    if (four_digit1==3):
        fouth_number1=("Three")
    if (four_digit1==4):
        fouth_number1=("Four")
    if (four_digit1==5):
        fouth_number1=("Five")
    if (four_digit1==6):
        fouth_number1=("Six")
    if (four_digit1==7):
        fouth_number1=("Seven")
    if (four_digit1==8):
        fouth_number1=("Eight")
    if (four_digit1==9):
        fouth_number1=("Nine")    


#Hundred numbers from 1 to 9
    if (three_digit==0):
        third_number=("" )
    if (three_digit==1):
        third_number=("One Hundred")
    if (three_digit==2):
        third_number=("Two Hundred")
    if (three_digit==3):
        third_number=("Three Hundred")
    if (three_digit==4):
        third_number=("Four Hundred")
    if (three_digit==5):
        third_number=("Five Hundred")
    if (three_digit==6):
        third_number=("Six Hundred")
    if (three_digit==7):
        third_number=("Seven Hundred")
    if (three_digit==8):
        third_number=("Eight Hundred")
    if (three_digit==9):
        third_number=("Nine Hundred")


#Numbers from 10 to 19    
    if(both_digit>=10 and both_digit<=20):
        if both_digit==10:
            two_digit=("Ten")
        if both_digit==11:
            two_digit=("Eleven")
        if both_digit==12:
            two_digit=("Twelve")   
        if both_digit==13:
            two_digit=("Thirteen")
        if both_digit==14:
            two_digit=("Fourteen")
        if both_digit==15:
            two_digit=("Fifteen")
        if both_digit==16:
            two_digit=("Sixteen")
        if both_digit==17:
            two_digit=("Seventeen")
        if both_digit==18:
            two_digit=("Eighteen")
        if both_digit==19:
            two_digit=("Nineteen")
        if both_digit==20:
            two_digit=("twenty")

        
#Numbers from 10 to 90 with 10's multiplication        
    else:
        if (two_digit==0):
            digit_two=("")
        if (two_digit==2):
            digit_two=("twenty ")
        if (two_digit==3):
            digit_two=("Thirty ")
        if (two_digit==4):
            digit_two=("Fourty")
        if (two_digit==5):
            digit_two=("Fifty")
        if (two_digit==6):
            digit_two=("Sixty")
        if (two_digit==7):
            digit_two=("Seventy")
        if (two_digit==8):
            digit_two=("Eighty")
        if (two_digit==9):
            digit_two=("Ninety")
            
         
#Numbers from 1 to 9 
    if (one_digit==0):
        first_number=("")
    if (one_digit==1):
        first_number=("One")
    if (one_digit==2):
        first_number=("Two")
    if (one_digit==3):
        first_number=("Three")
    if (one_digit==4):
        first_number=("Four")
    if (one_digit==5):
        first_number=("Five")
    if (one_digit==6):
        first_number=("Six")
    if (one_digit==7):
        first_number=("Seven")
    if (one_digit==8):
        first_number=("Eight")
    if (one_digit==9):
        first_number=("Nine")
        

#Output    
#print 1 digit number   
    if (number_of_digits==1):
        print(first_number)
        
#print 2 digit number     
    elif (number_of_digits==2):
        if(number>=10 and number<=20):
           print(two_digit)
        else:
           print(digit_two,first_number)
           
#print 3 digit number 
    if (number_of_digits==3):
       if(both_digit>=10 and both_digit<=20): 
           print(third_number,"and",two_digit) 
       else:
            if(two_digit==00):
               print(third_number,digit_two,first_number)
            else:
               print(third_number,"and",digit_two,first_number)
           
#print 4 digit number            
    if (number_of_digits==4):
        if(last_three==000):
           print(fouth_number)
        else:
            if(both_digit>=10 and both_digit<=20):
               print(fouth_number,third_number,"and",two_digit)
            else:
                if(both_digit!=0):
                   print(fouth_number,third_number,"and",digit_two,first_number)
                else:
                   print(fouth_number,"and",third_number,digit_two,first_number) 
                            
#print 5 digit number              
    elif (number_of_digits==5):
        if(last_four==0000):
           print(fifth_number1)
        else:
            if(last_three==000):
                print(fifth_number,fouth_number)
                
    if(number<19999 and number>10000):            
        if(both_digit>=10 and both_digit<=20):
            print(fifth_number,third_number,"and",two_digit)
        else:
            if(both_digit!=0):
                print(fifth_number,third_number,"and",digit_two,first_number)
            else:
                 print(fifth_number,third_number,digit_two,first_number)
                
    if(number>20000):
        if(both_digit<10):
            if(one_digit==0 and digit_two==0):
                print(fifth_number,fouth_number,"Thousand",third_number,digit_two,first_number)
            elif(both_digit>=10 and both_digit<=20):
               print(fifth_number,fouth_number,third_number,two_digit) 
        
        if(both_digit<=9 and two_digit!=0):
            print(fifth_number,fouth_number1,"Thousand",third_number,first_number)
        if(both_digit>=10 and both_digit<20):
             print(fifth_number,fouth_number1,"Thousand",third_number,"and",two_digit)
        else:
             print(fifth_number,fouth_number1,"Thousand",third_number,"and",digit_two,first_number)
             
#If the number is greater than 100000 it won't be give any output
if(number>=100000):
    print("Please enter a number less than 100000")             

  
