import os
import time

face = """
        v    V                       v      v
        v    v                       v      v
        v    v                       v      v
        v    v                       v      v
        v    v     !TAKEDOWN!        v      v
        v    v                       v      v   
        v    v                       v      v
        v    v                       v      v
        v    v                       v      v
        v    v                       v      v
        v    v                       v      v
        v    v                       v      v
        v    v                       v      v
        v    v                       v      v
"""

for i in range(0, 256, 10): 
    os.system('clear')  
    print(f"\033[38;5;{i}m{face}\033[0m")  
    time.sleep(0.1)  

for i in range(255, -1, -10):  
    os.system('clear')
    print(f"\033[38;5;{i}m{face}\033[0m")
    time.sleep(0.1)