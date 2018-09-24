import sort_doc
import docexe


def target_start():
    data = sort_doc.start_sort()
    count = 0
    docexe.write_to_file(data)

def main():
    print('Got to main')
    target_start()


if __name__ == '__main__':
    main()