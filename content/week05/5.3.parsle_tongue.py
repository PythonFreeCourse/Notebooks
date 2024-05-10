import re
import time


def find_secret_messages(filename: str, timeout: int = 10) -> list:
    '''
    Finds the secret messages in the file
    :param filename: str, file path
    :param timeout: int, timeout in seconds
    :return: list, secret messages
    '''

    result = []
    buffer_size = 8192
    overlap_size = 20
    pattern = re.compile(b'[a-z]{5,}!')
    start_time = time.time()  

    with open(filename, 'rb') as file:
        buffer = file.read(buffer_size)
        while buffer:
            if time.time() - start_time > timeout:
                print("Timeout reached\n")
                break
            for match in pattern.finditer(buffer):
                result.append(match.group().decode('utf-8'))
                print(f'Found secret message: {match.group().decode("utf-8")}')

            next_chunk = file.read(buffer_size - overlap_size)
            buffer = buffer[len(next_chunk):] + next_chunk
    return result


if __name__ == '__main__':
    print(find_secret_messages('content\\week05\\resources\\logo.jpg', timeout=15))
