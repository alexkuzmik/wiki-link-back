## Prerequisites
Package requires at least Python 3.9 (because of new typing system) <br>
If you don't have suitable environment you may install and activate it via following command in terminal <br>
`python3.9 -m venv .venv && source .venv/bin/activate`


## Usage
This code will run parallel computation with amount of working processes equal to doubled amount of CPU cores <br>
`python back_links.py https://en.wikipedia.org/wiki/Israel` 

In order to configure amount of workers manually use --workers argument <br>
`python back_links.py https://en.wikipedia.org/wiki/Israel --workers N` will use N working processes



