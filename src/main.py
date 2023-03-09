import argparse

class Interpreter:
    def init(self, source: str) -> None:
        self.source = source.upper()
        self.array = [0]
        self.position = 0

    def str(self) -> str:
        return self.array.str()

    def repr(self) -> str:
        return self.array.str()

    def get_value(self) -> int:
        return self.array[self.position]

    def increment(self) -> None:
        self.array[self.position] += 1

    def decrement(self) -> None:
        self.array[self.position] -= 1

    def forward(self) -> None:
        self.position += 1
        if len(self.array) == self.position:
            self.array.append(0)

    def back(self) -> None:
        if self.position == 0:
            self.array = [0] + self.array
        else:
            self.position -= 1

    def input(self) -> None:
        while True:
            c = input()
            if len(c) == 1:
                break
            print('Input non valido')
        self.array[self.position] = ord(c)

    def output(self) -> None:
        print(chr(self.array[self.position]), end='')

    def run(self) -> None:
        comandi = {
            'CANE': self.increment,
            'BESTIA': self.decrement,
            'PORCO': self.forward,
            'NEGRO': self.back,
            'BASTARDO': self.input,
            'STRONZO': self.output,
        }
        c = 0
        tokens = self.source.split('DIO ')
        keys = comandi.keys()
        maledetti: list[int] = []
        while c < len(tokens):
            if tokens[c].startswith('MALEDETTO'):
                if self.get_value() == 0:
                    n = 1
                    while n != 0:
                        c += 1
                        if tokens[c].startswith('MALEDETTO'):
                            n += 1
                        elif tokens[c].startswith('BOIA'):
                            n -= 1
                else:
                    maledetti.append(c)
            elif tokens[c].startswith('BOIA'):
                c = maledetti.pop() - 1
            else:
                for key in keys:
                    if tokens[c].startswith(key):
                        comandi[key]()
                        break
            c += 1

def main() -> None:
    argument_parser = argparse.ArgumentParser(
                                                description= "A programming language for intellectuals.",
                                                epilog= ""
                                             )
    argument_parser.add_argument('file', help = 'File to be interpreted')
    args = argument_parser.parse_args()
    with open(args.file, 'r') as file:
        source = '\n'.join(file.readlines())
    interpreter = Interpreter(source)
    interpreter.run()

if __name__ == '__main__':
    main()
