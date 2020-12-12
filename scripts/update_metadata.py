# -*- coding: utf-8 -*-

verbose = False

for type in ['Presentations', 'Publications']:

    # 1- getting all citekeys
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
    from bibtexparser.bwriter import BibTexWriter
    from bibtexparser.bibdatabase import BibDatabase
    from bibtexparser.customization import convert_to_unicode

    bibtex = f'../../perrinet_curriculum-vitae_tex/LaurentPerrinet_{type}.bib'
    keys = []
    # 1- Load BibTeX file for parsing.
    with open(bibtex, 'r', encoding='utf-8') as bibtex_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        for entry in bib_database.entries:
            #parse_bibtex_entry(entry, pub_dir=pub_dir, featured=featured, overwrite=overwrite, normalize=normalize)
            keys.append(entry['ID'])

    # 2- making a dictionary to slugify
    from academic.import_bibtex import slugify, month2number

    dico = {}
    for key in keys:
        dico[slugify(key)] = key

    import os
    import glob

    # 4- updating metadata with bibtex
    from academic.import_bibtex import clean_bibtex_str
    from academic.publication_type import PUB_TYPES, PublicationType

    import datetime
    import dateutil.parser

    def getDateTimeFromISO8601String(s, full=False):
        d = dateutil.parser.parse(s)
        if not full:
            # then get the current date
            d = d.date()
        return d

    def clean_bibtex_tags(s, normalize=False):
        """Clean BibTeX keywords and convert to yaml tags"""
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
    if type == 'Presentations':
        pub_dir = 'content/talk'
    elif type == 'Publications':
        pub_dir = 'content/publication'

    import yaml

    for file_path in glob.glob(f"{pub_dir}/**/index.md"):
        new_key = file_path.split(f'{pub_dir}/')[-1].split('/index.md')[0]
        if not new_key in ['___template___',  'person-re-id', 'template']:
            with open(file_path, 'r', encoding='utf-8') as source_file:
                page = source_file.read() + '\n'
            metadata = page.split('---')
            # print(metadata)
            parsed_yaml = yaml.load(metadata[1], Loader=yaml.FullLoader)

            # print('new_key =', new_key, 'dico[new_key]', dico[new_key])
            old_key = dico[new_key]
            entry = bib_database.entries_dict[old_key]
            #bib_database.get_entry_dict()[old_key]
            bundle_path = f"{pub_dir}/{slugify(entry['ID'])}"

            #  old_cite_path = os.path.join(bundle_path, f"{slugify(entry['ID'])}.bib")
            cite_path = os.path.join(bundle_path, "cite.bib")
            # import os
            # os.rename(old_cite_path, cite_path)
            # Save citation file.
            if verbose: print(f'Saving citation to {cite_path}')
            db = BibDatabase()
            db.entries = [entry]
            writer = BibTexWriter()
            with open(cite_path, 'w', encoding='utf-8') as f:
                f.write(writer.write(db))

            if verbose: print('input', old_key, ' -> output', new_key)

            # Prepare yaml front matter for Markdown file.
            parsed_yaml['title'] = clean_bibtex_str(entry["title"])

            if 'date' in entry:
                date_str = clean_bibtex_str(entry["date"])
            else:
                date_str = clean_bibtex_str(entry["year"])
            # print('len(date_str)', len(date_str))
            if len(date_str) == 4:
                # the date is just the year, so we guess from the rest of the information...
                if 'month' in entry:
                    print(date_str, entry['month'])
                    date_str = f"{date_str}-{month2number(entry['month'])}-01"
                else:
                    date_str = f"{date_str}-01-01"
            parsed_yaml['date'] = getDateTimeFromISO8601String(date_str)

            # Time stamping the entry to be published today
            if not 'publishDate' in parsed_yaml.keys():
                today = datetime.datetime.now().date().isoformat()#[2:]
                parsed_yaml['publishDate'] = today

            authors = None
            if 'author' in entry:
                authors = entry['author']
            elif 'editor' in entry:
                authors = entry['editor']
            if authors:
                authors = clean_bibtex_authors([i.strip() for i in authors.replace('\n', ' ').split(' and ')])
                parsed_yaml['authors'] = authors #f"[{', '.join(authors)}]"

            for this_key in ['abstract', 'summary']:
                if this_key in entry:
                    parsed_yaml[this_key] = clean_bibtex_str(entry[this_key])
                else:
                    parsed_yaml.pop(this_key, None)

            #frontmatter.append(f'featured = {str(featured).lower()}')

            if 'keywords' in entry:
                parsed_yaml['tags'] = clean_bibtex_tags(entry["keywords"], normalize)

            for this_key in ['grants', 'projects']:
                if this_key in entry:
                    # parsed_yaml['projects'] = []
                    parsed_yaml[this_key] = clean_bibtex_tags(entry[this_key], normalize)
                    if verbose: print(parsed_yaml[this_key])
                    # print(parsed_yaml['projects'])


            for url_key in ['url_slides', 'url_code', 'url_link']:
                if url_key in entry:
                    parsed_yaml[url_key] = f'{clean_bibtex_str(entry[url_key])}'

            if 'url' in entry:
                parsed_yaml['url_pdf'] = f'{clean_bibtex_str(entry["url"])}'

            if 'preprint' in entry:
                parsed_yaml['url_preprint'] = f'{clean_bibtex_str(entry["preprint"])}'

            if 'doi' in entry:
                parsed_yaml['doi'] = f'{entry["doi"]}'

            if type == 'Presentations':
                # if 'time_start' in entry:
                #     parsed_yaml['date'] = getDateTimeFromISO8601String(clean_bibtex_str(entry["time_start"]))
                # else:
                #     parsed_yaml['date'] = getDateTimeFromISO8601String(clean_bibtex_str(entry["ID"][:10]))
                #     # parsed_yaml['date'] = getDateTimeFromISO8601String('1973-02-23')

                for this_key in ['event_url', 'location']:
                    if this_key in entry:
                        parsed_yaml[this_key] = f'{clean_bibtex_str(entry[this_key])}'
                if 'booktitle' in entry:
                    parsed_yaml['event'] = f'{clean_bibtex_str(entry["booktitle"])}'

                if 'time_start' in entry:
                    parsed_yaml['time_start'] = getDateTimeFromISO8601String(f'{clean_bibtex_str(entry["time_start"])}', full=True)
                    parsed_yaml['date'] = parsed_yaml['time_start'] # overwrite date
                    # HACK to show the entry = Scheduled page publish date.

                else:
                    #parsed_yaml['time_start'] = getDateTimeFromISO8601String(clean_bibtex_str(entry["ID"][:10]))
                    parsed_yaml['date'] = getDateTimeFromISO8601String(clean_bibtex_str(entry["ID"][:10]))


                #parsed_yaml['publishDate'] = today #str(parsed_yaml['date'])[:4] + '-01-01' # overwrite date
                # remove obsolete entry:
                parsed_yaml.pop("time_start", None)
                parsed_yaml.pop("time_end", None)


            elif type == 'Publications':

                parsed_yaml['publication_types'] = [f'{PUB_TYPES.get(entry["ENTRYTYPE"], 0)}']

                # Publication name.
                if 'booktitle' in entry:
                    parsed_yaml['publication'] = f'*{clean_bibtex_str(entry["booktitle"])}*'
                elif 'journal' in entry:
                    parsed_yaml['publication'] = f'*{clean_bibtex_str(entry["journal"])}*'
                else:
                    parsed_yaml['publication'] = ''

                # TODO:  optional abbreviated version.
                # publication_short = "In *ICMEW*"


            metadata[1] = yaml.dump(parsed_yaml, encoding=('utf-8'), allow_unicode=True)
            metadata[1] = metadata[1].decode('utf-8')

            if not len(metadata) == 3 : print('Z'*150, '  len(metadata)', len(metadata), 'new_key', new_key)

            # clean-up: strip double lines
            # metadata[2] = metadata[2].replace('\n\n', '\n')

            # Save Markdown file.
            try:
                if verbose: print(f"Saving Markdown to '{file_path}'")
                page = '---\n'.join(metadata).strip('\n')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(page + '\n')
            except IOError:
                print('ERROR: could not save file.')
