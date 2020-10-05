# Project Cleaner

## About
Tired of all your `vendor` and `node_module` folders scattered here and there taking up all that space?
Here's your solution!

## Important note:
- Currently for **Unix-based machines only**. 
- You will need to have the system shell commands `rm` and `du` installed (usually installed by default)

## Usage
- Clone this repo to your machine
- run `python3 main.py starting_path`
  - `starting_path` is the root directory from where the script will start searching
  - by default, `starting_path` is the directory that the script is called ( '`.`' )


### **[Bonus]** Setting this up as a shell script
- Make sure you're within the project dir
- Run `chmod +x main.py` 
  - (this will make it executable, you *may* have to `sudo` it)
- Go to a directory which is 'owned' by you (where you have write permisison)
- I would suggest you make a `bin` folder in your home (`~/`) directory
- Copy the **absolute path** to the `bin` folder (e.g. `/home/user_name/bin`)
- Add it to the end of your `$PATH` shell variable export

### OR

**READ** and run the `sample_setup.sh`.
- Emphasis on **READ**, I am not responsible if your machine sends your nearest nuclear reactor into meltdown or kills your cat / dog / favourite human
- Download the script from Github or read and copy it.
- Bash:
  - `wget https://raw.githubusercontent.com/JacquesFernandes/web-project-cleaner/master/sample_setup.sh -O /var/tmp/wpc_setup.sh && bash /var/tmp/wpc_setup.sh`