import argparse
import sys
import pytest


class ParseArgs:

    def __init__(self):
        parser = argparse.ArgumentParser(description='Runs the neural net.', usage='python model.py <command> [<args>]')
        parser.add_argument("command", help="Subcommand of run.")
        args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def build(self):
        parser = argparse.ArgumentParser(
            description='Trains and builds the neural net')

        parser.add_argument('--batch_size', action='store', type=int)
        parser.add_argument('--epoch', action='store', type=int)
        parser.add_argument('--verbose', action='store', type=int)
        parser.add_argument('--callbacks', action='store', type=int)
        parser.add_argument('--validation_split', action='store', type=int)
        parser.add_argument('--validation_data', action='store', type=int)
        parser.add_argument('--class_weight', action='store', type=int)
        parser.add_argument('--sample_weight', action='store', type=int)
        parser.add_argument('--initial_epoch', action='store', type=int)
        parser.add_argument('--steps_per_epoch', action='store', type=int)
        parser.add_argument('--validation_steps', action='store', type=int)

        args = parser.parse_args(sys.argv[2:])
        epoch = args.epoch
        batch_size = args.batch_size
        print(f'Building neural net, epoch={epoch}, batch_size={batch_size}')

    def predict(self):
        parser = argparse.ArgumentParser(
            description='Predicts the sentiment of the sentence')

        print(f'Predicting sentiment, score=')


@pytest.fixture(scope='function')
def setUp():
    sys.argv = ['parseargs.py']  # used to because sys.argv ordering different using pytest
    return sys.argv


def test_help_message_correct(capsys, setUp):
    setUp.append('-h')
    with pytest.raises(SystemExit):
        ParseArgs()
    out, err = capsys.readouterr()
    assert "Runs the neural net." in out


def test_unknown_command(capsys, setUp):
    setUp.append('whatever')
    with pytest.raises(SystemExit):
        ParseArgs()
    out, err = capsys.readouterr()
    assert "Unrecognized command" in out


def test_build_message_correct(capsys, setUp):
    setUp.append('build')
    ParseArgs()
    out, err = capsys.readouterr()
    assert "Building neural net" in out


def test_predict(capsys, setUp):
    setUp.append('predict')
    ParseArgs()
    out, err = capsys.readouterr()
    assert "Predicting sentiment" in out


def test_epoch(capsys, setUp):
    setUp.append('build')
    setUp.append('--epoch')
    setUp.append('1')
    ParseArgs()
    out, err = capsys.readouterr()
    assert "epoch=1" in out

def test_two_arguments(capsys, setUp):
    setUp.append('build')
    setUp.append('--epoch')
    setUp.append('1')
    setUp.append('--batch_size')
    setUp.append('1')

    ParseArgs()
    out, err = capsys.readouterr()
    assert "epoch=1" in out
    assert "batch_size=1" in out




if __name__ == '__main__':
    ParseArgs()
