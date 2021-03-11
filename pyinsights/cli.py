import argparse
from typing import Any, Dict, Type
import sys
from datetime import datetime, timedelta

from pyinsights.__version__ import __version__
from pyinsights.config import load_config
from pyinsights.query import query
from formatter import format_result


CliOptions = Type[Dict[str, Any]]


def parse_args() -> Dict[str, Any]:
    """Parse arguments

    Returns:
        Dict[str, Any]
    """

    parser = argparse.ArgumentParser(
        prog='pyinsights',
        description='AWS CloudWatch Logs Insights is wrapped by Python',
    )

    parser.add_argument(
        '-c',
        '--config',
        required=True,
        default='pyinsights.yml',
        help='PyInsights config file path',
    )
    
    parser.add_argument(
        '--from-date',
        help='Date to start with',
    )
    
    parser.add_argument(
        '--date-delta',
        default=-1,
        help='Days to skip',
    )

    parser.add_argument(
        '--date-count',
        default=7,
        help='intervals to run',
    )
    
    parser.add_argument(
        '--to-date',
        default=datetime.now(),
        help='Date to end with',
    )
    
    parser.add_argument(
        '--assume-role',
        help='role to assume',
    )

    parser.add_argument(
        '-f',
        '--format',
        choices=['json', 'table'],
        default='json',
        help='Output format "json" or "table"'
    )

    parser.add_argument('-p', '--profile', help='AWS profile name')

    parser.add_argument('-r', '--region', help='AWS region')

    parser.add_argument(
        '-v', '--version', action='version', version=__version__
    )

    return vars(parser.parse_args())


def process_dates(cli_options: CliOptions):
    
    from_date=cli_options['from_date']
    to_date=cli_options['to_date']
    date_delta=cli_options['date_delta']
    date_count=cli_options['date_count']    
    delta = timedelta(days=date_delta)
    now = datetime.now()
    if not date_count:
        print('no date count')
        return (None,None)
    #print("scanning", date_count)
    for x in range(1,date_count):
        end_date = now.date()
        now = now + delta
        start_date = now.date()
        #print (start_date, end_date) 
        yield (start_date, end_date)        
        #with open("queries/all_{end_date}.yml".format(end_date=end_date),"w") as w:
        #w.write(q.format(start_date=start_date, end_date=end_date))


def run(cli_options: CliOptions) -> bool:
    config = load_config(cli_options['config'])
    count = 0

    #print('start')
    for dates in process_dates(cli_options):
        #print(dates)
        assume_role = None

        if 'assume_role' in cli_options:
            assume_role = cli_options['assume_role']
        #print("role", assume_role)
        
        tmp_result = query(
            dates,
            cli_options['region'],
            cli_options['profile'],
            assume_role,
            config
        )

        if isinstance(tmp_result, dict) and (results := tmp_result.get('results')):
            formatted_result = format_result(cli_options['format'], results)
            sys.stdout.write(formatted_result)
            count = count + 1

    return count > 0


def main() -> bool:
    args = parse_args()
    sys.exit(run(args))

if __name__ == '__main__':
    main()
