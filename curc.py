#!/usr/bin/env python
import argparse
import urllib2
import json
   
def main():
    parser = argparse.ArgumentParser(description='Command line currency convertor.')
    parser.add_argument('amount', metavar='amount', type=float, 
        help='The amount to be converted.')

    parser.add_argument('from', metavar='from_currency', 
        help='Source currency.')

    parser.add_argument('to', metavar='to_currency', 
        help='Target currency.')

    args = vars(parser.parse_args())

    raw_url = """http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20%3D%20%22{FROM}{TO}%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback="""
    fin_url = raw_url.format(FROM=args['from'], TO=args['to'])

    raw_data = urllib2.urlopen(fin_url)
    json_data = json.loads(raw_data.read())
    xchange_rate = json_data['query']['results']['rate']['Rate']

    print float(xchange_rate) * args['amount']

if __name__ == '__main__':
    main()