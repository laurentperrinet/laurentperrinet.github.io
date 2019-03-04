
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
#from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import convert_to_unicode

for type in ['Presentations', 'Publications']:#, 'Events']:
    bibtex = f'../perrinet_curriculum-vitae_tex/LaurentPerrinet_{type}.bib'
    keys = []
    # Load BibTeX file for parsing.
    with open(bibtex, 'r', encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        for entry in bib_database.entries:
            #parse_bibtex_entry(entry, pub_dir=pub_dir, featured=featured, overwrite=overwrite, normalize=normalize)
            if 'keywords' in entry.keys():
                print('->', entry['keywords'], end='...')
                entry['keywords'] = entry['keywords'].replace('; ', ',').replace(';', ',')
                tags = set(sorted(entry['keywords'].split(','), key=str.lower))
                entry['keywords'] = ','.join(tags)
                print('->', entry['keywords'])

            keys.append(entry['ID'])

    writer = BibTexWriter()
    writer.indent = '    '     # indent entries with 4 spaces instead of one
    writer.order_entries_by = ('ID')
    with open(bibtex, 'w') as bibfile:
        bibfile.write(writer.write(bib_database))
