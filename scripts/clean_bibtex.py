# normalize entries in the bibtex file
verbose = False
import calendar
import re
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
#from bibtexparser.bibdatabase import BibDatabase

for type in ['talks', 'publications']:#, 'Events']:
    bibtex = f'../../perrinet_curriculum-vitae.tex/LaurentPerrinet_{type}.bib'
    keys = []
    # Load BibTeX file for parsing.
    with open(bibtex, 'r', encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=True)
        # no convert_to_unicode: the file is rewritten, and escapes such as \% must survive for the CV to compile
        # keep biblatex types such as @thesis, which would otherwise be silently dropped on rewrite
        parser.ignore_nonstandard_types = False
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        for entry in bib_database.entries:
            #parse_bibtex_entry(entry, pub_dir=pub_dir, featured=featured, overwrite=overwrite, normalize=normalize)
            for tag_key in ['projects', 'keywords']:
                if tag_key in entry.keys():
                    # extract tags and remove unwnated spaces
                    tags = entry[tag_key]
                    tags_old = tags
                    tags = tags.replace(';', ',')
                    tags = tags.replace(', ', ',')
                    tags = tags.replace(' ,', ',')
                    # sort tags
                    tags = sorted(list(set(tags.split(','))), key=str.lower)
                    # concatenate tags in one string
                    entry[tag_key] = ','.join(tags)
                    if not tags_old == tags:
                        if verbose:
                            print('before sorting ->"', tags_old, end='"')
                            print(' after sorting ->"', entry[tag_key], end='"\n')

            keys.append(entry['ID'])

    writer = BibTexWriter()
    writer.indent = '    '     # indent entries with 4 spaces instead of one
    #writer.order_entries_by = ('ID', 'year')
    text = writer.write(bib_database)
    # common_strings expands month macros (sep -> {September}); write them back as macros so biber can sort them
    text = re.sub(r'^(\s*month = )\{(' + '|'.join(calendar.month_name[1:]) + r')\}',
                  lambda m: m.group(1) + m.group(2)[:3].lower(), text, flags=re.M)
    with open(bibtex, 'w') as bibfile:
        bibfile.write(text)
