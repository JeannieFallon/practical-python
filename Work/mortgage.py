# mortgage.py
#
# Exercise 1.7
import sys
import getopt


OPTS = 'hs:e:p:'
OPTS_LONG = ['help', 'start', 'end', 'extra']


def main(argv):
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    num_months = 0

    extra_payment = 0.0
    extra_payment_start_month, extra_payment_end_month = 0, 0

    try:
        opts, args = getopt.getopt(argv, OPTS, OPTS_LONG)
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print('Arguments:\n-s, --start:\textra payment start month\n-e, --end:\textra payment end month\n-p, --payment:\textra payment amount')
                return
            elif opt in ('-s', '--start'):
                extra_payment_start_month = opt
            elif opt in ('-e', '--end'):
                extra_payment_end_month = opt
            elif opt in ('-p', '--payment'):
                extra_payment = opt
    except getopt.error as e:
        print(str(e))

    if extra_payment_start_month and extra_payment_end_month and extra_payment:
        print('Calculating values for extra payments')
    else:
        print('Calculating default values. Use -h, --help to see custom options')

    while principal > 0:
        if num_months == extra_payment_start_month:
            while num_months < extra_payment_end_month:
                if principal <= 0:
                    break
                principal = principal * (1+rate/12) - extra_payment
                total_paid = total_paid + extra_payment
                num_months += 1

        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        num_months += 1

    print(f'Total paid: {round(total_paid, 2)} in {num_months} months')


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
