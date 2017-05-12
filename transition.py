tag_count = {}
bigrams = {}
transitions = {}

def add_prob_value(the_bigram):
    the_bigram_split = the_bigram.split(',')
    prev_pos = the_bigram_split[0]
    curr_pos = the_bigram_split[1]
    if prev_pos not in transitions:
        transitions[prev_pos] = {'N':.1, 'V':.1, 'CONJ' : .1, 'PRO' : .1, '</s>' : .1}
    denom = float(tag_count[prev_pos] + float(len(tag_count.keys()) * .1))
    transitions[prev_pos][curr_pos] = float(bigrams[the_bigram] + .1)/denom

def add_tag_count(the_pos):
    the_pos = the_pos.rstrip('\n')
    if the_pos in tag_count:
        tag_count[the_pos] += 1
    else:
        tag_count[the_pos] = 1

def add_bigram_count(tag_one, tag_two):
    tag_one = tag_one.rstrip('\n')
    tag_two = tag_two.rstrip('\n')
    tag_bigram = tag_one + ',' + tag_two
    if tag_bigram in bigrams:
        bigrams[tag_bigram] += 1
    else:
        bigrams[tag_bigram] = 1

def get_transitions():
    with open('Training_Fixed.txt', 'r') as train_file:
        for line in train_file:
            prev_pos = '<s>'
            add_tag_count('<s>')
            for word_pos in line.split(' '):
                word_pos_split = word_pos.split('/')
                curr_pos = word_pos_split[1]
                add_bigram_count(prev_pos, curr_pos)
                add_tag_count(curr_pos)
                prev_pos = curr_pos
            add_bigram_count(prev_pos, '</s>')

        for bigram in bigrams:
            add_prob_value(bigram)

        return transitions
