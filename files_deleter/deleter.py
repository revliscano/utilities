import os
import glob
import sys
import datetime as dt
import operator


def files_by_date(comparison: str, date: str) -> list:
    """
    date should be a string that comply with the format: m-d-Y
    comparison should be a string with one of the following values: gt, lt, eq 
    """
    if comparison not in ('gt', 'lt', 'eq'):
        raise ValueError('Invalid comparison')
    op = getattr(operator, comparison)
    target_date = dt.datetime.strptime(date, '%m-%d-%Y').date()
    get_fdate = lambda x: dt.datetime.fromtimestamp(os.lstat(x).st_ctime).date()
    return [f for f in os.listdir() if op(get_fdate(f), target_date)]

OPTIONS = {'-ext': lambda x: glob.glob(f'*.{x}'),
           '-contains': lambda x: [f for f in os.listdir() if x in f],
           '-date': files_by_date}

try:
    matching_files = OPTIONS[sys.argv[1]](*sys.argv[2:])
    if not matching_files: raise FileNotFoundError
    print('Files to be PERMANENTLY deleted: ', *matching_files, sep='\n')
    proceed = input('Proceed? [y/N]: ') or 'N'
    if proceed == 'y':
        for file in matching_files:
            os.remove(file)
except (KeyError, IndexError):
    print('Invalid option. Available options are:',
          '-ext <extension>: Match files with the given extension',
          '-contains <word>: Match files containing given word in its name',
          '-date <lt|gt|eq> <date>: Match files which creation date is\
            \r\nlower, greater or equal than the given date',
          sep='\n')
except FileNotFoundError:
    print('File(s) with given name, extension or date not found.')
except (ValueError, TypeError) as e:
           print(e)
