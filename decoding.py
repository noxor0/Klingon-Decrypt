import emission
import transition

#obs
words = ('rojHom', 'neH', "ja'chuqmeH", "pa'Daq", "tera'ngan", 'ghah', 'puq',
          "'e", "'eg", 'taH', 'qIp')
#states
pos = ('<s>', 'CONJ', 'V', 'PRO', 'N')
# start_p = ('<s>' : 1.0)
emm_tbl = emission.get_emissions()
trans_tbl = transition.get_transitions()

for key in emm_tbl.keys():
    print key, emm_tbl[key], '\n'

print '------------------------'

for key in trans_tbl.keys():
    print key, trans_tbl[key], '\n'
