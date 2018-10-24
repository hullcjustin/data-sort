import sort_doc
import docexe


def target_start():
    data = sort_doc.start_sort()
    docexe.write_to_file(data)

def main():
    target_start()


if __name__ == '__main__':
    main()