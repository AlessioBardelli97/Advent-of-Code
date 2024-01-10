from sys import argv


type Tunnel = str


class Valve:
    def __init__(self, open: bool, flowRate: int, tunnels: list[Tunnel]) -> None:
        self.open = open
        self.flowRate = flowRate
        self.tunnels = tunnels
    def __repr__(self) -> str:
        return f"Valve(o={self.open}, fr={self.flowRate}, t={self.tunnels})"
    def copy(self) -> "Valve":
        return Valve(self.open, self.flowRate, self.tunnels)


class State:
    def __init__(self, tunnel: Tunnel, valves: dict[Tunnel, Valve], time: int, mostPressureRelease: int) -> None:
        self.tunnel = tunnel
        self.valves = valves
        self.time = time
        self.mostPressureRelease = mostPressureRelease
    def getOpen(self) -> bool:
        return self.valves[self.tunnel].open
    def setOpen(self):
        self.valves[self.tunnel].open = True
    def getTunnels(self) -> list[Tunnel]:
        return self.valves[self.tunnel].tunnels
    def getFlowRate(self) -> int:
        return self.valves[self.tunnel].flowRate
    def __repr__(self) -> str:
        return f"tu={self.tunnel}, v={self.valves}, ti={self.time}, m={self.mostPressureRelease}"
    def getActions(self):
        result: list[State] = []
        if not self.goal():
            if not self.getOpen() and self.getFlowRate() > 0:
                newState = State(\
                    self.tunnel,\
                    {valve: self.valves[valve].copy() for valve in self.valves},\
                    self.time + 1,\
                    self.mostPressureRelease + ((30 - self.time) * self.getFlowRate())\
                )
                newState.setOpen()
                result.append(newState)
            for tunnel in self.getTunnels():
                newState = State(tunnel, {valve: self.valves[valve].copy() for valve in self.valves}, self.time + 1, self.mostPressureRelease)
                result.append(newState)
        return result
    def goal(self) -> bool:
        return (self.time >= 30) or all(valve.open for valve in self.valves.values() if valve.flowRate > 0)
    def euristica1(self) -> int:
        """Si favoriscono gli stati che hanno il maggior numero di valvole aperte"""
        return sum([valve.open for valve in self.valves.values()])
    def euristica2(self) -> int:
        """Si favoriscono gli stato con la maggiore pressione rilasciata"""
        return self.mostPressureRelease
    def euristica3(self) -> int:
        """Si favoriscono gli stati dove la somma dei flow rate delle valvole ancora chiuse è maggiore"""
        return sum(valve.flowRate for valve in self.valves.values() if not valve.open)


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        valves: dict[Tunnel, Valve] = {}
        for line in file.read().split("\n"):
            line = line.replace("Valve ", "")\
              .replace(" has flow rate=", "/")\
              .replace("; tunnels lead to valves ", "/")\
              .split("/")
            valves[line[0]] = Valve(open=False, flowRate=int(line[1]), tunnels=line[2].split(", "))
        states = [State("AA", valves, 1, 0)]
    finalStates: int = 0
    while len(states) > 0:
        state = states.pop()
        if state.goal() and state.mostPressureRelease > finalStates:
            finalStates = state.mostPressureRelease
            print(finalStates)
        else:
            for newState in state.getActions():
                states.append(newState)
            sorted(states, key=lambda s: s.euristica3())
