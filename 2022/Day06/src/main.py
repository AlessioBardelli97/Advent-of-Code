from sys import argv


def start_of(signal: str, size: int) -> int:
    i, j, found = 0, size-1, False
    while j < len(signal) and not found:
        found = True
        for k in range(i, j):
            for w in range(k+1, j+1):
                if signal[k] == signal[w]:
                    found = False
        if not found:
            i += 1
            j += 1
    return j+1


def start_packet(signal: str) -> int:
    return start_of(signal, 4)
                    

def start_message(signal: str) -> int:
    return start_of(signal, 14)


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        signal = file.read()
        print("  Part One:", start_packet(signal))
        print("  Part Two:", start_message(signal))
