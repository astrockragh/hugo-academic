"""Downsample precomputed spectra binary and optionally strip zero arrays.

Input binary layout:  [wavelength: N_OLD] + N_SPEC × 4 × N_OLD floats
  per spectrum: [intensity_b, intensity_c, dT_intensity_b, dT_intensity_c]

If --strip-zero is given (or STRIP_ZERO = True), arrays that are all-zero
across every spectrum (e.g. c-type arrays for C2v) are dropped, and
n_arrays is written to the output index so the viewer knows the format.
"""
import numpy as np, json, os, sys

# ── Configuration ────────────────────────────────────────────────────────
INPUT_BIN    = '../../raw_data/mol_spectra_data_C2v_big.bin'
INPUT_INDEX  = 'mol_spectra_index_Cs_big.json'
OUTPUT_BIN   = 'mol_spectra_data_C2v_1000.bin'
OUTPUT_INDEX = 'mol_spectra_index_C2v_1000.json'
STEP         = 2          # downsample factor
STRIP_ZERO   = True       # drop arrays that are all-zero across all spectra
ARRAYS_IN    = 4          # arrays per spectrum in the input file

# ── Load ─────────────────────────────────────────────────────────────────
idx   = json.load(open(INPUT_INDEX))
N_OLD = idx['n_wav']
N_NEW = N_OLD // STEP
N_SPEC = idx['n_spectra']

raw = np.fromfile(INPUT_BIN, dtype=np.float32)
print(f'Loaded {len(raw)} floats: {N_OLD} wav + {N_SPEC} spectra × {ARRAYS_IN} arrays')

# ── Detect which arrays are non-zero ─────────────────────────────────────
# Array order: 0=intensity_b, 1=intensity_c, 2=dT_b, 3=dT_c
keep = list(range(ARRAYS_IN))  # default: keep all

if STRIP_ZERO:
    array_names = ['intensity_b', 'intensity_c', 'dT_intensity_b', 'dT_intensity_c']
    keep = []
    for a in range(ARRAYS_IN):
        nonzero = False
        for k in range(N_SPEC):
            base = N_OLD + k * ARRAYS_IN * N_OLD
            chunk = raw[base + a * N_OLD : base + (a + 1) * N_OLD]
            if np.any(chunk != 0):
                nonzero = True
                break
        if nonzero:
            keep.append(a)
            print(f'  keeping array {a} ({array_names[a]})')
        else:
            print(f'  stripping array {a} ({array_names[a]}) — all zeros')

N_ARRAYS_OUT = len(keep)
print(f'Output: {N_ARRAYS_OUT} arrays per spectrum')

# ── Write downsampled binary ─────────────────────────────────────────────
with open(OUTPUT_BIN, 'wb') as f:
    # Wavelength array
    f.write(raw[:N_OLD][::STEP].tobytes())
    # Per-spectrum arrays (only the kept ones)
    for k in range(N_SPEC):
        base = N_OLD + k * ARRAYS_IN * N_OLD
        for a in keep:
            f.write(raw[base + a * N_OLD : base + (a + 1) * N_OLD][::STEP].tobytes())

# ── Write index ──────────────────────────────────────────────────────────
idx['n_wav']    = N_NEW
idx['n_arrays'] = N_ARRAYS_OUT  # 2 for C2v (b + dT_b), 4 for Cs
json.dump(idx, open(OUTPUT_INDEX, 'w'))

old_mb = os.path.getsize(INPUT_BIN) / 1e6
new_mb = os.path.getsize(OUTPUT_BIN) / 1e6
print(f'{old_mb:.1f} MB → {new_mb:.1f} MB  ({N_NEW} pts/spectrum, {N_ARRAYS_OUT} arrays)')
