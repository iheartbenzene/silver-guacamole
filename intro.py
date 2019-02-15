from textwrap import dedent
from datetime import *

lets_go = datetime.now() - datetime(2018, 12, 5)

print(dedent("""
             Okay, so this is a test run.
             Don't set the bar too high and you won't be disappointed.
             Okay. Here we go.

             WARNING: THIS IS COMMAND LINE ONLY.

             Thanks for watching!
             """))

print(f"\n {lets_go.days} days and counting. \n \n \n")
