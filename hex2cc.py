#!/usr/bin/python

#  hex2cc converts the result from a 125khz card id to a CC (ZK) number
#
#  Adam Laurie <adam@algroup.co.uk>
#  http://rfidiot.org/
#
#  This code is copyright (c) Adam Laurie, 2006, All rights reserved.
#  For non-commercial use only, the following terms apply - for all other
#  uses, please contact the author:
#
#    This code is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#

# 1. Reverse each nibble
# 2. Reverse the binary of each nibble
# 3. convert each hex nibble to a 2 digit decimal number


def reverse(ch) -> chr:
    '''
    reverses the bit order eg. 0001 -> 1000
    :param ch:
    :return:
    '''
    if ch is '0':
        return '0'
    if ch is '1':
        return '8'
    if ch is '2':
        return '4'
    if ch is '3':
        return 'C'
    if ch is '4':
        return '2'
    if ch is '5':
        return 'A'
    if ch is '6':
        return '6'
    if ch is '7':
        return 'E'
    if ch is '8':
        return '1'
    if ch is '9':
        return '9'
    if ch is 'A':
        return '5'
    if ch is 'B':
        return 'D'
    if ch is 'C':
        return '3'
    if ch is 'D':
        return 'B'
    if ch is 'E':
        return '7'
    if ch is 'F':
        return 'F'


def rev_conv(ch) -> chr:
    '''
    reverses the bit order eg. 0001 -> 1000 and
    convert each from hex to a two digit number
    :param ch:
    :return:
    '''
    if ch is '0':
        return '00'
    if ch is '1':
        return '08'
    if ch is '2':
        return '04'
    if ch is '3':
        #return 'C'
        return '12'
    if ch is '4':
        return '02'
    if ch is '5':
        #return 'A'
        return '10'
    if ch is '6':
        return '06'
    if ch is '7':
        #return 'E'
        return '14'
    if ch is '8':
        return '01'
    if ch is '9':
        return '09'
    if ch is 'A':
        return '05'
    if ch is 'B':
        #return 'D'
        return '13'
    if ch is 'C':
        return '03'
    if ch is 'D':
        #return 'B'
        return '11'
    if ch is 'E':
        return '07'
    if ch is 'F':
        #return 'F'
        return '15'


def conv_rev(ch) -> chr:
    '''
    reverses the bit order eg. 0001 -> 1000 and
    convert each from hex to a two digit number
    :param ch:
    :return:
    '''
    if ch == '00':
        return '0'
    if ch == '08':
        return '1'
    if ch == '04':
        return '2'
    if ch == '12':
        return '3'
    if ch == '02':
        return '4'
    if ch == '10':
        return '5'
    if ch == '06':
        return '6'
    if ch == '14':
        return '7'
    if ch == '01':
        return '8'
    if ch == '09':
        return '9'
    if ch == '05':
        return 'A'
    if ch == '13':
        return 'B'
    if ch == '03':
        return 'C'
    if ch == '11':
        return 'D'
    if ch == '07':
        return 'E'
    if ch == '15':
        return 'F'


def hex2cc(hex_id) -> str:
    res = ''
    cid = iter(hex_id)
    for frst in cid:
        scnd = next(cid)
        res += rev_conv(scnd)
        res += rev_conv(frst)
    return res


def cc2hex(cc_id) -> str:
    res = ''
    ii = 0

    cid = iter(cc_id)
    for frst in cid:
        scnd = next(cid)
        thrd = next(cid)
        frth = next(cid)
        res += conv_rev(str(thrd) + str(frth))
        res += conv_rev(str(frst) + str(scnd))
    return res


print(hex2cc('0100BC2FF1'))
print(cc2hex(hex2cc('0100BC2FF1')))
print(cc2hex('08000000111304081504'))

#print(hex2cc('0012390959'))
