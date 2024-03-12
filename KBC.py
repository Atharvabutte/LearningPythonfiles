Questions = [
    
            [f"The first captain of Indian Cricket team in Test matches was?","C K Nayudu","Madan Lal","Kapil Dev","Mohinder Amarnath",1],
            
            [f"In 2009, who was the captain of the Deccan Chargers?","Arjun Yadav","Adam Gilchrist","Dwarka Teja","VS Laxman",2],
            
            [f"ICC World Cup 2012 Cricket Tournament started on?","March 24, 2012","April 13, 2012","December 14, 2012","September 18, 2012",4],
            
            [f"In 1983 World Cup Final, which player won the Man of the Match award?","C K Nayudu","Mohinder Amarnath","Madan Lal","Kapil Dev",2],
            
            [f"_________ won the first Cricket World Cup in 1975?","Pakistan","Sri Lanka","Australia","West Indies",4],
           
            [f"How many teams took part in the first Cricket World Cup?","5","8","4","12",2],
           
            [f"Who was the Man of the Match in the 2007 Cricket World Cup Final?","Jason Gillespie","Adam Gilchrist","Mark Waugh","Ian Healy",2],
           
            [f"India played its First 1 - day international match in?","Headingley","Lords","Oval","Green park",1],
           
            [f"The first ODI captain for India was?","C K Nayadu","Vinoo Mankad","Ajit Wadekar","Lala Amarnath",3],
           
            [f"The first ODI match was played in India in?","Ahmedabad","Lucknow","Kanpur","Kolkata",1],
           
            [f"Which country won the final series of the triangular Cricket series that took place in Durban in February 1997?","Australia","South Africa","India","Pakistan",2],
           
            [f"India became victorious in the World Cricket Championship beating Pakistan in the final by Eight wickets. Who won the man of the tournament title?","Sachin Tendulka","Ravi Shastr","Saurav Ganguly","Ajay Jadeja",2],
           
            [f"Who is RunnerUp in 2023 Cricket World cup?","Australia","India","South Africa","England",2],
           
            [f"Who scored 200 in 2023 Cricket World cup against Afganisthan?","Rohit Sharma","Shubhaman Gill","Glenn Maxwell","Travis Head",3],
            
            [f"Which is a favourite shot of Kumar Sangakara?","Pull Shot","Straight Drive","Cover Drive","Flick",3],
         ]


Levels =[1000,2000,3000,5000,10000,15000,25000,50000,100000,175000,200000,320000,480000,600000,7200000]
Money = 0 

for i in range(0,len(Questions)):
    Question = Questions[i]
    print(f"\n\nQuestion for Rs. {Levels[i]}")
    print(Question[0])
    print(f"1.{Question[1]}              2.{Question[2]}")
    print(f"3.{Question[3]}              4.{Question[4]}")
    Responce = int(input("Enter your answer(1-4 or 0 to quit):"))
    if(Responce == 0):
        money = Levels[i-1]
        break
    if(Responce == Question[-1]):
        print(f"Correct answer.😁 you won Rs. {Levels[i]}")
        if(i == 4):
            Money = 10000
        elif(i == 8):
            Money = 100000
        elif(i == 14):
            Money = 7200000
    else:
        print("Wrong Answer!")
        break

print(f"You won as a price Rs. {Money}")