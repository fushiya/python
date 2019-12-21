from datetime import timedelta

print("Завдання описано в 'Task-1.jpg'")

def start():
    print("---------------------------------")
    print('Введіть час в форматі <hh>:<mm>:<ss>')

    a = input("Час 1: ").split(":")
    b = input("Час 2: ").split(":")

    a = [int(item) for item in a]
    b = [int(item) for item in b]

    d1 = timedelta(hours=a[0], minutes=a[1], seconds=a[2])
    d2 = timedelta(hours=b[0], minutes=b[1], seconds=b[2])

    print( " ".join(str((d2 - d1)).split(":")) )


if __name__ == "__main__":
    start()