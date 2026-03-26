# This code allows you to store information on people owing you money
# and then list all those people in a ordered and formatted way in the terminal.
# Try to improve the `payday` function by splitting the logic into smaller functions.

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Debtor:
    """Stores the information on a person owing us money"""
    name: str
    debt: float

def payday(debtors: Iterable[Debtor]) -> None:
    ordered_debtors = _sort_debtors(debtors)
    _print_deptors(ordered_debtors)

def _sort_debtors(debtors: Iterable[Debtor]) -> Iterable[Debtor]:
    return reversed(sorted(debtors, key=lambda debtor: debtor.debt))

def _print_deptors(debtors: Iterable[Debtor]) -> None:
    for debtor in debtors:
        if debtor.debt > 100.0:
            print(f"{debtor.name}: !!!{debtor.debt}!!!")
        else:
            print(f"{debtor.name}: {debtor.debt}")

if __name__ == "__main__":
    payday([
        Debtor("Person1", 100.0),
        Debtor("Person2", 200.0),
        Debtor("Person3", 10.0),
        Debtor("Person4", 50.0),
        Debtor("Person5", 1250.0)
    ])
