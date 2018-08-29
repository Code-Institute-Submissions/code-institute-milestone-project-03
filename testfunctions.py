import json

def checkusername(username, final_score):
    
    if username == "" or username in final_score:
        return False
    return True

def checkanswer(riddlea, riddle_answer):
    
    if riddle["answer"].lower() in answer.lower():
        return True
    else:
        return False

def nextriddle(riddles, attempt):
   
    if attempt == None:
        return riddles[0]
    else:
        if attempt >= (len(riddles) - 1):
            return None
        else:
            return riddles[attempt+1]
