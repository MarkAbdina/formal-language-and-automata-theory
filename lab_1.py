# DFA Simulator
def run_dfa(transitions, start, accept, string):
    state = start
    for ch in string:
        if (state, ch) in transitions:
            state = transitions[(state, ch)]
        else:
            return False  # invalid symbol or missing transition
    return state in accept

# ---------- Automaton 1 ----------
# States: a, b, 1
transitions1 = {
    ('a', '0'): 'a',
    ('a', '1'): 'b',
    ('b', '0'): '1',
    ('b', '1'): 'a',
    ('1', '1'): '1'
}

start1 = 'a'
accept1 = {'1'}

# Test some strings
strings1 = ["101", "010", "0101", "1001", "0110", "0011"]
for s in strings1:
    print(s, "=>", "ACCEPTED" if run_dfa(transitions1, start1, accept1, s) else "REJECTED")
