team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players(players: list[dict]) -> None:
    """This function prints all players to the client"""

    for player in players:
        print(f"Player:{player['name']},{player['age']},{player['number']}")


def add_player(players: list[dict], num: int, name: str, age: int) -> None:
    """This function adds a new player."""

    for player in players:
        if player["number"] == num:
            print(f"{num} player already exists.")
            return
    players.append({"name": name, "age": age, "number": num})
    print(f"Name: {name}, Age: {age}, Number: {num} is added")


def remove_player(players: list[dict], num: int) -> None:
    """This function removes the player by their number."""
    for player in players:
        if player["number"] == num:
            players.remove(player)
            print(f"Player with number: {num} is removed")
            return
    print(f"No player with number: {num}")


def main():
    show_players(team)

    add_player(players=team, num=1, name="Allan", age=44)
    add_player(players=team, num=57, name="Sam", age=23)
    remove_player(players=team, num=8)

    show_players(team)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module is only for running")
