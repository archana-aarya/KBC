question_list=["who is the disco of this campus?", "who is the F.M of this campus?", "Which course is taught in navgurukul?"]
option_list=[["1.archana", "2.aaru", "3.rohini", "4.kajal"],["1.lucky", "2.Bharti", "3.Chandni", "4.archana aarya"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
answer_list=[3,4,1]
fifty_list=[['1.archana','3.rohini'],['2.bharti','4.archana aarya'],['1.Software Engineering','2.Counseling']]
solution_list=[3,4,1]
lifelinecount = 0
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0): 
        while j<len(fifty_list[index]):
            print(j+1,fifty_list[index][j])
            j=j+1
        user_ans = int(input('.....'))
        lifelinecount+=1
        if user_ans==solution_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return "no"
        
def option(index):
    j=0
    while j<len(option_list[index]):
        print(j+1,option_list[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==answer_list[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False

def que():
    index=0
    while index<len(question_list):
        print("Q.",index+1,question_list[index],"?")
        result=option(index)
        if result=="no":
            index-=1
        elif result==True:
            print("CONGRAGULATION YOU WIN 100000")
        else:
            print("YOU LOSS YOUR GAME")
            break   
        index+=1

def main():
    que()
main()