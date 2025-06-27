from ollama import Client
import sys
import random
import threading
import time

# Global control variable
_printing = False
_print_thread = None

def _print_hashes():
    while _printing:
        colorPrint("random", '#', end='', flush=True)
        time.sleep(0.3)
    print()  
    
def startPrinting():
    global _printing, _print_thread
    _printing = True
    _print_thread = threading.Thread(target=_print_hashes)
    _print_thread.start()

def stopPrinting():
    global _printing, _print_thread
    _printing = False
    if _print_thread:
        _print_thread.join()


client = Client(
  host='http://localhost:11434',
)

colors = ["red", "blue", "purple", "green", "yellow", "gray"]

def colorPrint(color, text, end='\n', flush=False): 
    if color == "random":
        color = random.choice(colors)
   
    if color == colors[0]: 
        print(f"\033[91m{text}\033[00m",end=end, flush=flush) 

    elif color == colors[1]:
        print(f"\033[96m{text}\033[00m",end=end, flush=flush)

    elif color == colors[2]: 
        
        print(f"\033[94m{text}\033[00m",end=end, flush=flush)

    elif color == colors[3]: 
        
        print(f"\033[92m {text}\033[00m",end=end, flush=flush)


    elif color == colors[4]: 
        
        print(f"\033[93m {text}\033[00m",end=end, flush=flush)

    elif color == colors[5]: 
        
        print(f"\033[97m {text}\033[00m",end=end, flush=flush)

    else: 
        print(text)

def guide(question):
    content = f"pretend you are groot and answer the followig question: {question}"
    startPrinting()
    response = client.chat(model="llama3.2:1b", messages=[
        {
            'role': 'user',
            'content': content,
        },
    ])
    stopPrinting()

    colorPrint("purple", "---------------------------------")
    colorPrint("random", response.message.content)


if len(sys.argv) == 3:
    model = sys.argv[1]
    question = sys.argv[2]
    color = "random"
    response = client.chat(model=model, messages=[
        {
            'role': 'user',
            'content': question,
        },
    ])

    colorPrint(color, response.message.content)
    
elif len(sys.argv) == 4:
    model = sys.argv[1]
    color = sys.argv[2]
    question = sys.argv[3]
    response = client.chat(model=model, messages=[
        {
            'role': 'user',
            'content': question,
        },
    ])


    colorPrint(color, response.message.content)

elif len(sys.argv) == 2:
    question = sys.argv[1]
    guide(question)







