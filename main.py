#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from bill_member import calculate_and_print_bill

def parse_arguments():
    """Parse arguments for cmd line application."""
    import argparse
    parser = argparse.ArgumentParser(
        description="""Main entry point for command line app to compute your \n
        energy bill based on a given readings.json file, which is assumed \n
        to be in the root directory.""")
    parser.add_argument('--member_id', type=str, default='member-123',
                        help='The identifier we use to select\
                         the member profile.')
    parser.add_argument('--account_id', type=str, default='ALL',
                        help='The identifier we use to select the member account.\
                        You can choose to bill for all accounts,\
                        or an individual account.')
    parser.add_argument('--bill_date', type=str, default='2017-08-31',
                        help='ISO standard formatted date for UTC timezone (e.g. 2017-08-31).')
    parser.add_argument('--readings_file', type=str, default='./readings.json',
                        help='JSON file path with readings')
    return parser.parse_args()


def main(member_id=None, account_id=None, bill_date=None, readings_file=None):
    """Main entry point for bill calculation command line app.

    member_id :: the member identifier in our dataset.

    account_id :: the account identifier in our dataset.
    If left unset, we return a total bill for all accounts.

    bill_date :: is a given business date that we want to compute the bill for.
    by default, we expect that the billing period is this date minus one month.

    Expects an iso standard date format as a string, e.g. '2017-11-01'
    Timezone is assumed to be GMT.
    """
    calculate_and_print_bill(member_id, account_id, bill_date, readings_file)


if __name__ == '__main__':
    args = parse_arguments()
    main(member_id=args.member_id,
         account_id=args.account_id,
         bill_date=args.bill_date,
         readings_file=args.readings_file)
