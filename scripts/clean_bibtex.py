# normalize entries in the bibtex file
verbose = False
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
#from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import convert_to_unicode

for type in ['talks', 'publications']:#, 'Events']:
    bibtex = f'../../perrinet_curriculum-vitae_tex/LaurentPerrinet_{type}.bib'
    keys = []
    # Load BibTeX file for parsing.
    with open(bibtex, 'r', encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
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
    with open(bibtex, 'w') as bibfile:
        bibfile.write(writer.write(bib_database))
