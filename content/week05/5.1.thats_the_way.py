import os


def thats_the_way(directory_path: str) -> list[str]:
    '''
    Returns a list of files starting with 'deep' in the directory
    :param directory_path: str, path to the directory
    :return: list of str, files starting with 'deep'
    '''
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f'{directory_path} not found')

    return [f for f in os.listdir(directory_path) if f.startswith('deep')]


if __name__ == '__main__':

    try:
        path = 'content\week05\images'
        files_starting_with_deep = thats_the_way(path)
        print(f'\nFiles starting with "deep" in the directory {path} :\n{files_starting_with_deep}')
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
