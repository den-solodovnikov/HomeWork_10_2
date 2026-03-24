from src.decorators import log, my_function


def test_log_err(capsys):
    @log()
    def example_function(x, y):
        return x + y

    example_function(1,'2')
    captured = capsys.readouterr()
    assert captured.out == "example_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"


def test_log_ok(capsys):
    @log()
    def example_function(x, y):
        return x + y

    example_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "example_function OK\n"


def test_log_err_in_file():
    @log(filename='mylog.txt')
    def example_function(x, y):
        return x + y

    example_function(1,'2')
    with open('mylog.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        assert content == "example_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}"


def test_log_ok_in_file():
    @log(filename='mylog.txt')
    def example_function(x, y):
        return x + y

    example_function(1,2)
    with open('mylog.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        assert content == "example_function OK"