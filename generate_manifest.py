import os

def all_file_names(year, month):
    files = os.listdir(f".\\public\\{year}\\{month}\\")
    just_names = set()
    for f in files:
        name = f.replace("FHD", "RES").replace("1K", "RES").replace("2K", "RES").replace("4K", "RES")
        just_names.add(name)
    return sorted(list(just_names))


if __name__ == "__main__":
    try:
        with open(".\\public\\2024_janeiro.manifest", "x") as f:
            f.write('\n'.join(all_file_names(2024, "janeiro")))
    except FileExistsError:
        pass
    
    try:
        with open(".\\public\\2023_setembro.manifest", "x") as f:
            f.write('\n'.join(all_file_names(2023, "setembro")))
    except FileExistsError:
        pass
