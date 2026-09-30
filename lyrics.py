import time
import sys
import os


timed_lyrics = [
    ("Ibabalik kita nang buong-buo", 0.1),
    ("Pangako 'yun sa'yo", 0.2),         
    ("SA'YO LANG ANG PUSO KO", 0.3),     
    ("Kahit kainin mo", 0.7)             
]

def typewriter_display_with_timing(lines_with_time, char_speed=0.04):
    
    for line, total_duration in lines_with_time:
        
        start_time = time.time()
        
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(char_speed)
        
        print() 
        
        end_time = time.time()
        typing_time = end_time - start_time
        
        remaining_pause = total_duration - typing_time
        if remaining_pause > 0:
            time.sleep(remaining_pause)
            
typewriter_display_with_timing(timed_lyrics, char_speed=0.05)