#!/usr/bin/env python3
"""
Rename section IDs: E001~E004, S071D~S071O, S072~S075
Update all file contents and rename files.
"""
import os, re, sys, glob
sys.stdout.reconfigure(encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Rename map (old ID → new ID) ─────────────────────────────────────────
RENAME_MAP = {
    'E001': 'S069',
    'E002': 'S079',
    'E003': 'S080',
    'E004': 'S081',
    'S071D': 'S072',
    'S071E': 'S072A',
    'S071F': 'S072B',
    'S071G': 'S072C',
    'S071H': 'S073',
    'S071I': 'S073A',
    'S071J': 'S073B',
    'S071K': 'S073C',
    'S071L': 'S074',
    'S071M': 'S074A',
    'S071N': 'S074B',
    'S071O': 'S074C',
    'S072':  'S075',
    'S073A': 'S076A',
    'S073':  'S076',
    'S074':  'S077',
    'S075':  'S078',
}

# Build single-pass regex (longer keys first to avoid prefix issues)
sorted_keys = sorted(RENAME_MAP, key=len, reverse=True)
PATTERN = re.compile(r'\b(' + '|'.join(re.escape(k) for k in sorted_keys) + r')\b')

def apply_rename(text):
    return PATTERN.sub(lambda m: RENAME_MAP[m.group(0)], text)

# ── Files that need content updates ───────────────────────────────────────
content_files = (
    glob.glob(os.path.join(BASE, '03_sections', '*.md')) +
    glob.glob(os.path.join(BASE, '01_outline', '*.md')) +
    [os.path.join(BASE, '01_outline', 'story_structure_overview.html'),
     os.path.join(BASE, '00_project', 'illustration_spec.md')]
)

print('─ Step 1: Update file contents ─')
updated = 0
for fp in sorted(content_files):
    with open(fp, encoding='utf-8') as f:
        original = f.read()
    new = apply_rename(original)
    if new != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f'  updated: {os.path.relpath(fp, BASE)}')
        updated += 1
    else:
        # Check if this file has any old IDs at all (sanity)
        pass
print(f'  {updated} files updated\n')

# ── File rename map (old filename prefix → new prefix) ────────────────────
# Format: (old_id, old_suffix, new_id)
FILE_RENAMES = [
    # Step 1: rename files whose target names are already free (E-series, S071X)
    ('E001', 'returned_alone',                  'S069'),
    ('E002', 'boy_who_found_his_name',           'S079'),
    ('E003', 'world_where_starlight_remains',    'S080'),
    ('E004', 'staying_in_the_twilight',          'S081'),
    # Step 2: rename S07X that would conflict — free up targets first
    # Order: S075→S078, S074→S077, S073A→S076A, S073→S076, S072→S075
    ('S075', 'starlight_crack',                  'S078'),
    ('S074', 'last_choice',                      'S077'),
    ('S073A','handing_empty_name_tag',           'S076A'),
    ('S073', 'ian_speaks',                       'S076'),
    ('S072', 'empty_name_tag',                   'S075'),
    # Step 3: rename S071X files (targets now free)
    ('S071D','first_memory_walked_together',     'S072'),
    ('S071E','first_fragment_melts',             'S072A'),
    ('S071F','too_easy_resentment',              'S072B'),
    ('S071G','misread_loneliness',               'S072C'),
    ('S071H','second_memory_market_step_back',   'S073'),
    ('S071I','second_fragment_trembles',         'S073A'),
    ('S071J','cold_question',                    'S073B'),
    ('S071K','lost_letter',                      'S073C'),
    ('S071L','third_memory_returned_companion',  'S074'),
    ('S071M','third_fragment_opens',             'S074A'),
    ('S071N','blocking_view',                    'S074B'),
    ('S071O','see_it_yourself',                  'S074C'),
]

print('─ Step 2: Rename files ─')
sections_dir = os.path.join(BASE, '03_sections')
renamed = 0
errors = 0
for old_id, suffix, new_id in FILE_RENAMES:
    old_name = f'{old_id}_{suffix}.md'
    new_name = f'{new_id}_{suffix}.md'
    old_path = os.path.join(sections_dir, old_name)
    new_path = os.path.join(sections_dir, new_name)
    if not os.path.exists(old_path):
        print(f'  MISSING: {old_name}')
        errors += 1
        continue
    if os.path.exists(new_path):
        print(f'  CONFLICT: {new_name} already exists')
        errors += 1
        continue
    os.rename(old_path, new_path)
    print(f'  {old_name} → {new_name}')
    renamed += 1

print(f'\n  {renamed} files renamed, {errors} errors\n')

# ── Verify: check that no old IDs remain in 03_sections ──────────────────
print('─ Step 3: Verification ─')
remaining = []
for fp in glob.glob(os.path.join(sections_dir, '*.md')):
    with open(fp, encoding='utf-8') as f:
        t = f.read()
    hits = PATTERN.findall(t)
    if hits:
        remaining.append((os.path.basename(fp), sorted(set(hits))))

if remaining:
    print('  WARNING — old IDs still found:')
    for fname, ids in remaining:
        print(f'    {fname}: {ids}')
else:
    print('  OK — no old IDs remain in 03_sections/')

# Check old filenames still exist
old_ids_in_filenames = [f for f in os.listdir(sections_dir)
                        if re.match(r'(E00[1-4]|S071[D-O])_', f)]
if old_ids_in_filenames:
    print(f'  WARNING — old filenames still exist: {old_ids_in_filenames}')
else:
    print('  OK — no old-ID filenames remain')

print('\nDone.')
