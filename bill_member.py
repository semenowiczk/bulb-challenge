"""
A python script that given a set of meter readings,
computes a member’s monthly energy bill.
"""

from datetime import date, datetime
from calendar import monthrange
import load_readings
from tariff import BULB_TARIFF

def gas2energy(gas_reading):
    """
    Convert gas m^3 to kWh.
    Taken the formula from this page:
    https://www.theenergyshop.com/guides/how-to-convert-gas-units-to-kwh
    """
    correction_factor = 1.02264
    calorific_value = 40
    thermal_energy_per_kwh = 3.6
    kwh_from_gas = ((gas_reading * correction_factor) * calorific_value) / thermal_energy_per_kwh
    return kwh_from_gas

def process_data(energy_sources, bill_month, bill_year):
    """
    calculates the total £ amount and kWh for both electricity and gas
    for the calendar month by looping through energy sources
    """
    amount = 0
    total_estimated_kwh = 0
    for energy_source in energy_sources:
        for source, items in energy_source.items():
            if source in ['electricity', 'gas']:
                for i, data in enumerate(items):
                    if (datetime.fromisoformat(
                            data['readingDate'][:-1]).year == bill_year
                            and datetime.fromisoformat(
                                data['readingDate'][:-1]).month == bill_month):
                        index = i
                read = items[index]
                previous_read = items[index-1]
                read_date = datetime.fromisoformat(read['readingDate'][:-1])
                previous_read_date = datetime.fromisoformat(previous_read['readingDate'][:-1])
                read_interval = (read_date - previous_read_date).days
                average_consumption = (
                    (read.get('cumulative') - previous_read.get('cumulative')) / read_interval)
                number_of_days_in_month = monthrange(read_date.year, read_date.month)[1]
                estimated_consumption = average_consumption * number_of_days_in_month
                if source == 'gas' and read['unit'] == 'm3':
                    estimated_consumption = gas2energy(estimated_consumption)
                tariff = BULB_TARIFF[source]
                amount += (
                    (number_of_days_in_month * tariff['standing_charge'])
                    + (estimated_consumption * tariff['unit_rate'])) / 100
                total_estimated_kwh += estimated_consumption
            else:
                print(f"Unsupported {source} energy source")
    return amount, total_estimated_kwh

def calculate_bill(member_id=None, account_id=None, bill_date=None, readings_file=None):
    """
    Calculate the bill for provided member_id, account argument, and billing date,
    it will compute the bill for the customer.
    """
    readings = load_readings.get_readings(readings_file)
    data = readings.get(member_id)
    amount = 0
    kwh = 0
    account = ''
    bill_date = date.fromisoformat(bill_date)
    if account_id.lower() == 'all':
        for account in data:
            for acct_id, energy_sources in account.items():
                sources_amount, consumption = process_data(
                    energy_sources, bill_date.month, bill_date.year)
                amount += sources_amount
                kwh += consumption
    else:
        for member in data:
            if account_id in member:
                account = member
        amount, kwh = process_data(account[account_id], bill_date.month, bill_date.year)
    return round(amount, 2), int(kwh)

def calculate_and_print_bill(member_id, account, bill_date, readings_file):
    """Calculate the bill and then print it to screen.
    Account is an optional argument - I could bill for one account or many.
    There's no need to refactor this function."""
    amount, kwh = calculate_bill(member_id, account, bill_date, readings_file)
    print('Hello {member}!'.format(member=member_id))
    print('Your bill for {account} on {date} is £{amount}'.format(
        account=account,
        date=bill_date,
        amount=amount))
    print('based on {kwh}kWh of usage in the last month'.format(kwh=kwh))
