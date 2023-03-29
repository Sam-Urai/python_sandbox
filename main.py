import os
import pathlib
from person import PersonPhones



def process(dir_name):
    pf = PersonPhones()
    path = pathlib.Path(dir_name)
    with open(path / 'phones_listing.txt', 'w') as f_out:
        for filename in os.listdir(dir_name):
            phones = []
            if filename.endswith('.json'):
                person = pf.create_from_json(path / filename)
                phones = person.phones
            elif filename.endswith('.yaml'):
                person = pf.create_from_yaml(path / filename)
                phones = person.phones

            for phone in phones:
                f_out.write(f'{phone}\n')


if __name__ == '__main__':
    process('files')
    print('Done with the files list. Check phones_listing.txt for results.')