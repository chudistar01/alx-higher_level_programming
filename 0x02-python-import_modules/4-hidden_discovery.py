#!/usr/bin/python3

if __name__ == "__main__":
    """prints all the names defined by hidden"""
    import hidden_4

    hiddens = dir(hidden_4)
    for hidden in hiddens:
        if hidden[:2] != "__":
            print(hidden)
