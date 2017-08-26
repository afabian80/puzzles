# Given a word, decide if it can be typed on a T9 keyboard
# by only jumping like a chess knight.
# For example: pay -> valid
#              fax -> invalid

paths = {
    2: [7,9],
    3: [4,8],
    4: [3,9],
    5: [],
    6: [7],
    7: [2,6],
    8: [3],
    9: [2,4],
} #  graph: 6 <--> 7 <--> 2 <--> 9 <--> 4 <--> 3 <--> 8
# some optimizations would be possible

letters = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}

def letter_to_num(letter):
    for k,v in letters.iteritems():
        if letter in v:
            return k
    else:
        return 0 # an invalid number

def path(letter_from,letter_to):
    num_from = letter_to_num(letter_from)
    num_to   = letter_to_num(letter_to)
    return num_to in paths[num_from]

def valid(word):
    res = True
    for i in range(len(word)-1):
        if not path(word[i], word[i+1]):
            res = False
            break
    return res

if __name__ == '__main__':
    print 'running'
    print valid('pay')
    print valid('fax')
    print valid('axifud')
