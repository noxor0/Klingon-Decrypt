tag_count = {}
word_count = {}
word_pos_count = {}
emissions = {}

# def add_emission(the_bigram):
#     the_bigram_split = the_bigram.split('/')
#     the_word = the_bigram_split[0]
#     the_pos = the_bigram_split[1]
#     if the_word not in emissions:
#         emissions[the_word] = {'N':.1, 'V':.1, 'CONJ' : .1, 'PRO' : .1}
#
#     denom = float(tag_count[the_pos]) + (len(tag_count.keys()) * .1)
#     emissions[the_word][the_pos] = float(word_pos_count[the_bigram] + .1)/denom

def add_emission(the_bigram):
    the_bigram_split = the_bigram.split('/')
    the_word = the_bigram_split[0]
    the_pos = the_bigram_split[1]
    if the_pos not in emissions:
        emissions[the_pos] = {'rojHom': .1, 'neH': .1, "ja'chuqmeH": .1,
        "pa'Daq": .1, "tera'ngan": .1, 'ghah': .1, 'puq': .1, "'e": .1,
        "'eg": .1, 'taH': .1, 'qIp': .1}

    denom = float(tag_count[the_pos]) + (len(tag_count.keys()) * .1)
    emissions[the_pos][the_word] = float(word_pos_count[the_bigram] + .1)/denom

def add_tag_count(the_pos):
    the_pos = the_pos.rstrip('\n')
    if the_pos in tag_count:
        tag_count[the_pos] += 1
    else:
        tag_count[the_pos] = 1

def add_word_count(the_word):
    the_word = the_word.rstrip('\n')
    if the_word in word_count:
        word_count[the_word] += 1
    else:
        word_count[the_word] = 1

def add_word_pos_count(word_pos):
    word_pos = word_pos.rstrip('\n')
    if word_pos in word_pos_count:
        word_pos_count[word_pos] += 1
    else:
        word_pos_count[word_pos] = 1

def get_emissions():
    with open('Training_Fixed.txt', 'r') as train_file:
        for line in train_file:
            for word_pos in line.split(' '):
                word_pos_split = word_pos.split('/')
                word = word_pos_split[0]
                pos = word_pos_split[1]

                add_tag_count(pos)
                add_word_count(word)
                add_word_pos_count(word_pos)

        for word_pos in word_pos_count:
            add_emission(word_pos)

    return emissions
