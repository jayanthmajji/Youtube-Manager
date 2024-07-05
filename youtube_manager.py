import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []


def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_videos(videos):
    print("\n")
    print("*" * 50)
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 50)


def add_video(videos):
    name = input("Enter the name of the viedo: ")
    time = input("Enter time of the viedo: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)


def update_video(videos):
    list_videos(videos)
    number = int(input("Enter the video number to update: "))
    if (1 <= number <= len(videos)):
        name = input("Enter the new video name: ")
        time = input("Enter the time of the new video: ")
        videos[number - 1] = {'name': name, 'time': time}
        save_data(videos)
    else:
        print("Invalid index selected!")


def delete_video(videos):
    list_videos(videos)
    num = int(input("Enter the video number to be deleted: "))
    if (1 <= num <= len(videos)):
        del videos[num - 1]
        save_data(videos)
        print("Deleted successfully")
    else:
        print("Invalid video number selected!")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager || choose an option")
        print("1. List all youtube viedos")
        print("2. Add a youtube viedo")
        print("3. Update a youtube viedo details")
        print("4. Delete a youtube viedo")
        print("5. Exit the app")
        choise = input("Enter your choice: ")
        # print(videos)

        match choise:
            case '1':
                list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choise!")


if __name__ == "__main__":
    main()
