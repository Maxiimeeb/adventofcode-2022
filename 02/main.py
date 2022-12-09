import enum


class PlayResult(enum.Enum):
    WIN = -1
    TIE = 0
    LOSE = 1

    def get_reverse(self) -> "PlayResult":
        return PlayResult(-self.value)
        
class RockPaperScissorChoice:
    def __init__(self, name: str, chars: list[str], point: int):
        self.name = name
        self.chars = chars
        self.point = point

class PlayComparator:
    def __init__(self, winning_point: int, losing_point: int, tie_point: int):
        self.__winning_point = winning_point
        self.__losing_point = losing_point
        self.__tie_point = tie_point

    @property
    def winning_point(self) -> int:
        return self.__winning_point

    @property
    def losing_point(self) -> int:
        return self.__losing_point

    @property
    def tie_point(self) -> int:
        return self.__tie_point

    def get_match_score(self, choice1: RockPaperScissorChoice, choice2: RockPaperScissorChoice) -> int:
        if choice1.point == choice2.point:
            return self.__tie_point
        elif choice1.point % 3 + 1 == choice2.point:
            return self.__losing_point
        else:
            return self.__winning_point

class ChoiceFactory:
    def __init__(self, comparator: PlayComparator):
        self.__comparator = comparator
        self.choices = {
            "rock": RockPaperScissorChoice("rock", {"A", "X"}, 1),
            "paper": RockPaperScissorChoice("paper", {"B", "Y"}, 2),
            "scissor": RockPaperScissorChoice("scissor", {"C", "Z"}, 3),
        }

    def get_choice(self, choice: str) -> RockPaperScissorChoice:
        for key, value in self.choices.items():
            if choice in value.chars:
                return value

        raise ValueError(f"Invalid choice: {choice}")

    def get_choice_from_play_result(self, choice1: RockPaperScissorChoice, result: PlayResult) -> RockPaperScissorChoice:
        target_score = None

        if result == PlayResult.WIN:
            target_score = self.__comparator.winning_point
        elif result == PlayResult.LOSE:
            target_score = self.__comparator.losing_point
        elif result == PlayResult.TIE:
            target_score = self.__comparator.tie_point

        for _, value in self.choices.items():
            game_result = self.__comparator.get_match_score(choice1, value)

            if game_result == target_score:
                return value
    
def p1():
    play_comparator = PlayComparator(
        winning_point=6,
        tie_point=3,
        losing_point=0,
    )
    choice_factory = ChoiceFactory(play_comparator)
    current_score = 0

    with open("input.txt", "r") as f:
        for line in f:
            oponentRaw, meRaw = line.strip().split(' ')
            oponent = choice_factory.get_choice(oponentRaw)
            me = choice_factory.get_choice(meRaw)

            current_score += play_comparator.get_match_score(
                me,
                oponent,
            )
            current_score += me.point

    print(current_score)

def p2():
    mapping = {
        'X': PlayResult.LOSE,
        'Y': PlayResult.TIE,
        'Z': PlayResult.WIN,
    }
    play_comparator = PlayComparator(
        winning_point=6,
        tie_point=3,
        losing_point=0,
    )
    choice_factory = ChoiceFactory(play_comparator)
    current_score = 0

    with open("input.txt", "r") as f:
        for line in f:
            oponentRaw, meRaw = line.strip().split(' ')
            oponent = choice_factory.get_choice(oponentRaw)
            me = choice_factory.get_choice_from_play_result(oponent, mapping[meRaw].get_reverse())

            current_score += play_comparator.get_match_score(
                me,
                oponent,
            )
            current_score += me.point

    print(current_score)

if __name__ == "__main__":
    p1()
    p2()
