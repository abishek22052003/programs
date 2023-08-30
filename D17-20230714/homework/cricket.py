players=[{"country":"Sri Lanka","name":"Kumar Sangakara","centuries":25,"half centuries":93,"wickets taken":0,"hat-trick wickets":0,"top_batting_scores":4696},
         {"country":"Austalia","name":"Pat Cummmins","centuries":0,"half centuries":0,"wickets taken":124,"hat-trick wickets":6,"top_batting_scores":324},
         {"country":"West Indies","name":"Jason holder","centuries":0,"half centuries":12,"wickets taken":159,"hat-trick wickets":4,"top_batting_scores":606},
         {"country":"India","name":"Dhoni","centuries":46,"half centuries":65,"wickets taken":4,"hat-trick wickets":0,"top_batting_scores":7598},
         {"country":"Afghanistan","name":"Rashid Khan","centuries":0,"half centuries":5,"wickets taken":167,"hat-trick wickets":5,"top_batting_scores":458}]
def centuries(players):
    num=0
    sum=0
    for player in players:
        if player["centuries"]>10:
            num=num+1
        if player["hat-trick wickets"]>5:
            print("MOST HAT TRICK WICKET PLAYER")
            print(player["name"])
            print("\n")
        for player in players:
            if player["top_batting_scores"]>sum:
                    sum=sum>player
                    print(sum)
                    # return sum
                    
    return num
            
check=centuries(players)
print("\n")
print("MOST CENTURY PLAYERS")
print(check)
