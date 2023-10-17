import click
import sys


@click.command()
@click.option('-c', is_flag=True, show_default=True, default=False, help='Count bytes of the following file')
@click.option('-l', is_flag=True, show_default=True, default=False, help='Count lines of the following file')
@click.option('-w', is_flag=True, show_default=True, default=False, help='Count words of the following file')
@click.argument('file', type=click.File('r'), default=sys.stdin)


def main(c, l, w, file):
    """Simple implimentation of a standard word count command line tool. Check --help for options."""
    if file == None:
        print("no file")
        return
    opened_file = file.read()
    if c:
        click.echo(byteCount(opened_file))
    elif l:
        click.echo(lineCount(opened_file))
    elif w:
        click.echo(wordCount(opened_file))
    else:
        output_all = "    "
        output_all += str(lineCount(opened_file)) + "   "
        output_all += str(wordCount(opened_file)) + "  "
        output_all += str(byteCount(opened_file)) + " "
        output_all += file.name
        click.echo(output_all)


def byteCount(file):
    file_bytes = bytes(file, 'utf-8')
    num_bytes = len(file_bytes)
    return num_bytes


def lineCount(opened_file):
    lines = opened_file.split("\n")
    return len(lines)-1


def wordCount(opened_file):
    words= opened_file.split()
    return len(words)

def createTempFile():
    pass


if __name__ == '__main__':
    main()
