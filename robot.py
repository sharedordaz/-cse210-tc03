#Are you boring? Talk with the team robot

import tkinter as tk
import random

notlike = ["fashion", "tiktok", "alcohol", "drugs", "reggaeton", "gossip"]
like = ["videogames", "programing", "computers", "music", "windows", "linux", "comics", "me", "byu"]
notknow = ["art","citizenship","geography","history","languages","literacy","people","science","math","books","writing","dance","dancing","sports", "football", "basketball", "golf", "volleyball", "ball", "movies", "usa", "capitalism", "communism", "mexico", "europe", "asia", "china", "russia", "israel", "africa", "ghana", "arabia", "india", "japan", "france", "germany", "italy", "england", "korea", "canada", "peru", "brazil", "colombia", "argentina", "america", "philippines", "money", "economy", "politician", "politics", "anime", "manga", "novel", "novels", "horror", "paint", "psicology", "medicine", "expressionism", "realism", "barroque", "rock", "pop", "latin", "people","enginering", "phisics", "chemistry", "geology", "religion", "mormons", "philosophy", "greece", "greeks", "atheism", "catholics", "christians"]
conversation_history = []
context = ["no_context"]

def main():
    # Create the Tk root object.
    root = tk.Tk()
    
    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root, bg="gray4", width="500px",height="300px")
    frm_main.master.title("Python Robot")
    frm_main.pack(padx=0, pady=0, fill=tk.BOTH, expand=1)

    # Call the window_items function, which will add
    # labels, text entry boxes, and buttons to the main window.
    window_items(frm_main)
    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()
    print(conversation_history)
def window_items(frm_main):
    """The items that are shown in my program"""
    lbl_title = tk.Label(frm_main, fg="snow", bg="gray4", text="Python Robot:\nType something and talk!")
    
    #The conversation
    conversation_frame = tk.Frame(frm_main, bg= "DarkOrange1", width="300px", height= "300px", relief="groove", borderwidth="1px")
    conversation= tk.Label (conversation_frame, fg="black", bg= "DarkOrange1")

    talking_entry = tk.Entry(frm_main, bg="snow", width=42, relief="groove", borderwidth="1px")
    talking_button = tk.Button(frm_main, width=5, bg= "gray83", relief="groove", borderwidth="1px", text= "Talk")
    
    #Grid
    conversation.pack(side=tk.TOP)
    lbl_title.grid(row=0, column=0, columnspan= 4, padx=100, pady=5)
    conversation_frame.grid(row=1, column=0, columnspan= 4, padx=20, pady=20, sticky="n")
    talking_entry.grid(row=2, column=0, columnspan=3, padx=0, pady=20 , sticky="e")
    talking_button.grid(row=2, column=3, padx=0, pady=10, sticky = "e")



    def talk():
        """Returns a conversation"""
        
        #Get the input that the user writted
        user_input = talking_entry.get()
        
        #Append the user input to the main conversation
        conversation_history.append(f"YOU: {user_input}")
        
        #Make the input readable to the machine
        user_input = user_input.lower()
        
        
        def get_response(user_input, context=context):
            """The brain of the robot"""

            #print(f"context={context}")
            response_context = context[0]
            print(response_context)


            greetings = ["hello", "hi", "howdy", "whats up", "hello!", "hi!", "howdy!", "whats up!"]
            farewells = ["goodbye", "bye", "goodbye!", "bye!"]
            
            #Questions
            close_question = ["am i", "i am", "are you", "is he","is her", "are they", "are we", "is it", "was me", "was you", "was he", "was her", "were they", "were we", "were us", "was it"]
            open_question = ["who", "what", "where", "when", "why"]
            #Reactions
            neutral_reactions = ["Really interesting!", f"I see you know a lot about {response_context} ", "And how do you know that?", "I agree with you", f"Now i have a different perspective about {response_context}", "Thats new for me"]
            like_reactions = [f"Keep talking about {response_context} please", "I think we can have fun together", "You are funny", f"I thought {response_context} was different", f"You really like {response_context} isn't it?", "Interesting..."]
            notlike_reactions = [f"Sorry but i don't know a lot about {response_context}", f"Why do you like {response_context}?", "What is the hour?", f"Is that important in {response_context} things?", "A lot of people like to talk about that?"]
            likeornot = [like, notlike]
            yesorno = ["Yes", "No"]
            #remove ! symbol
            user_input = user_input.replace('!', '')
            #remove ? symbol    
            user_input = user_input.replace("?", " ?") 
            print(user_input)
            
            complete_user_input = user_input
            
            #Common questions that the computer can response
            def common_phrases(complete_user_input):
                """Return a response for start a conversation depending on the situation"""
                #Generic response database
                intro = ["really?", "say something about you", "help", "who are you", "who are you ?", "tell me about you", "how are you ?","how are you", "what is your name ?", "what's your name ?", "whats your name ?", "what is your name", "you have a name ?", "whats your name","tell me your name", "what's your name", "how i can call you ?", "tell me how i can call you", "how i can call you", "what is your function ?", "what is your purpose ?"]
                start_conv = ["what do you want to talk about ?", "do you want to talk about something ?", "talk", "tell me something", "what do you want to talk about", "start to talk", "start a conversation", "do you like something ?", "what do you like ?"]
                agreements = ["cool","ok","good", "okay", "yes", "no", "sure","great", "agree", "is ok"]

                if complete_user_input.lower() in intro:
                    response = "Im a Python Robot, I can talk with you about many topics"
                    return response
                if complete_user_input == "":
                    response = "Please say something"
                    return response
                if complete_user_input.lower() in agreements:
                    if context == ["no_context"]:
                        response = "So, what you want to talk about?"
                        return response
                    else:
                        response = (f"So, what other thing about {context[0]} do you want to tell me?")
                        return response
                if complete_user_input.lower() in start_conv:
                        choosed_conv = random.choice(like)
                        response = (f"I would like to talk about {choosed_conv}")
                        context.clear()
                        context.append(choosed_conv)
                        return response
            
            

            def questions(complete_user_input):  
                """Return yes or no to close questions"""
            
                for questions in close_question:
                    if questions in complete_user_input:
                        response = random.choice(yesorno)
                        return response

            #Storage a question response
            question_response = questions(complete_user_input)

            #What to do when there is no context of the conversation
            #Remove the blankspaces and a loop to read the user input and get a context
            def no_context_response(user_input,question_response, like, notlike, notknow):
                """Give a response when the computer doesn't have the context of the conversation"""
                #give list format    
                user_input = user_input.split(" ")

                for word in user_input:
                    if word.lower() in greetings:
                        response = (f"Hello! My name is Python Robot")
                        return response
                    elif word.lower() in farewells:
                        response = (f"Goodbye! Have a nice day!")
                        return response
                    elif word.lower() in notlike:
                        response = (f"I don't like to talk about {word}")
                        context.clear()
                        context.append(word)
                        return response
                    elif word.lower() in like:
                        response = (f"Oh! Im a big fan of {word}")
                        context.clear()
                        context.append(word)
                        return response
                    elif word.lower() in notknow:
                        response = (f"I don't know anything about {word}, but keep talking about it")
                        context.clear()
                        context.append(word)
                        return response
                    elif "?" == word:
                        response = question_response
                        return response
     
            def context_response(complete_user_input,question_response, like, notlike, notknow, response_context):
                """Give the response when the computer have a context"""
                if "?" in complete_user_input:
                    if question_response != None:
                        return question_response
                    else:
                        response = (f"I don't have a lot of knowledge about that sorry")
                        return response
                else:
                    if response_context in like:
                        response = random.choice(like_reactions)
                        #Reset the context
                        context.clear()
                        context.append("no_context")
                        return response
                    elif response_context in notlike:
                        response = random.choice(notlike_reactions)
                        #Reset the context
                        context.clear()
                        context.append("no_context")
                        return response
                    elif response_context in notknow: 
                        choice = random.choice(likeornot)
                        choice.append(response_context)
                        notknow.remove(response_context)
                        response = random.choice(neutral_reactions)
                        #Reset the context
                        context.clear()
                        context.append("no_context")
                        return response
                    else:
                        response = (f"I don't have a lot of knowledge about that sorry")
                        return response
            
            #Run common_phrases by priority
            if common_phrases(complete_user_input) != None:
                return common_phrases(complete_user_input)
            #After that run the "no_context_response function"
            if context == ["no_context"]:
                return no_context_response(user_input,question_response, like, notlike, notknow)
                
            #At the end, talk with a context of conversation
            elif context != ["no_context"]:
                return context_response(complete_user_input,question_response, like, notlike, notknow, response_context)
            


        def clear():
            """Clears the talking entry in the text box"""
            talking_entry.delete(0, tk.END)
            
            talking_entry.focus()


            # Give the keyboard focus to the age entry box.
            talking_entry.focus()

        #Display the answer of the machine
        response = get_response(user_input)
        if response == None:
            conversation_history.append(f"PYTHON ROBOT: I don't know what are you talking about...")
        else:
            conversation_history.append(f"PYTHON ROBOT: {response}")

        #Display the text on the box of tkinker
        
        display = "\n\n".join(conversation_history)
        conversation.config(text=(f"{display}"))
        clear()
        
    
    talking_button.config(command=talk)


main()
