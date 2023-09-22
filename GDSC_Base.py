# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:35:15 2023

@author: sherl
"""

"""
Created on Wed Sep 20 15:06:05 2023
 
@author: sherl
"""
 
 
 
import random
 
 
class Questions():
    
    def __init__(self,question_data):
        self.question_data=question_data
        
    
    def shuffle(self):
        random.shuffle(self.question_data)
        
        
 
 
class Gameplay():
    
    def __init__(self,question_data):
        self.question_data=question_data
        self.answer=""
        
    def display_question(self):
        dictionary=self.question_data.pop()
        question=dictionary["text"]
        self.answer=dictionary["answer"]
        return question
        
    def check_answer(self,answer):
        if self.answer==answer:
            print("Yep, that's correct!")
            return True
        else:
            print("Nope, that's incorrect!")
            return False
        
    def questions_left(self):
        if len(self.question_data)==0:
            return False
        else:
            return True
        
class Player():
    
    def __init__(self,name):
        self.name=name
        self.score=0
        
    def score_change(self,correct):
        if correct:
            self.score+=2
        else:
            self.score-=1
            
            
            
 
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

print("WELCOME TO THE QUIZ\nThe marking scheme is as follows: +2 for each correct answer and -1 for each wrong answer")



name=input("Enter your name to begin the quiz: ")
 
player=Player(name)
      
question_bank=Questions(question_data)
 
question_bank.shuffle()
 
game=Gameplay(question_bank.question_data)
 
  
left=True 
while left:
    
    print("Question: ",end=" ")
    
    x=game.display_question()
    
    print(x)
    
    ans=""
    valid=False
    while not valid:
        temp_ans=input("Enter t/T for True or f/F for False: ")
        if temp_ans in "tTfF":
            valid=True
        else:
            print("Invalid answer!")
            continue
    
    if temp_ans in "tT":
        ans="True"
        
    else:
        ans="False"
        
        
    correct=game.check_answer(ans)

    player.score_change(correct)
    left=game.questions_left()
    
print(f"Your final score is: {player.score}")