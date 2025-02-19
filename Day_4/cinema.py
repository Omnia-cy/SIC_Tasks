import json
info = []
def add_show():

    TV_info = open("data.json", 'r')
    info = json.load(TV_info)
    title = input("title: ")
    publish_year = input("publish year: ")
    data = {
        "Title": title,
        "Year": publish_year
    }
  
    info.append(data)
    TV_info = open("data.json", 'w')
    json.dump(info, TV_info, indent=4)
    TV_info.close()
    print("TV show added successfully! ")

def remove_show():

    TV_info = open("data.json", 'r')
    info = json.load(TV_info)
    title = input("Enter the title of the TV show to remove: ")
    show_removed = False
    for show in info:
        if show["Title"] == title:
            info.remove(show)
            show_removed = True

  
    if show_removed:
        with open("data.json", 'w') as TV_info:
            json.dump(info, TV_info, indent=4)
        print("TV show removed successfully!")
    else:
        print("TV show not found!")


def search_for_show():

    title = input("Enter the title of the TV show you search for: ")
    TV_info = open("data.json", 'r')
    info = json.load(TV_info)
    found_shows = [show for show in info if show["Title"] == title]

    if found_shows:
        for show in found_shows:
            print("Title:", show["Title"], "\nyear of Publishing:", show["Year"])
    else:
        print("TV show not found.")


def show_all_tv_shows():
    TV_info = open("data.json", 'r')
    info = json.load(TV_info)
    for show in info:
        print("Title:", show["Title"], "\nyear of Publishing:", show["Year"],"\n\n")



while True:
    print("Menu:")
    print("[1] Add TV Show")
    print("[2] Remove TV Show")
    print("[3] Search for TV Show")
    print("[4] Show All TV Shows")
    print("[5] Close the Program")

    option = int(input("Enter your choice: "))
    if option == 1:
        add_show()
    elif option == 2:
        remove_show()
    elif option == 3:
        search_for_show()
    elif option == 4:
        show_all_tv_shows()
    elif option > 5:
        print("Invalid option")
    elif option == 5:
        print("Visit us again ^.^")
        break

