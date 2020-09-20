import argparse
from jmx import *
from engine import printRed
from engine import printGreen


def main():
    try:
        parser = argparse.ArgumentParser(description='Evaluate JMeter Test Plan')
        requiredNamed = parser.add_argument_group('mandatory arguments')
        requiredNamed.add_argument("-f", "--file", dest="jmxfile", help="Add JMeter Test Plan file path")
        args = parser.parse_args()
        jmx = args.jmxfile
        with open(jmx,'r') as f:
            parseJMX(jmx)
        f.close()       
    except FileNotFoundError:
        printRed("Trouble in accessing JMeter test plan. Check for missing file and/or its permissions.")

if __name__ == "__main__":
    main()