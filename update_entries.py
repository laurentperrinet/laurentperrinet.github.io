

# 1- getting all citekeys
import bibtexparser
from bibtexparser.bparser import BibTexParser
#from bibtexparser.bwriter import BibTexWriter
#from bibtexparser.bibdatabase import BibDatabase
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


# 2- making a dictionary to slugify
from academic import slugify

dico = {}
for key in keys:
    dico[slugify(key)] = key

# 3- updating bibtex with the metadata
import os
import glob
import toml
from bibtexparser.bwriter import BibTexWriter

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
        translate = {'abstract':'abstract', 'tags':'tags', #'projects':'projects',
                    'url_pdf':'url', 'url_preprint':'preprint', 'doi':'doi'}
        for key in translate.keys():
            if key in parsed_toml.keys():
                print(parsed_toml[key])
                bib_database.entries_dict[old_key][translate[key]] = parsed_toml[key]

writer = BibTexWriter()
with open('bibtex.bib', 'w') as bibfile:
    bibfile.write(writer.write(bib_database))


# 4- updating metadata with bibtex
if False:
    # Prepare TOML front matter for Markdown file.
    frontmatter = ['+++']
    frontmatter.append(f'title = "{clean_bibtex_str(entry["title"])}"')
    if 'month' in entry:
        frontmatter.append(f"date = {entry['year']}-{month2number(entry['month'])}-01")
    else:
        frontmatter.append(f"date = {entry['year']}-01-01")

    authors = None
    if 'author' in entry:
        authors = entry['author']
    elif 'editor' in entry:
        authors = entry['editor']
    if authors:
        authors = clean_bibtex_authors([i.strip() for i in authors.replace('\n', ' ').split(' and ')])
        frontmatter.append(f"authors = [{', '.join(authors)}]")

    frontmatter.append(f'publication_types = ["{PUB_TYPES.get(entry["ENTRYTYPE"], 0)}"]')

    if 'abstract' in entry:
        frontmatter.append(f'abstract = "{clean_bibtex_str(entry["abstract"])}"')
    else:
        frontmatter.append('abstract = ""')

    frontmatter.append(f'featured = {str(featured).lower()}')

    # Publication name.
    if 'booktitle' in entry:
        frontmatter.append(f'publication = "*{clean_bibtex_str(entry["booktitle"])}*"')
    elif 'journal' in entry:
        frontmatter.append(f'publication = "*{clean_bibtex_str(entry["journal"])}*"')
    else:
        frontmatter.append('publication = ""')

    if 'keywords' in entry:
        frontmatter.append(f'tags = [{clean_bibtex_tags(entry["keywords"], normalize)}]')

    if 'url' in entry:
        frontmatter.append(f'url_pdf = "{clean_bibtex_str(entry["url"])}"')

    if 'doi' in entry:
        frontmatter.append(f'doi = "{entry["doi"]}"')

    frontmatter.append('+++\n\n')

    # Save Markdown file.
    try:
        print(f"Saving Markdown to '{markdown_path}'")
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(frontmatter))
    except IOError:
        print('ERROR: could not save file.')
