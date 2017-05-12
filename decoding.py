import emission
import transition

#obs
words = ('rojHom', 'neH', "ja'chuqmeH", "pa'Daq", "tera'ngan", 'ghah', 'puq',
          "'e", "'eg", 'taH', 'qIp')
#states
pos_list = ('CONJ', 'V', 'PRO', 'N')
emm_tbl = emission.get_emissions()
trans_tbl = transition.get_transitions()

prac_sent = "tera'ngan legh yaS"
prac_sent = prac_sent.split(' ')

prev_vals = {'<s>' : 1.0}
best_pos = []

print 'possible probs', prev_vals, 'max: ', max(prev_vals, key=prev_vals.get)
for word in prac_sent:
    prev_max = max(prev_vals, key=prev_vals.get)
    prev_max_val = prev_vals[prev_max]
    prev_vals.clear()
    for curr_pos in pos_list:
        if word not in emm_tbl[curr_pos]:
            emm_tbl[curr_pos][word] = .1
        curr_prob = prev_max_val * emm_tbl[curr_pos][word] * trans_tbl[prev_max][curr_pos]
        # print word, curr_pos, curr_prob
        prev_vals[curr_pos] = curr_prob

    best_pos.append(max(prev_vals, key=prev_vals.get))
    # print 'possible probs', prev_vals, 'max: ', max(prev_vals, key=prev_vals.get)



print best_pos

# print 'emmission table'
# for key in emm_tbl.keys():
#     print key, emm_tbl[key]
#
# print '------------------------'
#
# print 'transition table'
# for key in trans_tbl.keys():
#     print key, trans_tbl[key]
