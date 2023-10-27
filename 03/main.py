from collections.abc import Iterable
import dataclasses


@dataclasses.dataclass
class Rucksack:
    compartments: list[set[str]]

class FileRucksackFactory:
    def __init__(self, filename: str):
        self.__filename = filename
        
    def get_rucksacks(self) -> Iterable[Rucksack]:
        with open(self.__filename, "r") as file:
            for line in file:
                print('test')
                line = line.strip()
                half = len(line) // 2
                compartment_1 = set(line[:half])
                compartment_2 = set(line[half:])
                yield Rucksack([compartment_1, compartment_2])

class ItemPriorityCalculator:
    _test = 123
    __first_priority_lower = ord("a")
    __last_priority_lower = ord("z")

    __first_priority_upper = ord("A")
    __last_priority_upper = ord("Z")

    def get_priority(self, item: str) -> int:
        # get ascii value of item
        ascii_value = ord(item)

        if self.__first_priority_lower <= ascii_value <= self.__last_priority_lower:
            return ascii_value - self.__first_priority_lower + 1
        elif self.__first_priority_upper <= ascii_value <= self.__last_priority_upper:
            return ascii_value - self.__first_priority_upper + 27

        raise ValueError(f"Invalid item: {item}")

def p1():
    priority_calculator = ItemPriorityCalculator()

    factory = FileRucksackFactory("input.txt")
    rucksacks = factory.get_rucksacks()

    priority_sum = 0

    for rucksack in rucksacks:
        repeated_items = set.intersection(*rucksack.compartments)

        for item in repeated_items:
            priority = priority_calculator.get_priority(item)
            priority_sum += priority

def p2():
    group_size = 3
    full_rucksacks = [set() for _ in range(group_size)]
    priority_calculator = ItemPriorityCalculator()

    factory = FileRucksackFactory("input.txt")
    rucksacks = factory.get_rucksacks()

    priority_sum = 0

    for i, rucksack in enumerate(rucksacks):
        modulo = i % group_size

        full_rucksacks[modulo] = set.union(*rucksack.compartments)

        if modulo == group_size - 1:
            repeated_items = set.intersection(*full_rucksacks)

            for item in repeated_items:
                priority = priority_calculator.get_priority(item)
                priority_sum += priority


if __name__ == "__main__":
    p1()
    p2()