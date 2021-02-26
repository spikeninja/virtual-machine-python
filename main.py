import sys


class VM:
    def __init__(self):
        self._stack = []
        self.operations = {
            "OP_EOP": '00',
            "OP_PUSH": '01',
            "OP_POP": '02',
            "OP_PRINT": '03',
            "OP_ADD": '04',
        }
        self.do = {
            "OP_EOP": lambda x: print('EOP'),
            "OP_PUSH": lambda x,e: x.push(e),
            "OP_POP": lambda x: x._stack.pop(),
            "OP_PRINT": lambda x: print('print'),
            "OP_ADD": lambda x: x._stack.append(x._stack.pop() + x._stack.pop()),
        }

    def pop(self):
        return self._stack.pop(0)

    def push(self, element):
        self._stack.append(int(element))

    def perform_actions(self, instructions):
        n = len(instructions)
        i = 0
        flag = 1
        while flag and i < n:
            ins = instructions[i]
            if ins == self.operations["OP_EOP"]:
                flag = 0
            elif ins == self.operations["OP_PRINT"]:
                print("Stack: ",self._stack)
            elif ins == self.operations["OP_PUSH"]:
                self.do["OP_PUSH"](self, instructions[i+1])
            elif ins == self.operations["OP_POP"]:
                self.do["OP_POP"](self)
            elif ins == self.operations["OP_ADD"]:
                self.do["OP_ADD"](self)
            i += 1



def load_bytecode(filepath):
    with open(filepath) as f:
        ops = f.read().replace("/n", " ").split()
    return ops


def main(argv):
    vm = VM()
    bytecode = load_bytecode(argv[1])
    vm.perform_actions(bytecode)



if __name__ == '__main__':
    main(sys.argv)
