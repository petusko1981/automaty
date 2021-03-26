#!/usr/bin/env python3
# -*- coding: utf-8 -*-

testovacie_data = [
    {"win": 5, "cwin": 325, "count": 6},
    {"win": 5, "cwin": 0, "count": 6},
    {"win": 5, "cwin": 10, "count": 1},
    {"win": 5, "cwin": 0, "count": 1},
]

# metoda pre vypisanie jedneho riadku gamble
def print_step(step, start_bet, gamble_win):
    print("Gamble step: {} Bet: {} win: {}".format(
        step, start_bet, gamble_win))


# objekt pre vysledok s metodou pre vypisanie vysledku
class Result:
    def __init__(self, tbet, twin):
        self.tbet = tbet
        self.twin = twin

    def print_info(self):
        print("--------------------------------")
        print("Total Gamblebet {}, Total Gamblewin {}, zisk {} vyhernost % {}".format(
            self.tbet,
            self.twin,
            (self.twin - self.tbet),
            ((self.twin / self.tbet) * 100),
        ))
        print("#################################")


# objekt pre zadanie s metodou ktora vyrata vsetko
class Input:
    step = 1

    def __init__(self, win, cwin, count):
        self.win = win
        self.cwin = cwin
        self.count = count

    def calculate(self):
        # prazdny objekt ktory postupne naplnim
        result = Result(
            tbet=0,
            twin=0
        )

        start_bet = self.win

        if self.cwin > 0:
            while (self.step <= self.count):
                gamble_win = start_bet * 2

                print_step(self.step, start_bet, gamble_win)

                result.tbet += start_bet
                result.twin += gamble_win
                start_bet = gamble_win
                self.step += 1


        elif self.cwin == 0:

            while (self.step <= self.count):
                if self.step <= (self.count - 1):
                    gamble_win = start_bet * 2

                    print_step(self.step, start_bet, gamble_win)

                    result.tbet += start_bet
                    result.twin += gamble_win
                    start_bet = gamble_win
                    self.step += 1

                else:
                    gamble_win = 0
                    print_step(self.step, start_bet, gamble_win)

                    result.tbet += start_bet
                    result.twin += gamble_win
                    self.step += 1

        return result

def main():

    for t in testovacie_data:

        input = Input(
            win=t["win"],
            cwin=t["cwin"],
            count=t["count"],
        )

        # vyratat vysledok
        result = input.calculate()

        # zobrazit vysledok
        result.print_info()

if __name__ == "__main__":
    main()
