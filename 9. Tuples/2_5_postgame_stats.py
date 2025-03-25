if __name__ == "__main__":

    player1 = {
        "name" : "Lebron James",
        "position" : "Small Forward",
        "stat" : "30.2"
    }

    player2 = {
        "name" : "Steph Curry",
        "position" : "Point Guard",
        "stat" : "28.2"
    }

    player3 = {
        "name" : "Shaquille O'Neal",
        "position" : "Center",
        "stat" : "35.2"
    }

    players = player1, player2, player3

    for player in players:
        print(player["position"])

    player1["stat"] = "40.2"

    print(player1["stat"])

    average = ( float(player1["stat"]) + float(player2["stat"]) + float(player2["stat"]) ) / 3

    print(average)