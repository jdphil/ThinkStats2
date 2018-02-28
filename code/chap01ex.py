"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function
import sys

import nsfg
import thinkstats2


def read_fem_resp(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
    """Function to read the Female Response File.

    dct_file: dictionary file
    dat_file: data file in zip format
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df_resp = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df_resp


def check_preg_num():
    """Function to Check that Pregnum in the response file
        matches the number of pregnacies in the pregnancy file.

    dct_file: dictionary file
    dat_file: data file in zip format
    """
    for row in RESP.iterrows():
        if row['pregnum'] != len(PREG_MAP[row['caseid']]):
            return False

    return True


def main():
    """Tests the functions in this module.

    script: string script name
    """
    RESP = read_fem_resp()
    PREG = nsfg.ReadFemPreg()
    PREG_MAP = nsfg.MakePregMap(PREG)
    print(RESP.pregnum.value_counts())
    assert check_preg_num()
    print('%s: All tests passed.')


if __name__ == '__main__':
    main(*sys.argv)
