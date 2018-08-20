import evaluator
import parser
import tokenizer
import sys  #sys.argv


def main():
    if len(sys.argv) == 1:
        while True:
            user_data = input('> ')
            calculate(user_data)

    else:
        str_user_data = sys.argv[1:]
        user_data = str.join(' ', str_user_data)
        calculate(user_data)


def calculate(user_data):
    try:
        result = evaluator.evaluate(parser.parse(tokenizer.tokenize(user_data)))
        print(result)
    except tokenizer.TokenizeError:
        print('Unrecognized input.')
    except parser.ParseError as err:
        print(f'Badly formed expression. {err}')
    except evaluator.EvaluateError as err:
        print(f'{err}')


if __name__ == '__main__':
    main()