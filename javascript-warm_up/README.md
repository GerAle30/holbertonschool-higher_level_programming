# JavaScript - Warm up

This directory contains JavaScript exercises for learning basic JavaScript concepts and Node.js fundamentals.

## Requirements

- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS with Node.js (version 14.x)
- **Code Style**: Semistandard compliant (version 16.x.x) - Standard rules + semicolons
- **Shebang**: First line of all files should be `#!/usr/bin/node`
- **File permissions**: All files must be executable
- **Line endings**: All files should end with a new line

## Setup

### Install Node.js 14:
```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install semi-standard:
```bash
sudo npm install semistandard --global
```

## Files

- `0-javascript_is_amazing.js` - Prints "JavaScript is amazing"
- `1-multi_languages.js` - Prints multiple programming language statements
- `2-arguments.js` - Handles command line arguments

## Usage

Run any JavaScript file with:
```bash
./filename.js
```

Check code style with:
```bash
semistandard *.js
```
