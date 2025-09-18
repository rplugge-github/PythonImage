# PythonImage

https://www.askpython.com/python/examples/images-into-cartoons

python.exe -m pip install --upgrade pip

pip install opencv-python
pip install matplotlib
pip install argparse


  WARNING: The scripts f2py.exe and numpy-config.exe are installed in 'C:\Users\rplug\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  WARNING: The scripts pip.exe, pip3.13.exe and pip3.exe are installed in 'C:\Users\rplug\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.
  WARNING: The scripts fonttools.exe, pyftmerge.exe, pyftsubset.exe and ttx.exe are installed in 'C:\Users\rplug\AppData\Roaming\Python\Python313\Scripts' which is not on PATH

=====
python cartoon.py --help
python cartoon.py --filename "C:\Users\rplug\Pictures\Saved Pictures\20220608_134822000_iOS.jpg"
python cartoon.py --show 0 --output
python cartoon.py --show 1 --output "C:\temp\image_output.jpg"
=====
python arguments: python script.py arg1 arg2

import sys

# Access arguments
script_name = sys.argv[0]  # The script name
arguments = sys.argv[1:]   # All arguments after the script name

print(f"Script Name: {script_name}")
print(f"Arguments: {arguments}")

====
python argparse example: python script.py --name John --age 30

import argparse

# Create parser
parser = argparse.ArgumentParser(description="Example script with arguments")

# Add arguments
parser.add_argument("--name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age")

# Parse arguments
args = parser.parse_args()

print(f"Name: {args.name}")
print(f"Age: {args.age}")

====
# python click example: python script.py --name John --age 30
python script.py

import click

@click.command()
@click.option('--name', prompt='Your name', help='The person\'s name.')
@click.option('--age', prompt='Your age', help='The person\'s age.')
def greet(name, age):
    click.echo(f"Hello {name}, you are {age} years old!")

if __name__ == '__main__':
    greet()
