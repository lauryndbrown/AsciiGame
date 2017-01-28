class Player:
    """
    Generic Player Class used by Game
    """
    def __init__(self, name, high_score=0):
        self.name = name
        self.high_score = high_score
        self.score = 0
