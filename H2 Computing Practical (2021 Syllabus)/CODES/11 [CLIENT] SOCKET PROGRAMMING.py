from socket import socket

# Hide-and-seek
server_location = [0, 0]
client_location = [5, 5]
client_board = [["0" for _ in range(6)] for _ in range(6)]
client_board[client_location[1]][client_location[0]] = "C"
number_of_turns = 1

# Data validation
def move(client_board):
    for row in client_board:
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
client = socket()
client.connect(("127.0.0.1", 12345))

# Game
done = False
protocols = [b"START", b"MOVE"]
received = b""
while b"\n" not in received:
    received += client.recv(1024)
if protocols[0] in received:
    start = int(received.decode()[5])
if start == 1: # client is hider
    print("YOU ARE HIDER")
else: # client is seeker
    print("YOU ARE SEEKER")

while not done:
    if start == 1: # client is hider
        # hider (client) moves first
        print("CLIENT MOVE")
        prev_location = client_location
        client_location = move(client_board)
        client_board[prev_location[1]][prev_location[0]] = "0"
        client_board[client_location[1]][client_location[0]] = "C"
        client.sendall(protocols[1] + f"{client_location[1]},{client_location[0]}\n".encode())
        
        # seeker (server) moves second
        print("SERVER MOVE")
        received = b""
        while b"\n" not in received:
            received += client.recv(1024)
        if protocols[1] in received:
            temp = received.decode()[4:-1].split(",")
            server_location = [int(temp[1]), int(temp[0])]
        
    else: # client is seeker
        # hider (server) moves first
        print("SERVER MOVE")
        received = b""
        while b"\n" not in received:
            received += client.recv(1024)
        if protocols[1] in received:
            temp = received.decode()[4:-1].split(",")
            server_location = [int(temp[1]), int(temp[0])]

        # seeker (client) moves second
        print("CLIENT MOVE")
        prev_location = client_location
        client_location = move(client_board)
        client_board[prev_location[1]][prev_location[0]] = "0"
        client_board[client_location[1]][client_location[0]] = "C"
        client.sendall(protocols[1] + f"{client_location[1]},{client_location[0]}\n".encode())

    if server_location == client_location: # hider is found
        print(f"Seeker found hider in {number_of_turns} turns!")
        done = True
        
    number_of_turns += 1

client.close()
