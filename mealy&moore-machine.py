class FiniteStateMachine:
    def __init__(self, states, initial):
        self.states = states
        self.initial_state = initial
        self.state = initial

    def reset(self):
        self.state = self.initial_state


class MooreMachine(FiniteStateMachine):
    def __init__(self):
        super().__init__(['A', 'B', 'C'], 'A')

    def get_output(self, state):
        if state == 'A':
            return 'b'
        elif state == 'B':
            return 'b'
        elif state == 'C':
            return 'a'

    def process(self, inp):
        self.reset()
        output = self.get_output(self.state)

        for ch in inp:
            if self.state == 'A':
                if ch == '0':
                    self.state = 'B'
                else:
                    self.state = 'A'

            elif self.state == 'B':
                if ch == '0':
                    self.state = 'B'
                else:
                    self.state = 'C'

            elif self.state == 'C':
                if ch == '0':
                    self.state = 'B'
                else:
                    self.state = 'A'

            output += self.get_output(self.state)

        print("\n--- Moore Machine ---")
        print("Input:  ", inp)
        print("Output: ", output)
        print("Final State:", self.state)


class MealyMachine(FiniteStateMachine):
    def __init__(self):
        super().__init__(['A', 'B', 'C'], 'A')

    def process(self, inp):
        self.reset()
        output = ""

        for ch in inp:
            if self.state == 'A':
                if ch == '0':
                    output += 'b'
                    self.state = 'B'
                else:
                    output += 'b'
                    self.state = 'A'

            elif self.state == 'B':
                if ch == '0':
                    output += 'b'
                    self.state = 'B'
                else:
                    output += 'a'
                    self.state = 'C'

            elif self.state == 'C':
                if ch == '0':
                    output += 'b'
                    self.state = 'B'
                else:
                    output += 'b'
                    self.state = 'A'

        print("\n--- Mealy Machine ---")
        print("Input:  ", inp)
        print("Output: ", output)
        print("Final State:", self.state)


def main():
    print("=" * 50)
    print("EXAMPLE DEMO:")
    example_input = "110011"
    print(f"Sample Input: {example_input}")

    moore = MooreMachine()
    moore.process(example_input)

    mealy = MealyMachine()
    mealy.process(example_input)
    print("=" * 50)

    while True:
        print("\n1. Moore Machine\n2. Mealy Machine\n3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            m = MooreMachine()
            s = input("Enter input (0s and 1s): ").strip()
            m.process(s)
        elif choice == "2":
            m = MealyMachine()
            s = input("Enter input (0s and 1s): ").strip()
            m.process(s)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
