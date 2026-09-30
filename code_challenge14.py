#Anime list 
anime_list = []
p1 = True
while p1:
    anime_name = input("Enter an anime (or type \"exit\" to stop): ")

    if anime_name.lower() == "exit":
        print("You have exited the anime entry program")
        p1 = False
        
    else:
        anime_list.append(anime_name)
        
print("Your anime list includes: ")
for anime_name in anime_list:
    print(f"-{anime_name}")


