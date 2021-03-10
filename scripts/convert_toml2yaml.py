
for name in ['config', 'languages', 'menus', 'params']:
    fname = '../config/_default/' + name
    print (f'{fname=}')

    import toml
    with open(fname + '.toml', 'r', encoding='utf-8') as f:
    	parsed_toml = toml.load(f)
    print (f'{parsed_toml=}')

    import yaml
    #parsed_yaml = yaml.load(metadata[1], Loader=yaml.FullLoader)
    page = yaml.dump(parsed_toml, encoding=('utf-8'), allow_unicode=True).decode("utf-8") 
    print (f'{page=}')

    with open(fname + '.yaml', 'w', encoding='utf-8') as f:
    	f.write(page + '\n')
