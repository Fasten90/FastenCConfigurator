# FastenCConfigurator

# Design:
# X             | DEFINE1 | DEFINE2 | DEFINE3
# NAME OF SET   | x       |         | 
# new debug set | x       | x       | x


# TODO: Add argparser
# Input file

# Expected result:
# All configs (defines) generated with: " -DCONFIG_USE_PANEL_FASTENNODE=1"


def parse_md(content):
    """ return with config list """
    # TODO: Support comment: started line with '#'
    lines = content.splitlines()
    headers = lines[0].split('|')[1:]
    settings = [line.split('|') for line in lines[1:]]
    generated_settings = {}
    for item in settings:
        config_name = item[0]
        config_settings = item[1:]
        generated_settings[config_name] = []
        for index, config_item in enumerate(config_settings):
            print(config_item, index)
            generated_settings[config_name].append((headers[index], True if ('x') in config_item else False ))
    return generated_settings


def read_config(confile_file_path='project_config.md'):
    with open(confile_file_path) as config_file:
        content = config_file.read()
        config = parse_md(content)
        return config


if __name__ == '__main__':
    config = read_config()
    # TODO: generate
    print('Config', config)
