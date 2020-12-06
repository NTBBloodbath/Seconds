![Seconds](https://socialify.git.ci/NTBBloodbath/Seconds/image?description=1&descriptionEditable=Transform%20seconds%20to%20minutes%2C%20hours%2C%20etc.%20and%20vice%20versa%20quickly%2C%20easily%2C%20and%20understandable%20by%20humans&font=Source%20Code%20Pro&forks=1&issues=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light)

![Python Versions](https://img.shields.io/pypi/pyversions/seconds)
![Version](https://img.shields.io/pypi/v/seconds?color=green&label=version)
[![Downloads](https://pepy.tech/badge/seconds)](https://pepy.tech/project/seconds)
![License](https://img.shields.io/pypi/l/seconds)

Seconds is a utility package to transform seconds to minutes, hours, etc. and vice versa
quickly, easily, understandable by humans and without external dependencies
so its performance is excellent and it's extremely lightweight!

------

## Why use Seconds?
Since Seconds doesn't contain external dependencies, it's extremely lightweight (only 12kB!)
and very fast, it becomes the perfect tool to manage and transform time!

------

# Quick start
## Installation
Seconds requires Python 3.x and can be installed through `pip` with the following command.
```sh
pip3 install -U seconds

# Or from github's latest commit
# Available branches:
#   • master
pip3 install -U git+https://github.com/NTBBloodbath/Seconds@branch
```

## Usage example
This is a brief example of Secs.
```py
# Lets import Secs class from Seconds Package
from seconds import Secs

# Lets pass 5 minutes to seconds and seconds to 10 minutes
Secs("5m") # => 300
Secs(600)  # => 10 minutes
# But we want to abbreviate our minutes so we
# will pass the abbrev parameter to options
Secs(600, abbrev=True) # => 10m

# Lets pass 6 months to seconds and then pass 1 year to seconds
Secs("6mo") # => 110451600
Secs("1y")  # => 220903200
```

## Documentation
You can see the Seconds documentation through the `help()` function of the REPL.

------

# License
**Seconds is distributed under MIT License.**

# Contributing
You can see how to contribute [here](./CONTRIBUTING.md)

# Code of Conduct
You can see the code of conduct [here](./CODE_OF_CONDUCT.md)
