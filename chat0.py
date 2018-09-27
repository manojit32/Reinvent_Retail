from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import item_finder
import os
import subprocess
import recomm
def chatbot(user):
    # Create a new instance of a ChatBot
    bot = ChatBot("NOSTAW",silence_performance_warning=True,
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../SecondaryDataBase.json"
    )
    
    
    bot.set_trainer(ChatterBotCorpusTrainer)
    
    # Train the chat bot with the entire english corpus
    bot.train("C:/Users/1399869/Downloads/money.corpus.json",
              "C:/Users/1399869/Downloads/conversations.corpus.json",
              "C:/Users/1399869/Downloads/ai.corpus.json",
              "C:/Users/1399869/Downloads/botprofile.corpus.json",
              "C:/Users/1399869/Downloads/computers.corpus.json")
    
    print("Type thoughts to bot.\n")
    
    # The following loop will execute each time the user enters input
    while True:
        try:
            # We pass None to this method because the parameter
            # is not used by the TerminalAdapter
        
            bot_input = bot.get_response(None)
            if "finder" in bot_input:
                exec(bot_input)
            elif "trending" in bot_input:
                recomm.trending()
            elif "recommendations" in bot_input:
                recomm.user_based(user)
            print("\n")    
    
        # Press ctrl-c or ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break