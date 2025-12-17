from dataclasses import dataclass

@dataclass
class Interazione:
    cromosoma1 : str
    cromosoma2 : str
    peso : float


    def __str__(self):
        return f"{self.cromosoma1} {self.cromosoma2} {self.peso}"

