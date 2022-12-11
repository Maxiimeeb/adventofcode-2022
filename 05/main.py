import abc
import dataclasses
import os
import re
from collections.abc import Iterable


@dataclasses.dataclass
class Container:
    letter: str


class ContainerShip:
    def __init__(self, stack_count: int):
        self.__stacks: dict[int, ] = {}

        for i in range(stack_count):
            self.__stacks[i + 1] = []

    def add_container(self, container: Container, stack_id: int):
        self.__stacks[stack_id].append(container)

    def remove_container(self, stack_id: int) -> Container:
        """
        :raises: IndexError
        """
        return self.__stacks[stack_id].pop()

    def peek_container(self, stack_id: int) -> Container:
        """
        :raises: IndexError
        """
        return self.__stacks[stack_id][-1]

    @property
    def stack_count(self) -> int:
        return len(self.__stacks)


class Crane(abc.ABC):
    @abc.abstractmethod
    def move_container(self, from_stack_id: int, to_stack_id: int, quantity: int):
        pass


class Crane9001(Crane):
    def __init__(self, ship: ContainerShip):
        self.__ship = ship

    def move_container(self, from_stack_id: int, to_stack_id: int, quantity: int):
        """
        :raises: IndexError
        """
        containers = []

        for _ in range(quantity):
            container = self.__ship.remove_container(from_stack_id)
            containers.append(container)

        for container in reversed(containers):
            self.__ship.add_container(container, to_stack_id)


class Crane9000(Crane):
    def __init__(self, ship: ContainerShip):
        self.__ship = ship

    def move_container(self, from_stack_id: int, to_stack_id: int, quantity: int):
        """
        :raises: IndexError
        """
        for _ in range(quantity):
            container = self.__ship.remove_container(from_stack_id)
            self.__ship.add_container(container, to_stack_id)


@dataclasses.dataclass
class CraneCommand:
    from_stack_id: int
    to_stack_id: int
    quantity: int


class CraneController:
    def __init__(self, crane: Crane):
        self.__crane = crane

    def execute_command(self, command: CraneCommand):
        self.__crane.move_container(command.from_stack_id, command.to_stack_id, command.quantity)

class FilePuzzleFactory:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_container_ship(self) -> ContainerShip:
        is_first_line = True

        with open(self.__file_path, 'r') as file:
            reversed_containers = {}

            for line in file:

                line = line.rstrip(os.linesep)

                if is_first_line:
                    stack_count = (len(line) // 4) + 1  # Will not se any diff between 0 and 1 stack
                    ship = ContainerShip(stack_count)

                    for i in range(stack_count):
                        reversed_containers[i + 1] = []

                    is_first_line = False

                if self.__is_command(line):
                    break

                for match in re.finditer(r'\[([a-zA-Z])\]', line):
                    container_letter = match.group(1)
                    stack_id = match.start() // 4 + 1

                    reversed_containers[stack_id].append(Container(container_letter))

        for stack_id, containers in reversed_containers.items():
            for container in reversed(containers):
                ship.add_container(container, stack_id)
                
        return ship

    def get_command(self) -> Iterable[CraneCommand]:
        with open(self.__file_path, 'r') as file:
            for line in file:
                line = line.rstrip(os.linesep)

                if self.__is_command(line):
                    # move 1 from 2 to 1
                    match = re.match(r'move (\d+) from (\d+) to (\d+)', line)
                    from_stack_id = int(match.group(2))
                    to_stack_id = int(match.group(3))
                    quantity = int(match.group(1))

                    yield CraneCommand(from_stack_id, to_stack_id, quantity)


    def __is_command(self, line: str) -> bool:
        return line.startswith('move')


def p1():
    factory = FilePuzzleFactory('input.txt')
    ship = factory.get_container_ship()

    crane = Crane9000(ship)
    controller = CraneController(crane)

    for command in factory.get_command():
        controller.execute_command(command)
    
    result = ''
    for i in range(0, ship.stack_count):
        stack_id = i + 1

        result += f'{ship.peek_container(stack_id).letter}'

    print(result)


def p2():
    factory = FilePuzzleFactory('input.txt')
    ship = factory.get_container_ship()

    crane = Crane9001(ship)
    controller = CraneController(crane)

    for command in factory.get_command():
        controller.execute_command(command)
    
    result = ''
    for i in range(0, ship.stack_count):
        stack_id = i + 1

        result += f'{ship.peek_container(stack_id).letter}'

    print(result)

if __name__ == '__main__':
    p1()
    p2()