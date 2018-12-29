"""
ArgsParse is apython module that allow neat argument parsing in python
Automatically genrate the usage
It has built in function
Auto formta the o/p to console
It has inteface with system module to grab command line arguments
support checking and make sure required argument provided
How Args parse works
1.parser=argsparse.ArgumentParser()
2.parser.add_argument("num",help="helptext",type=int)
3.args=parser.parse_args()
print(args.num)
positional arguments are required arguments that we need to complete program
positional argument do not required - becauase its not an option
"""

import argparse

def f(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
def Main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group();
    group.add_argument("-v","--verbose",action="store_true")
    group.add_argument("-q","--quit",action="store_true")
    parser.add_argument("numb",help="The fab no",type=int)
    parser.add_argument("-o","--output",help="Output result to a file",action="store_true")
    args=parser.parse_args()
    result=f(args.numb)
    print(f"the {args.numb}th fib is {result}")

    if args.verbose:
        print(f"the {args.numb}th fib is {result}")
    elif args.quit:
        print(result)

    if args.output:
        print("file open")
        fp=open('fibnachies.txt','a+')
        fp.write(f"the {args.numb}th fib is {result}");
        fp.close()

if __name__ == '__main__':
    Main()

"""
1.as per titile optional arguments are optional
2.we can create as many of as we like and argsarser will handel that
3.parser.add_argument("--quit",help="helptext",action="store_true"

Mutually exlusive arguments we can select one or other option but not both
this is done using group.it automatically generate o/p telling user that he can select any one option

4. if we wish to call a function with option then we can create a subclass of argsparse.Action then we have
to supply a __call__method
5.argsparse also supports taking arguments in list this is done using nargs attribute in tha add_argument method
nargs='+' we don't know how many argument be
nargs=2 two arguments are expected
just keep that these go into python list
"""
