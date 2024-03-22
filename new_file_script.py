from os import path


def create_file(kata_name, kyu: int):
    path_to_folder = fr'C:\Users\Koren Kaplan\Desktop\Studies\Python\CodeWarsDrills\{str(kyu)}kyu'
    with open(f'{path.join(path_to_folder, kata_name.replace(" ", "_"))}.py', 'w') as file:
        file.write(f'''"""
5kyu -> {kata_name}:
{'-' * (len(kata_name) + 9)}
"""''')


create_file("Find the missing term in an Arithmetic Progression", 6)