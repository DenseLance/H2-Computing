from socket import socket

# Hide-and-seek
server_location = [0, 0]
client_location = [5, 5]
server_board = [["0" for _ in range(6)] for _ in range(6)]
server_board[server_location[1]][server_location[0]] = "S"
number_of_turns = 1

# Data validation
def start_menu():
    menu = """
            Who is the seeker?
            [1] Server
            [2] Client
            > """
    user_input = input(menu)
    while not validate_menu(user_input):
        user_input = input(menu)
    return int(user_input)

def validate_menu(user_input):
    if len(user_input) == 0: # presence check
        return False
    elif not user_input.isdigit(): # type check
        return False
    elif int(user_input) not in [1, 2]: # restricted value check
        return False
    else:
        return True

def move(server_board):
    for row in server_board:
        print("".join(row)) # print board
    x = input("x:")
    while not validate_move(x):
        x = input("x:")
        
    y = input("y:")
    while not validate_move(y):
        y = input("y:")
    return [int(x), int(y)]

def validate_move(move):
    if len(move) == 0: # presence check
        return False
    elif not move.isdigit(): # type check
        return False
    elif int(move) < 0 or int(move) > 5: # range check
        return False
    else:
        return True

# Socket
server = socket()
server.bind(("127.0.0.1", 12345))
server.listen()
client, address = server.accept()

# Game
done = False
protocols = [b"START", b"MOVE"]
start = start_menu()
if start == 1: # server is seeker
    print("YOU ARE SEEKER")
else: # server is hider
    print("YOU ARE HIDER")
client.sendall(protocols[0] + f"{start}\n".encode())
        
while not done:
    if start == 1: # server is seeker
        # hider (client) moves first
        print("CLIENT MOVE")
        received = b""
        while b"\n" not in received:
            received += client.recv(1024)
        if protocols[1] in received:
            temp = received.decode()[4:-1].split(",")
            client_location = [int(temp[1]), int(temp[0])]

        # seeker (server) moves second
        print("SERVER MOVE")
        prev_location = server_location
        server_location = move(server_board)
        server_board[prev_location[1]][prev_location[0]] = "0"
        server_board[server_location[1]][server_location[0]] = "S"
        client.sendall(protocols[1] + f"{server_location[1]},{server_location[0]}\n".encode())
        
    else: # server is hider
        # hider (server) moves first
        print("SERVER MOVE")
        prev_location = server_location
        server_location = move(server_board)
        server_board[prev_location[1]][prev_location[0]] = "0"
        server_board[server_location[1]][server_location[0]] = "S"
        client.sendall(protocols[1] + f"{server_location[1]},{server_location[0]}\n".encode())

        # seeker (client) moves second
        print("CLIENT MOVE")
        received = b""
        while b"\n" not in received:
            received += client.recv(1024)
        if protocols[1] in received:
            temp = received.decode()[4:-1].split(",")
            client_location = [int(temp[1]), int(temp[0])]

    if server_location == client_location: # hider is found
        print(f"Seeker found hider in {number_of_turns} turns!")
        done = True
        
    number_of_turns += 1

client.close()
server.close()
