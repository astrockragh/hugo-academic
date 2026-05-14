"""Downsample the precomputed spectra binary from 2000 to 500 wavelength points."""
import numpy as np, json, os

INPUT_BIN   = '../../raw_data/mol_spectra_data_Cs_big.bin'
INPUT_INDEX = 'mol_spectra_index_Cs_big.json'  # index is small, stays in static/data
OUTPUT_BIN   = 'mol_spectra_data_Cs_1000.bin'
OUTPUT_INDEX = 'mol_spectra_index_Cs_1000.json'
STEP = 2  # 2000 / 4 = 500

idx = json.load(open(INPUT_INDEX))
N_OLD = idx['n_wav']
N_NEW = N_OLD // STEP
N_SPEC = idx['n_spectra']
ARRAYS_PER = 4

raw = np.fromfile(INPUT_BIN, dtype=np.float32)
print(f'Loaded {len(raw)} floats: {N_OLD} wav + {N_SPEC} spectra x {ARRAYS_PER} arrays')

with open(OUTPUT_BIN, 'wb') as f:
    # Downsample wavelength array
    f.write(raw[:N_OLD][::STEP].tobytes())
    # Downsample each spectrum's 4 arrays
    for k in range(N_SPEC):
        base = N_OLD + k * ARRAYS_PER * N_OLD
        for a in range(ARRAYS_PER):
            f.write(raw[base + a*N_OLD : base + (a+1)*N_OLD][::STEP].tobytes())

idx['n_wav'] = N_NEW
json.dump(idx, open(OUTPUT_INDEX, 'w'))

old_mb = os.path.getsize(INPUT_BIN) / 1e6
new_mb = os.path.getsize(OUTPUT_BIN) / 1e6
print(f'{old_mb:.1f} MB -> {new_mb:.1f} MB  ({N_NEW} pts/spectrum)')
