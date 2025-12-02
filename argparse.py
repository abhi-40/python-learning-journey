import argparse

parser=argparse.ArgumentParser(description="Simple calc")

parser.add_argument("num1",type=float,help="1st num")
parser.add_argument("num2",type=float,help="2nd num")
parser.add_argument("op",choices=["add","sub","div","mul"],help="operation to perf")

args=parser.parse_args()

if(args.operation=="add"):
    print(f"the result is {args.num1+args.num2}")

elif(args.operation=="sub"):
    print(f"the result is {args.num1-args.num2}")

elif(args.operation=="div"):
    print(f"the result is {args.num1/args.num2}")

elif(args.operation=="mul"):
    print(f"the result is {args.num1*args.num2}")