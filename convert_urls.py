

# 1- getting all citekeys
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import convert_to_unicode

bibtex = '../perrinet_curriculum-vitae_tex/LaurentPerrinet.bib'
keys = []
# Load BibTeX file for parsing.
with open(bibtex, 'r', encoding='utf-8') as bibtex_file:
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(bibtex_file, parser=parser)
    for entry in bib_database.entries:
        #parse_bibtex_entry(entry, pub_dir=pub_dir, featured=featured, overwrite=overwrite, normalize=normalize)
        keys.append(entry['ID'])


# keys = ["Perrinet04tauc", "Adams12", "Perrinet05ecvp", "Perrinet05icann", "Barthelemy07", "Perrinet06", "Bogadhi10", "Perrinet06ciotat", "Bogadhi10vss", "Perrinet06cns", "Boutin18hots", "Perrinet06fab", "BoutinFranciosiniPerrinet18", "Perrinet06fens", "BoutinFranciosiniRuffierPerrinet18itwist", "Perrinet06neurocomp", "BoutinRuffierPerrinet17neurofrance", "Perrinet07cns", "BoutinRuffierPerrinet17spars", "Perrinet07neurocomp", "Cessac07", "Perrinet07nips", "Chemla18", "Perrinet08areadne", "CristobalPerrinetKeil15bicv", "Perrinet08areadne\(2f\)ToDo", "CristobalPerrinetKeil15bicv\(3d\)", "Perrinet08cosyne_learning", "CristobalPerrinetKeil15bicv_chap1", "Perrinet08cosyne_motion", "Damasse14gdr", "Perrinet08spie", "Damasse15gdr", "Perrinet08spie\(2f\)ToDo", "Damasse15vss", "Perrinet08vss", "Damasse16ecvp", "Perrinet09cns", "Damasse16vss", "Perrinet09cosyne", "Damasse17vss", "Perrinet09neurocomp", "Damasse18", "Perrinet09vss", "Danion15sfn", "Perrinet10DocSciences", "Dauc\(c3a9\)10", "Perrinet10areadne", "Davison07cns", "Perrinet10facets", "Davison08", "Perrinet10shl", "DupeyrouxBoutinSerresPerrinetViollet18", "Perrinet11interstices", "Fischer05", "Perrinet11nips", "Fischer07", "Perrinet11sfn", "Fischer07cv", "Perrinet12areadne", "Fleuriet11", "Perrinet12pred", "FranciosiniPerrinet18cs", "Perrinet13cns", "Friston12", "Perrinet13jffos", "Kaplan13", "Perrinet14", "Kaplan14beijing", "Perrinet14hdr", "KaplanKhoei14", "Perrinet14vss", "Khoei10tauc", "Perrinet15bicv", "Khoei11cns", "Perrinet15eusipco", "Khoei11ecvp", "Perrinet16EUVIP", "Khoei11sdn", "Perrinet16networks", "Khoei12sfn", "Perrinet17gdr", "Khoei13cns", "Perrinet18gdr", "Khoei13jpp", "Perrinet19PP", "Khoei14thesis", "Perrinet99", "Khoei14vss", "PerrinetAdamsFriston14", "KhoeiMassonPerrinet16", "PerrinetBednar15", "KhoeiMassonPerrinet17", "PerrinetBednar15\(2f\)Fr", "KhoeiMassonPerrinet17\(2f\)En", "PerrinetXXhdr", "Kremkow07cns", "PerrinetXXinterstices", "Kremkow08gns", "PerrinetXXpynn", "Kremkow08neurocomp", "PerrinetXXshl\(2f\)ToDo", "Kremkow08sfn", "Ravello18", "Kremkow09cns", "Ravello19droplets", "Kremkow09cnstalk", "Rudiger14cosyne", "Kremkow09gns", "Sanz12", "Kremkow09thesis", "Simoncini10vss", "Kremkow10jcns", "Simoncini11ecem", "Kremkow16", "Simoncini12", "LadretPerrinet18gdr", "Simoncini12Pattern", "Mansour16ecvp", "Simoncini12coding", "Mansour16gdr", "Simoncini12vss", "Mansour16sfn", "Simoncini13vss", "Mansour17ecvp", "Simoncini14vss", "Mansour17gdr", "Taouali14areadne", "Mansour18vss", "Taouali14neurocomp", "Masmoudi10", "Taouali15", "Masson10", "Taouali15icmns", "Masson12", "Taouali15vss", "Masson12areadne", "Taouali16areadne", "Meso13vss", "Vacher14ihp", "Meso14vss", "Vacher15icms", "Montagnini07", "Vacher15nips", "Montagnini15bicv", "Vacher16", "Montagnini15sfn", "Vacher18", "Montagnini16ecvp", "Voges08fens", "Nava13", "Voges08neurocomp", "Pasturel17gdr", "Voges09cns", "Pasturel18", "Voges09cosyne", "Pasturel18anemo", "Voges09gns", "Pasturel18grenoble", "Voges10neurocomp", "Perrinet01", "Voges11bccn", "Perrinet02esann", "Voges12", "Perrinet02sparse", "Wohrer06", "Perrinet02stdp", "Yger09gns", "Perrinet03", "Perrinet03ieee", "Perrinet03thesis", "Perrinet04nc"
# ]

# 2- making a dictionary to slugify

# from https://github.com/sourcethemes/academic-admin/blob/master/academic/cli.py#L177
import re
def slugify(s, lower=True):
    bad_symbols = ('.', '_', ':')  # Symbols to replace with hyphen delimiter.
    delimiter = '-'
    good_symbols = (delimiter,)  # Symbols to keep.
    for r in bad_symbols:
        s = s.replace(r, delimiter)

    s = re.sub(r'(\D+)(\d+)', r'\1\-\2', s)  # Delimit non-number, number.
    s = re.sub(r'(\d+)(\D+)', r'\1\-\2', s)  # Delimit number, non-number.
    s = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r'\-\1', s)  # Delimit camelcase.
    s = ''.join(c for c in s if c.isalnum() or c in good_symbols).strip()  # Strip non-alphanumeric and non-hyphen.
    s = re.sub('\-+', '-', s)  # Remove consecutive hyphens.

    if lower:
        s = s.lower()
    return s


dico = {}
for key in keys:
    dico[slugify(key)] = key

# print('dico', dico)


# 3- generating all conversion strings

import glob

for filename in glob.glob('content/publication/*'):
    # print("filename", filename)
    new_key = filename.split('content/publication/')[-1]
    if not new_key in ['___template___',  'person-re-id', '_index.md']:
        old_key = dico[new_key]
        input = 'https://invibe.net/LaurentPerrinet/Publications/' + old_key
        output = 'https://laurentperrinet.github.io/publication/' + new_key
        print('input', input, ' -> output', output)

# 4- replacing strings in a file

def inplace_change(filename, old_string, new_string, verbose=True):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            if verbose: print ('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        if verbose: print( 'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)

# https://stackoverflow.com/a/17548459/234547
inplace_change('content/publication/damasse-16-ecvp/cite.bib', 'https://laurentperrinet.github.io/publication/damasse-16-ecvp', 'https://laurentperrinet.github.io/publication/damasse-16-ecvp')

# 5- replacing all pairs of strings in all file
import os
for filename in glob.glob('**', recursive=True):
    ext = filename.split('.')[-1].lower()
    if os.path.isfile(filename) and ext not in ['jpg', 'png', 'gif', 'mp4']:
        print("Processing filename", filename)
        for filename_ in glob.glob('content/publication/*'):
            # print("filename", filename)
            new_key = filename_.split('content/publication/')[-1]
            if not new_key in ['___template___',  'person-re-id', '_index.md']:
                old_key = dico[new_key]
                input = 'https://invibe.net/LaurentPerrinet/Publications/' + old_key
                output = 'https://laurentperrinet.github.io/publication/' + new_key
                #print('input', input, ' -> output', output)
                inplace_change(filename, input, output, verbose=False)
