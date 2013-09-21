#!/usr/bin/env python
import argparse
import sys

def purify_source(s):
    allowed = ['0+', '0++', '0-', '0--', '0?', '0.', '0,', '0/', '/0', '0;']
    s = s.replace('\n', ' ').replace('\t', ' ')
    arr = s.split(' ')
    return list([ins for ins in arr if ins in allowed])

if __name__ == '__main__':
    arg = argparse.ArgumentParser(description='Zero language interpreter')
    arg.add_argument('source', action='store')
    ns = arg.parse_args()
    with open(ns.source, 'r') as ns:
        s = ns.read()
    ins = purify_source(s)

    class Program:
        def __init__(self):
            self.memory = [0,]
            self.position = 0
            self.loops = list()
            self.loop_ended = False
            self.ins = 0

        def __inc_pos(self):
            self.ins = self.ins + 1

        def incp(self):
            if self.loop_ended:
                self.__inc_pos()
                return
            self.position = self.position + 1
            if len(self.memory) == self.position:
                self.memory.append(0)
            self.__inc_pos()

        def decp(self):
            if self.loop_ended:
                self.__inc_pos()
                return
            if self.position > 0:
                self.position = self.position - 1
            self.__inc_pos()

        def incv(self):
            if self.loop_ended:
                self.__inc_pos()
                return
            self.memory[self.position] = self.memory[self.position] + 1
            self.__inc_pos()

        def decv(self):
            if self.loop_ended:
                self.__inc_pos()
                return
            self.memory[self.position] = self.memory[self.position] - 1
            self.__inc_pos()

        def loop_start(self):
            if self.loop_ended:
                self.__inc_pos()
                return
            if self.memory[self.position] == 0:
                self.loops.remove(self.ins)
                self.loop_ended = True
                self.__inc_pos()
                return
            self.loops.append(self.ins)
            self.__inc_pos()

        def loop_end(self):
            if self.loop_ended:
                self.loop_ended = False
                self.__inc_pos()
                return
            self.ins = self.loops[-1]

        def print_ascii(self):
            c = self.memory[self.position]
            if c >= 0 and c < 128:
                sys.stdout.write(chr(c))
                self.__inc_pos()
            else:
                sys.stderr.write('Wrong ascii value at memory cell %d\n' % self.position)
                sys.exit(1)

        def print_int(self):
            if self.loop_ended:
                self.__inc_pos()
                return
            sys.stdout.write('%d' % self.memory(self.position))
            self.__inc_pos()

        def read_ascii(self):
            x = raw_input()
            self.memory[self.position] = ord(x)
            self.__inc_pos()

        def read_int(self):
            x = raw_input()
            self.memory[self.position] = int(x)
            self.__inc_pos()

    prog = Program()

    instructions = {
        '0+': prog.incp,
        '0-': prog.decp,
        '0++': prog.incv,
        '0--': prog.decv,
        '0.': prog.print_ascii,
        '0,': prog.print_int,
        '0/': prog.loop_start,
        '/0': prog.loop_end,
        '0?': prog.read_ascii,
        '0;': prog.read_int,
    }

    ins_count = len(ins)
    while prog.ins < ins_count: # lol :X
        instructions[ins[prog.ins]]()
    sys.exit(0)


