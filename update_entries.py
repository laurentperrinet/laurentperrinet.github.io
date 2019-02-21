

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

if False:
    writer = BibTexWriter()
    writer.indent = '    '     # indent entries with 4 spaces instead of one
    writer.order_entries_by = ('ID')
    with open(bibtex, 'w') as bibfile:
        bibfile.write(writer.write(bib_database))

# 2- making a dictionary to slugify
from academic import slugify

dico = {}
for key in keys:
    dico[slugify(key)] = key

import os
import glob
import toml

if False:
    from academic import clean_bibtex_str
    # 3- updating bibtex with the metadata
    for file_path in glob.glob('content/publication/**/index.md'):
        new_key = file_path.split('content/publication/')[-1].split('/index.md')[0]
        if not new_key in ['___template___',  'person-re-id', '_index.md']:
            with open(file_path, 'r', encoding='utf-8') as source_file:
                page = source_file.read() + '\n'
            metadata = page.split('+++')
            parsed_toml = toml.loads(metadata[1])
            #print(parsed_toml)

            #for new_key in dico.keys():
            old_key = dico[new_key]
            print('input', old_key, ' -> output', new_key)
            #bib_database.get_entry_dict()[old_key]
            translate = {'abstract':'abstract', 'tags':'keywords', 'projects':'projects',
                        'url_pdf':'url', 'url_preprint':'preprint', 'doi':'doi'}

            if 'date' in parsed_toml.keys():
                # parsed_toml['date'] = clean_bibtex_str(entry["date"])
                bib_database.entries_dict[old_key]['year'] = parsed_toml['date'][:4]


            for key in ['projects', 'tags']:
                if key in parsed_toml.keys():
                    tags = parsed_toml[key] #bib_database.entries_dict[old_key][translate['tags']]
                    #print(tags)
                    if not type(tags) == str:
                        parsed_toml[key] = ','.join(tags)
                    #print(parsed_toml['tags'])

            for key in translate.keys():
                if key in parsed_toml.keys():
                    if key == 'abstract':
                        if parsed_toml[key] == "": break
                    #print(parsed_toml[key])

                    bib_database.entries_dict[old_key][translate[key]] = parsed_toml[key]

    writer = BibTexWriter()
    writer.indent = '    '     # indent entries with 4 spaces instead of one
    writer.order_entries_by = ('ID')
    with open(bibtex, 'w') as bibfile:
        bibfile.write(writer.write(bib_database))


# 4- updating metadata with bibtex
from academic import PUB_TYPES, clean_bibtex_str#, clean_bibtex_authors#, clean_bibtex_tags

def clean_bibtex_tags(s, normalize=False):
    """Clean BibTeX keywords and convert to TOML tags"""
    tags = clean_bibtex_str(s).split(',')
    #tags = [f'"{tag.strip()}"' for tag in tags]
    if normalize:
        tags = [tag.lower().capitalize() for tag in tags]
    #tags_str = ', '.join(tags)
    return tags#_str

def clean_bibtex_authors(author_str):
    """Convert author names to `firstname(s) lastname` format."""
    authors = []
    for s in author_str:
        s = s.strip()
        if len(s) < 1:
            continue
        if ',' in s:
            split_names = s.split(',', 1)
            last_name = split_names[0].strip()
            first_names = [i.strip() for i in split_names[1].split()]
        else:
            split_names = s.split()
            last_name = split_names.pop()
            first_names = [i.replace('.', '. ').strip() for i in split_names]
        if last_name in ['jnr', 'jr', 'junior']:
            last_name = first_names.pop()
        for item in first_names:
            if item in ['ben', 'van', 'der', 'de', 'la', 'le']:
                last_name = first_names.pop() + ' ' + last_name
        #authors.append(f'"{" ".join(first_names)} {last_name}"')
        authors.append(f'{" ".join(first_names)} {last_name}')
    return authors

normalize = False
pub_dir = 'publication'
if True:
    for file_path in glob.glob(f"content/{pub_dir}/**/index.md"):
        new_key = file_path.split('content/publication/')[-1].split('/index.md')[0]
        if not new_key in ['___template___',  'person-re-id']:
            with open(file_path, 'r', encoding='utf-8') as source_file:
                page = source_file.read() + '\n'
            metadata = page.split('+++')
            parsed_toml = toml.loads(metadata[1])

            old_key = dico[new_key]
            entry = bib_database.entries_dict[old_key]
            #bib_database.get_entry_dict()[old_key]
            bundle_path = f"content/{pub_dir}/{slugify(entry['ID'])}"
            cite_path = os.path.join(bundle_path, f"{slugify(entry['ID'])}.bib")
            # Save citation file.
            print(f'Saving citation to {cite_path}')
            db = BibDatabase()
            db.entries = [entry]
            writer = BibTexWriter()
            with open(cite_path, 'w', encoding='utf-8') as f:
                f.write(writer.write(db))

            print('input', old_key, ' -> output', new_key)

            # Prepare TOML front matter for Markdown file.
            parsed_toml['title'] = clean_bibtex_str(entry["title"])

            if 'date' in entry:
                parsed_toml['date'] = clean_bibtex_str(entry["date"])
            else:
                if 'month' in entry:
                    parsed_toml['date'] = f"{entry['year']}-{month2number(entry['month'])}-01"
                else:
                    parsed_toml['date'] = f"{entry['year']}-{month2number(entry['month'])}-01-01"

            authors = None
            if 'author' in entry:
                authors = entry['author']
            elif 'editor' in entry:
                authors = entry['editor']
            if authors:
                authors = clean_bibtex_authors([i.strip() for i in authors.replace('\n', ' ').split(' and ')])
                parsed_toml['authors'] = authors #f"[{', '.join(authors)}]"

            parsed_toml['publication_types'] = [f'{PUB_TYPES.get(entry["ENTRYTYPE"], 0)}']

            if 'abstract' in entry:
                parsed_toml['abstract'] = clean_bibtex_str(entry["abstract"])
            else:
                parsed_toml['abstract'] = ""

            #frontmatter.append(f'featured = {str(featured).lower()}')

            # Publication name.
            if 'booktitle' in entry:
                parsed_toml['publication'] = f'*{clean_bibtex_str(entry["booktitle"])}*'
            elif 'journal' in entry:
                parsed_toml['publication'] = f'*{clean_bibtex_str(entry["journal"])}*'
            else:
                parsed_toml['publication'] = ''

            if 'keywords' in entry:
                parsed_toml['tags'] = clean_bibtex_tags(entry["keywords"], normalize)
            if 'projects' in entry:
                parsed_toml['projects'] = clean_bibtex_tags(entry["projects"], normalize)

            if 'url' in entry:
                parsed_toml['url_pdf'] = f'{clean_bibtex_str(entry["url"])}'
            if 'preprint' in entry:
                parsed_toml['url_preprint'] = f'{clean_bibtex_str(entry["url"])}'

            if 'doi' in entry:
                parsed_toml['doi'] = f'{entry["doi"]}'


            metadata[1] = toml.dumps(parsed_toml)

            # Save Markdown file.
            try:
                print(f"Saving Markdown to '{file_path}'")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('+++'.join(metadata))
            except IOError:
                print('ERROR: could not save file.')
