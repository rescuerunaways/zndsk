# zndsk

install dependencies: 
pip install -r requirements.txt

run tests:
python -m unittest url_test
python -m unittest integration_test (performs real calls to pytickets, so it's should be running)


run a server:
./zndsk.py 


Usage:


  zndsk.py show [--page=<number>]


  zndsk.py show <ticket>


  zndsk.py (-h | --help)
  
Example usage:


  ./zndsk.py show


  ./zndsk.py show 2


  ./zndsk.py show --page=2


