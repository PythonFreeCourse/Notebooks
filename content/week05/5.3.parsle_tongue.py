def parsle_tongue():
    chunk_size = 1024
    chars = []
    data = []
    is_sequential = False
    with open('resources\logo.jpg','rb') as file:
        while True:
            chunk = file.read(chunk_size)
            for byte in chunk:
                if byte == ord('!') and is_sequential:
                    if len(chars) >= 5:
                        data.append(''.join(chars))
                    chars.clear()
                    is_sequential = False
                elif ord('a') <= byte <= ord('z'):
                    chars.append(chr(byte))
                    is_sequential = True
                else:
                    is_sequential = False
                    chars.clear()
            if not chunk:
                break
    return data

def main():
    print(' '.join(parsle_tongue()))

if __name__ == '__main__':
    main()