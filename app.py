from fire import Fire
from  math import factorial as fact
import re

def binomial_coef(k, n):
    return fact(n) / (fact(k) * fact(n-k))


def hypergeometric_dist(k, n, K, N):
    # {\displaystyle p_{X}(k)=\Pr(X=k)={\frac {{\binom {K}{k}}{\binom {N-K}{n-k}}}{\binom {N}{n}}},}
    # {\displaystyle N}N is the population size,
    # {\displaystyle K}K is the number of success states in the population,
    # {\displaystyle n}n is the number of draws (i.e. quantity drawn in each trial),
    # {\displaystyle k}k is the number of observed successes,
    # {\textstyle \textstyle {a \choose b}}{\textstyle \textstyle {a \choose b}} is a binomial coefficient.

    return binomial_coef(k, K) * binomial_coef(n-k, N-K) / binomial_coef(n, N)


class Calculator:
    def __init__(self, deck_file="deck.txt"):
        self.deck_list = []
        self.deck_quantities = []
        self.hand_size = 7

        # Parse deck list from file
        with open(deck_file, "r") as deck:
            for line in deck:
                if "Sideboard" in line:
                    break

                m = re.match(r"(\d+) (.+)\(", line)
                if m:
                    self.deck_list.append(m.group(2))
                    self.deck_quantities.append(int(m.group(1)))

        self.show(self.hand_size)


    @property
    def deck_size(self):
        return sum(self.deck_quantities)


    def show(self, draw_size):
        # header
        print(f"{' ':3} {' ':40} {'Qty':<5s}  " + " ".join([f"{n}+{' ':8}" for n in range(1, draw_size+1)]))

        for idx, (c, q) in enumerate(zip(self.deck_list, self.deck_quantities)):
            print(f"{idx:3} {c:40} {q:<5d}  " + " ".join(["%.5f   " % self.draw_proba(i, q, draw_size) for i in range(q+1) if i>0 and i<=draw_size]))
        print(f"{'Total':44} {self.deck_size}")


    def draw_proba(self, number_wanted_card, total_card, draw_size):
        proba = 0
        for k in range(number_wanted_card, min(total_card, draw_size) + 1):
            proba += hypergeometric_dist(k, draw_size, total_card, self.deck_size)
        return proba

    def none(self):
        while self.deck_size > 0:
            try:
                idxs = map(int, input("indexes of drawn card : ").split())
                for idx in idxs:
                    self.deck_quantities[idx] -= 1
                self.show(1)
            except:
                return

if __name__ == "__main__":
    Fire(Calculator)

