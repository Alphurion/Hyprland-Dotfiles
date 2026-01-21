import os
import subprocess
import random
from pathlib import Path

Dark_Folder = Path.home() / "Pictures/Wallpapers/Dark"
Light_Folder = Path.home() / "Pictures/Wallpapers/Light"


def Wallpaper_Counter(folder):
    return sum(1 for file in os.listdir(folder))

Dark_Count = Wallpaper_Counter(Dark_Folder)
Light_Count = Wallpaper_Counter(Light_Folder)

def Random_Wallpaper(Monitor):
   
    winner = random.choice([True, False])

    if winner:
        choice = random.randint(1, Light_Count)
        string = f"{Monitor},{Light_Folder}/{choice}.png"
    else:
        choice = random.randint(1, Dark_Count)
        string = f"{Monitor},{Dark_Folder}/{choice}.png"
    subprocess.run(["hyprctl", "hyprpaper", "wallpaper", string])

Random_Wallpaper("DP-3")
