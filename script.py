import subprocess
import shlex
import os
import shutil

# ----- Functions ----- #

def install_program(program):
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm", program])


def bash(command):
    args = shlex.split(command)
    return subprocess.run(args)


def command_exists(cmd):
    return subprocess.run(["which", cmd], stdout=subprocess.DEVNULL).returncode == 0


def install_configs():
    repo_path = os.getcwd()
    config_path = os.path.expanduser("~/.config")

    os.makedirs(config_path, exist_ok=True)

    configs = [
        "hypr",
        "kitty",
        "dunst",
        "wofi",
        "waybar"
    ]

    for cfg in configs:
        src = os.path.join(repo_path, cfg)
        dst = os.path.join(config_path, cfg)

        if os.path.exists(src):
            print(f"Installing {cfg} config...")

            if os.path.exists(dst):
                shutil.rmtree(dst)

            shutil.copytree(src, dst)

# ----- Variables ----- #

title = """
▄▖▜   ▌ ▌    ▖▖      ▜      ▌  ▄   ▗   
▌▌▐ ▛▌▛▌ ▛▘  ▙▌▌▌▛▌▛▘▐ ▀▌▛▌▛▌  ▌▌▛▌▜▘▛▘
▛▌▐▖▙▌▌▌ ▄▌  ▌▌▙▌▙▌▌ ▐▖█▌▌▌▙▌  ▙▘▙▌▐▖▄▌
    ▌          ▄▌▌                     
"""

installs = [
    "dolphin",
    "dunst",
    "grim",
    "hyprland",
    "kitty",
    "polkit-kde-agent",
    "qt5-wayland",
    "qt6-wayland",
    "slurp",
    "uwsm",
    "wofi",
    "waybar",
    "xdg-desktop-portal-hyprland",
    "noto-fonts",
    "noto-fonts-cjk",
    "noto-fonts-emoji",
    "ttf-jetbrains-mono-nerd"
]

# ----- Begin program ----- #

print(title)
print("Installing Hyprland dotfiles...")

# Install packages
for program in installs:
    install_program(program)

# Install configs
install_configs()

# Wallpaper script
wallpaper_script = os.path.join(os.getcwd(), "scripts", "wallpaper.sh")

if os.path.exists(wallpaper_script):
    bash(f"chmod +x {wallpaper_script}")
    bash(wallpaper_script)

# Audio
if not command_exists("pipewire") and not command_exists("pulseaudio"):
    print("No audio system found.")
    print("Install (1) PipeWire or (2) PulseAudio?")
    choice = input("> ")

    if choice == "1":
        bash("sudo pacman -S --noconfirm pipewire pipewire-pulse wireplumber")
    else:
        bash("sudo pacman -S --noconfirm pulseaudio pulseaudio-alsa")

# Bluetooth
print("Installing Bluetooth...")
bash("sudo pacman -S --noconfirm blueman bluez bluez-utils")

print("Installation complete.")
