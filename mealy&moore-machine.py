class FiniteStateMachine:
    def __init__(self, states, initial_state):
        self.states = states
        self.current_state = initial_state

    def reset(self):
        self.current_state = self.states[0]

    def get_current_state(self):
        return self.current_state


class MooreMachine(FiniteStateMachine):
    def __init__(self):
        super().__init__(states=['A', 'B', 'C'], initial_state='A')

        self.state_outputs = {
            'A': 'b',
            'B': 'b',
            'C': 'a',
        }
        self.transitions = {
            'A': {'0': 'B', '1': 'A'},
            'B': {'0': 'B', '1': 'C'},
            'C': {'0': 'B', '1': 'A'},
        }

        self.state_sequence = []
        self.final_states = ['A', 'B', 'C']

    def reset(self):
        super().reset()
        self.state_sequence = []

    def process_input(self, input_symbol):
        if input_symbol not in self.transitions[self.current_state]:
            raise ValueError(
                f"Invalid input '{input_symbol}' for {self.current_state}")

        next_state = self.transitions[self.current_state][input_symbol]
        self.state_sequence.append(self.current_state)
        self.current_state = next_state
        return self.state_outputs[self.current_state]

    def process_string(self, input_string):
        self.reset()
        outputs = [self.state_outputs[self.current_state]]
        for ch in input_string:
            outputs.append(self.process_input(ch))
        return outputs

    def get_state_sequence(self):
        return self.state_sequence + [self.current_state]

    def display_transition_table(self):
        print("\n" + "=" * 60)
        print("MOORE MACHINE TRANSITION TABLE")
        print("=" * 60)
        print("Current | Output | 0 → | 1 →")
        print("-" * 60)
        for s in self.states:
            print(
                f"{s:^8}| {self.state_outputs[s]:^7}| {self.transitions[s]['0']:^5}| {self.transitions[s]['1']:^5}")
        print("=" * 60)
        print(f"Initial State: {self.states[0]}")
        print(f"Final States: {self.final_states}")
        print("=" * 60)


class MealyMachine(FiniteStateMachine):

    def __init__(self):
        super().__init__(states=['A', 'B', 'C'], initial_state='A')

        self.final_states = ['A', 'B', 'C']
        self.transitions = {
            'A': {'0': ('b', 'B'), '1': ('b', 'A')},
            'B': {'0': ('b', 'B'), '1': ('a', 'C')},
            'C': {'0': ('b', 'A'), '1': ('b', 'C')}
        }

        self.prev_symbol = None
        self.state_sequence = []

    def reset(self):
        super().reset()
        self.prev_symbol = None
        self.state_sequence = []

    def process_input(self, input_symbol):
        if input_symbol not in self.transitions[self.current_state]:
            raise ValueError(
                f"Invalid input '{input_symbol}' for {self.current_state}")

        _, next_state = self.transitions[self.current_state][input_symbol]
        output = 'a' if self.prev_symbol == '0' and input_symbol == '1' else 'b'

        self.state_sequence.append(self.current_state)
        self.current_state = next_state
        self.prev_symbol = input_symbol
        return output

    def process_string(self, input_string):
        self.reset()
        outputs = []
        for ch in input_string:
            outputs.append(self.process_input(ch))
        return outputs

    def get_state_sequence(self):
        return self.state_sequence + [self.current_state]

    def display_transition_table(self):
        print("\n" + "=" * 60)
        print("MEALY MACHINE TRANSITION TABLE")
        print("=" * 60)
        print("State | Input | Output | Next")
        print("-" * 60)
        for s in self.states:
            for i in ['0', '1']:
                o, n = self.transitions[s][i]
                print(f"{s:^6}| {i:^6}| {o:^7}| {n:^6}")
        print("=" * 60)
        print(f"Initial State: {self.states[0]}")
        print(f"Final States: {self.final_states}")
        print("=" * 60)


class MachineSimulator:

    @staticmethod
    def run():
        print("=" * 60)
        print("FINITE STATE MACHINE SIMULATOR (OOP VERSION)")
        print("=" * 60)

        while True:
            print("\nChoose a machine:")
            print("1. Moore Machine")
            print("2. Mealy Machine")
            print("3. Exit")

            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == '1':
                MachineSimulator.test_moore()
            elif choice == '2':
                MachineSimulator.test_mealy()
            elif choice == '3':
                print("Exiting simulator...")
                break
            else:
                print("Invalid choice. Try again.")

    @staticmethod
    def test_moore():
        machine = MooreMachine()
        machine.display_transition_table()
        input_str = input("Enter input string (only 0s and 1s): ").strip()
        if not all(ch in '01' for ch in input_str):
            print("Invalid input.")
            return
        outputs = ''.join(machine.process_string(input_str))
        print(f"\nInput:  {input_str}")
        print(f"Output: {outputs}")
        print(f"State Sequence: {' → '.join(machine.get_state_sequence())}")
        print(f"Final State: {machine.get_current_state()}")

    @staticmethod
    def test_mealy():
        machine = MealyMachine()
        machine.display_transition_table()
        input_str = input("Enter input string (only 0s and 1s): ").strip()
        if not all(ch in '01' for ch in input_str):
            print("Invalid input.")
            return
        outputs = ''.join(machine.process_string(input_str))
        print(f"\nInput:  {input_str}")
        print(f"Output: {outputs}")
        print(f"State Sequence: {' → '.join(machine.get_state_sequence())}")
        print(f"Final State: {machine.get_current_state()}")


if __name__ == "__main__":
    MachineSimulator.run()
