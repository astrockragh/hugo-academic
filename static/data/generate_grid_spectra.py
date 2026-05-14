"""
Generate a grid of PGOPHER spectra and export JSON for the spectrum_viewer widget.

Usage:
  1. Set the grid values below to taste.
  2. Run this script (needs pgo binary, templates, numpy, scipy).
  3. Output: static/data/mol_spectra.json

Grid count with defaults below:
  4 T × 1 A × 4 b_fac × 4 c_fac × 3 fA × 3 fB × 3 fC × 3 lt × 2 sig = 15,552 param combos
  For Cs each combo → 4 PGO calls (2 axes × {T, T+dT}).
"""

import os, json, tempfile, subprocess
import numpy as np
from scipy.interpolate import interp1d

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION  — edit these
# ═══════════════════════════════════════════════════════════════════════════
PGO_BINARY = os.path.expanduser('~/DIB/./pgo')
pgo_available = os.path.isfile(PGO_BINARY)
if not pgo_available:
    raise RuntimeError('pgo binary not found at ' + PGO_BINARY)

inferred_sym = 'Cs'        # 'C2v' or 'Cs'
inferred_dib = '15272'

# Wavelength grid (Angstroms) — shared x-axis for all spectra
CENTER_WAV = 15272.27178113337
data_wavelength = np.linspace(CENTER_WAV - 6.5, CENTER_WAV + 6.5, 2000)
CENTRAL_INVCM_BASE = 1e8 / CENTER_WAV

PGO_TEMPLATES = {
    ('C2v', '15272'):      os.path.expanduser('~/DIB/pgo_files/asym_top_15272_C2v.pgo'),
    ('Cs',  '15272', 'a'): os.path.expanduser('~/DIB/pgo_files/asym_top_15272_Cs_a.pgo'),
    ('Cs',  '15272', 'b'): os.path.expanduser('~/DIB/pgo_files/asym_top_15272_Cs_b.pgo'),
}

TEMP_DIR = tempfile.mkdtemp(prefix='dib_grid_pgo_')
print(f'PGOPHER temp dir: {TEMP_DIR}')

# Output paths (relative to Hugo site root)
OUTPUT_DIR   = os.path.expanduser('~/hugo-academic/static/data')
OUTPUT_INDEX = os.path.join(OUTPUT_DIR, 'mol_spectra_index.json')
OUTPUT_BIN   = os.path.join(OUTPUT_DIR, 'mol_spectra_data.bin')

# ── Parameter grid ────────────────────────────────────────────────────────
GRID_T     = [5, 10, 20, 40]
GRID_A     = [0.04]
GRID_b_fac = [0.98, 0.5, 0.1, 0.05]   # B = A × b_fac
GRID_c_fac = [0.98, 0.5, 0.1, 0.05]   # C = B × c_fac
GRID_fA    = [1.0, 0.98, 0.92]
GRID_fB    = [1.0, 0.98, 0.92]
GRID_fC    = [1.0, 0.98, 0.92]
GRID_lt    = [0.01]                    # Lorentz τ applied online in widget; keep minimal here
GRID_sig   = [0.01]                    # Gaussian σ applied online in widget; keep minimal here

# dT step for finite-difference derivative
DT_STEP = 0.05  # K

# ═══════════════════════════════════════════════════════════════════════════
# PGOPHER HELPERS  (unchanged from your code)
# ═══════════════════════════════════════════════════════════════════════════
def _fname_base(T, A, B, C, fA, fB, fC, lorentz=0.01, gaussian=0.3, axis='b', co=0.0):
    return (f'T{T:.4f}_A{A:.7f}_B{B:.7f}_C{C:.7f}_'
            f'FA{fA:.5f}_FB{fB:.5f}_FC{fC:.5f}_ax{axis}_lt{lorentz:.3f}_gauss{gaussian:.3f}_off{co:.2f}')


def _run_pgo(T, A, B, C, fA, fB, fC, lorentz, gaussian, axis, center_offset, template_key):
    """Template-substitute and run pgo; return path to spectrum text file."""
    PGO_TEMPLATE = PGO_TEMPLATES[template_key]
    A_g, B_g, C_g = A, B, C
    A_e, B_e, C_e = A * fA, B * fB, C * fC
    center = CENTRAL_INVCM_BASE + center_offset
    base = _fname_base(T, A, B, C, fA, fB, fC, lorentz, gaussian, axis, center_offset)
    pgo_file  = os.path.join(TEMP_DIR, f'tmp_{base}.pgo')
    spec_file = os.path.join(TEMP_DIR, f'spc_{base}.txt')

    sym = inferred_sym
    dib = inferred_dib

    if sym == 'C2v' and dib == '15272':
        awk_script = f"""
awk -v temp="{T}" -v A_ground="{A_g}" -v B_ground="{B_g}" -v C_ground="{C_g}" \\
    -v A_excited="{A_e}" -v B_excited="{B_e}" -v C_excited="{C_e}" \\
    -v axis="{axis}" -v lorentz_width="{lorentz}" -v gaussian_width="{gaussian}" '
BEGIN {{ in_ground=0; in_excited=0; }}
/<AsymmetricTop Name="v=0"/ {{ in_ground=1 }}
/<AsymmetricTop Name="v=1"/ {{ in_excited=1 }}
/<\\/AsymmetricTop>/ {{ in_ground=0; in_excited=0 }}
in_ground  && /<Parameter Name="A" Value=/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" A_ground "\\"") }}
in_ground  && /<Parameter Name="B" Value=/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" B_ground "\\"") }}
in_ground  && /<Parameter Name="C" Value=/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" C_ground "\\"") }}
in_excited && /<Parameter Name="A" Value=/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" A_excited "\\"") }}
in_excited && /<Parameter Name="B" Value=/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" B_excited "\\"") }}
in_excited && /<Parameter Name="C" Value=/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" C_excited "\\"") }}
/<CartesianTransitionMoment Bra="v=1" Ket="v=0"/ {{ sub(/Axis="[^"]+"/, "Axis=\\"" axis "\\"") }}
/<Parameter Name="Temperature" Value=/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" temp "\\"") }}
/<Parameter Name="Lorentzian" Value=/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" lorentz_width "\\"") }}
/<Parameter Name="Gaussian" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" gaussian_width "\\"") }}
{{ print }}
' {PGO_TEMPLATE} > {pgo_file}
"""
    else:
        awk_script = f"""
awk -v temp="{T}" -v A_ground="{A_g}" -v B_ground="{B_g}" -v C_ground="{C_g}" \\
    -v A_excited="{A_e}" -v B_excited="{B_e}" -v C_excited="{C_e}" \\
    -v lorentz_width="{lorentz}" -v gaussian_width="{gaussian}" -v center="{center}" '
BEGIN {{ inside_ground=0; inside_excited=0; }}
/<Parameter Name="Temperature" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" temp "\\"") }}
/<AsymmetricManifold Name="Ground"/ {{ inside_ground=1 }}
/<AsymmetricManifold Name="Excited"/ {{ inside_excited=1 }}
/<\\/AsymmetricManifold>/ {{ inside_ground=0; inside_excited=0 }}
inside_ground  && /<Parameter Name="A" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" A_ground "\\"") }}
inside_ground  && /<Parameter Name="B" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" B_ground "\\"") }}
inside_ground  && /<Parameter Name="C" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" C_ground "\\"") }}
inside_excited && /<Parameter Name="Origin" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" center "\\"") }}
inside_excited && /<Parameter Name="A" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" A_excited "\\"") }}
inside_excited && /<Parameter Name="B" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" B_excited "\\"") }}
inside_excited && /<Parameter Name="C" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" C_excited "\\"") }}
/<Parameter Name="Lorentzian" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" lorentz_width "\\"") }}
/<Parameter Name="Gaussian" Value="/ {{ sub(/Value="[0-9.eE+-]+"/, "Value=\\"" gaussian_width "\\"") }}
{{ print }}
' {PGO_TEMPLATE} > {pgo_file}
"""
    subprocess.run(awk_script, shell=True, check=True, executable='/bin/bash')
    subprocess.run([PGO_BINARY, '--plot', pgo_file, spec_file],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return spec_file


def get_pgopher_spectrum(spec_file):
    """Load a PGOPHER spectrum txt and interpolate to data_wavelength grid."""
    inv_cm, flux = np.loadtxt(spec_file).T
    wav_pgo = 1e8 / inv_cm
    out_i = interp1d(wav_pgo, flux, bounds_error=False, fill_value=np.nan)
    return out_i(data_wavelength)


# ═══════════════════════════════════════════════════════════════════════════
# GRID GENERATION
# ═══════════════════════════════════════════════════════════════════════════
from itertools import product

grid_axes = [GRID_T, GRID_A, GRID_b_fac, GRID_c_fac,
             GRID_fA, GRID_fB, GRID_fC, GRID_lt, GRID_sig]
total = 1
for g in grid_axes:
    total *= len(g)
print(f'Total grid points: {total}')

spectra_list = []
n_ok, n_fail = 0, 0

for idx, (T, A, b_fac, c_fac, fA, fB, fC, lt, sig) in enumerate(product(*grid_axes)):
    B = A * b_fac
    C = B * c_fac
    co = 0.0  # center offset always zero for the grid

    if (idx + 1) % 100 == 0 or idx == 0:
        print(f'  [{idx+1}/{total}]  T={T}  A={A}  B={B:.6f}  C={C:.6f}  '
              f'fA={fA}  fB={fB}  fC={fC}  lt={lt}  sig={sig}')

    try:
        if inferred_sym == 'C2v':
            tkey = ('C2v', inferred_dib)
            sf    = _run_pgo(T,           A, B, C, fA, fB, fC, lt, sig, 'a', co, tkey)
            sf_dT = _run_pgo(T + DT_STEP, A, B, C, fA, fB, fC, lt, sig, 'a', co, tkey)
            mf    = get_pgopher_spectrum(sf)
            mf_dT = get_pgopher_spectrum(sf_dT)

            # dT = finite-difference derivative spectrum
            entry = {
                'params': {
                    'T': T, 'A': A, 'B': B, 'C': C,
                    'fA': fA, 'fB': fB, 'fC': fC,
                    'tau': lt, 'sigma': sig,
                },
                'intensity_b':    mf.tolist(),
                'dT_intensity_b': (mf_dT - mf).tolist(),
            }

        else:  # Cs — two axes
            entry_data = {}
            for axis, key_suffix in [('a', 'b'), ('b', 'c')]:
                # a-axis pgo → b-type spectrum, b-axis pgo → c-type spectrum
                tkey  = ('Cs', inferred_dib, axis)
                sf    = _run_pgo(T,           A, B, C, fA, fB, fC, lt, sig, axis, co, tkey)
                sf_dT = _run_pgo(T + DT_STEP, A, B, C, fA, fB, fC, lt, sig, axis, co, tkey)
                mf    = get_pgopher_spectrum(sf)
                mf_dT = get_pgopher_spectrum(sf_dT)
                entry_data[f'intensity_{key_suffix}']    = mf.tolist()
                entry_data[f'dT_intensity_{key_suffix}'] = (mf_dT - mf).tolist()

            entry = {
                'params': {
                    'T': T, 'A': A, 'B': B, 'C': C,
                    'fA': fA, 'fB': fB, 'fC': fC,
                    'tau': lt, 'sigma': sig,
                },
                **entry_data,
            }

        spectra_list.append(entry)
        n_ok += 1

    except Exception as e:
        n_fail += 1
        print(f'  [{idx+1}/{total}]  FAILED: {e}')

print(f'\nDone: {n_ok} succeeded, {n_fail} failed out of {total}')

# ═══════════════════════════════════════════════════════════════════════════
# EXPORT — BINARY (.bin) + INDEX (.json)
# ═══════════════════════════════════════════════════════════════════════════
#
# Binary layout (all Float32, little-endian):
#   [wavelength: N floats] [spectrum_0: 4×N floats] [spectrum_1: 4×N floats] …
#
# Per-spectrum block order:
#   intensity_b | intensity_c | dT_intensity_b | dT_intensity_c
#
# Index JSON:
#   { "n_wav": N, "n_spectra": M, "spectra": [ {params dict}, … ] }
#
import struct

N_WAV = len(data_wavelength)
ARRAYS_PER_SPECTRUM = 4
ARRAY_KEYS = ['intensity_b', 'intensity_c', 'dT_intensity_b', 'dT_intensity_c']

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(OUTPUT_BIN, 'wb') as bf:
    # 1. Write wavelength array
    bf.write(np.array(data_wavelength, dtype=np.float32).tobytes())

    # 2. Write each spectrum's 4 arrays
    index_params = []
    for entry in spectra_list:
        index_params.append(entry['params'])
        for key in ARRAY_KEYS:
            arr = entry.get(key)
            if arr is not None:
                bf.write(np.array(arr, dtype=np.float32).tobytes())
            else:
                # Missing array (e.g. C2v has no intensity_c) → write zeros
                bf.write(np.zeros(N_WAV, dtype=np.float32).tobytes())

# 3. Write index JSON (small — just params, no spectra data)
index = {
    'n_wav':     N_WAV,
    'n_spectra': len(spectra_list),
    'spectra':   index_params,
}

with open(OUTPUT_INDEX, 'w') as f:
    json.dump(index, f)

bin_mb = os.path.getsize(OUTPUT_BIN) / 1e6
idx_kb = os.path.getsize(OUTPUT_INDEX) / 1e3
print(f'\nWrote {OUTPUT_BIN}  ({bin_mb:.1f} MB)')
print(f'Wrote {OUTPUT_INDEX}  ({idx_kb:.0f} KB)')
print(f'{len(spectra_list)} spectra × {N_WAV} wavelengths × 4 arrays')
print(f'Tip: gzip the .bin before deploying — '
      f'expected transfer size ~{bin_mb * 0.25:.0f} MB')
