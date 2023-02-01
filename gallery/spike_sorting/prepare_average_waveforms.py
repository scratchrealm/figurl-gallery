import numpy as np
import kachery_cloud as kcl

a = kcl.load_json('sha1://1b6d2442d6753724770fb47ac898d79083811545')
b = a['averageWaveforms']
b2 = np.array(b)[[4, 6, 8, 9, 15, 19, 20, 21, 24, 29, 31, 41, 44, 48, 57, 58, 59, 64, 65, 75]].tolist()
a2 = {**a, 'averageWaveforms': b2}
dd = kcl.store_json(a2)
uri = f'https://figurl.org/f?v=gs://figurl/figneuro-1&d={dd}&label=Average%20waveforms'

print(uri)