import argparse
import language_calculator

def main():
    parser = argparse.ArgumentParser(description='Quiz for a basic calculation.')
    parser.add_argument('n', type=int, help="How many numbers do you want to add?")
    parser.add_argument('upper_limit', type=int, help="What's the biggest number you want to see?")
    parser.add_argument('operator', type=str, help="only + is supported right now.")
    parser.add_argument('lg', type=str, help="What language do you want to practice? Refer to num2words for language codes.")
    parser.add_argument('--lower_limit', type=str, help="What's the smallest number you want to see?")

    args = parser.parse_args()
    options = vars(args)

    if options['lower_limit'] is None:
        lower_limit = 1
    else:
        lower_limit = options['lower_limit']

    language_calculator.quizCalculation(options['n'], options['upper_limit'], options['operator'], options['lg'], lower_limit)

if __name__ == '__main__':
    main()