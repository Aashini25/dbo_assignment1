class Rover:
    def __init__(self, x, y, dir, plateau_limits):
        self.x = x
        self.y = y
        self.dir = dir.upper()
        self.plateau_limits = plateau_limits
        self.dirs = ['N', 'E', 'S', 'W']

    def rotate_left(self):
        curr_index = self.dirs.index(self.dir)
        self.dir = self.dirs[(curr_index - 1) % 4]

    def rotate_right(self):
        current_index = self.dirs.index(self.dir)
        self.dir = self.dirs[(current_index + 1) % 4]

    def move_forward(self):
        if self.dir == 'N' and self.y < self.plateau_limits[1]:
            self.y += 1
        elif self.dir == 'E' and self.x < self.plateau_limits[0]:
            self.x += 1
        elif self.dir == 'S' and self.y > 0:
            self.y -= 1
        elif self.dir == 'W' and self.x > 0:
            self.x -= 1

    def exec_commands(self, commands):
        commands = commands.upper()
        for command in commands:
            if command == 'L':
                self.rotate_left()
            elif command == 'R':
                self.rotate_right()
            elif command == 'M':
                self.move_forward()

    def get_position(self):
        return f"{self.x} {self.y} {self.dir}"


def norm_input(input_str):
    input_str = input_str.strip()
    if " " in input_str:  # Standard case
        return list(map(int, input_str.split()))
    elif len(input_str) == 2:  # Concatenated case
        return [int(input_str[0]), int(input_str[1])]
    else:
        raise ValueError("Invalid plateau input format.")


def parse_init_pos(pos_str):
    pos_str = pos_str.strip().upper()
    if " " in pos_str:  # Standard case
        parts = pos_str.split()
        if len(parts) == 3 and parts[2] in ['N', 'E', 'S', 'W']:
            return int(parts[0]), int(parts[1]), parts[2]
    elif len(pos_str) >= 3:  # Concatenated case
        *coords, direction = pos_str
        if direction in ['N', 'E', 'S', 'W']:
            x, y = map(int, coords)
            return x, y, direction
    raise ValueError("Invalid position format.")


def main():
    try:
        plateau_size_raw = input()
        plateau_limits = tuple(norm_input(plateau_size_raw))
        n = int(input())
        results = []
        for _ in range(n):
            position_raw = input()
            x, y, direction = parse_init_pos(position_raw)
            commands = input().upper()  
            rover = Rover(x, y, direction, plateau_limits)
            rover.exec_commands(commands)
            results.append(rover.get_position())
        print("\n".join(results))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
