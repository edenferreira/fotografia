import os

def all_file_names(year, month):
    files = os.listdir(f".\\public\\{year}\\{month}\\")
    just_names = set()
    for f in files:
        name = f.replace("FHD", "RES").replace("1k", "RES").replace("2k", "RES").replace("4k", "RES")
        just_names.add(name)
    return just_names


if __name__ == "__main__":
    with open(".\\public\\2024_janeiro.manifest", "x") as f:
        f.write('\n'.join(all_file_names(2024, "janeiro")))
