# Bulb Challenge

## Overview

Thank you for interviewing at Bulb and taking the time to complete this coding exercise.

We expect the challenge to take around 3-4 hours, however feel free to take as long as you need. If you run out of time, that’s fine, just send us a README with the details of what you planned to include in your implementation.

Please approach this as you would a production problem with respect to quality and consider that we will ask you to extend your work in a pairing exercise as part of the technical interview.

The instructions are duplicated in the README.md file in the starting code ZIP file that should download.

In this challenge, we’d like you to write a small program which, given a set of meter readings, computes a member’s monthly energy bill. To do this, we have stubbed out the following files for you:

- `bill_member.py`, which contains functions to compute the customer bill and print it to screen.
  - You should implement calculate_bill. This is the entry point to your solution.
  - `calculate_bill` is currently hardcoded to give the correct answer for August 2017.
  - There’s no need to change calculate_and_print_bill.
- `test_bill_member.py`, a test module for bill_member.
main.py, the entry point for the program, there’s no need to make changes to this module.
- `tariff.py`, prices by kWh for all energy
- `load_readings.py`, provides a function for loading the readings from the given json.
- `readings.json`, contains a set of monthly meter readings for a given year, member and fuel

## We’d like you to:

- Implement the calculate_bill function, so that given a member_id, optional account argument and billing date, we can compute the bill for the customer.

We do not want you to spend time on:

- Making this backwards compatible with python <= 3.

You can assume:

- All times are UTC.
- We’re only dealing with £ denominated billing.
- You only need to handle electricity and gas billing.
- Energy is consumed linearly.
- The billing date is the last day of the month.
- Readings are always taken at midnight.
- There is only one meter reading per billing period.
- The JSON file structure will remain the same in any follow on exercise.

## Solution

- `gas2energy()` - converts gas m^3 to kW
- `process_data()` - calculates the total £ amount and kWh for both electricity and gas for the calendar month by looping through energy sources
- `calculate_bill()` - calculate bill for the provided account ID and member.

## Requirements

- Python3

## How to use

 ```bash
  ./main.py --help - usful information about additional arguments
  ./main.py - with out any arguments it will use by default `readings.json` as source of readings, MEMBER_ID='member-123', ACCOUNT_ID='ALL' and BILL_DATE='2017-08-31'
  ./main.py --member_id member-234 --account_id account-asd --readings_file kris_readings.json - using `kris_readings.json` as source of readings
  ```

Example output:

 ```bash
  ./main.py --member_id member-234 --account_id account-asd --readings_file kris_readings.json
  Hello member-234!
  Your bill for account-asd on 2017-08-31 is £27.57
  based on 167kWh of usage in the last month
```


## To do

- python error handling
