import sys 
import os

def progressbar(it, prefix="", size=60, out=sys.stdout):
    #left for reference, but no longer needed
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print(f"{prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count}", end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)
def generate_steam_paths():
    drive_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    steam_installation_path = "Program Files (x86)\\Steam"  # Default Steam installation path on 64-bit Windows

    steam_paths = []

    for drive_letter in drive_letters:
        path = f"{drive_letter}:\\{steam_installation_path}"
        steam_paths.append(path)

        for custom_path in ["Steam", "Games\\Steam", "SteamLibrary"]:
            path = f"{drive_letter}:\\{custom_path}"
            steam_paths.append(path)

    return steam_paths
def guess_mod_pack_path(target_workspace):
    for i in range(2,16):
        filename = f'data{i}.pak'
        guess = os.path.join(target_workspace, filename)
        if os.path.exists(guess):
            return guess
    else:
        return None
        

def guess_workspace_path():
    steam_paths = generate_steam_paths()

    for path in steam_paths:
        workspace_guess = os.path.join(path, 'steamapps', 'common', 'Dying Light 2', 'ph', 'source')
        
        if os.path.exists(workspace_guess):
            return workspace_guess
    else:
        return None


def resource_path(relative_path):
    """standardize relative references"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_int_date():
    import datetime
    current_date = datetime.datetime.now()
    return current_date.strftime("%Y-%m-%d")
run_number = get_int_date()
