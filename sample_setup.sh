USER_BIN=~/bin
SOURCES_DIR=$USER_BIN/.sources

mkdir -p $SOURCES_DIR

cd $SOURCES_DIR

echo 'Removing code, if it already exists'
rm -rf web-project-cleaner

echo "Cloning project into $SOURCES_DIR"
git clone https://github.com/JacquesFernandes/web-project-cleaner.git

echo "Setting main.py to be executable"
chmod +x ./web-project-cleaner/main.py

cd $USER_BIN
USER_BIN_ABS_PATH=$(pwd -P)

echo "Deleting symlink, if it exists"
rm -f web_project_cleaner

echo "Creating symlink 'web_project_cleaner'"
ln -s $SOURCES_DIR/web-project-cleaner/main.py web_project_cleaner

echo "Adding path to .bashrc"
echo "export PATH=\$PATH:$USER_BIN_ABS_PATH" >> ~/.bashrc
source ~/.bashrc

echo ""
echo "Done! Get started by doing 'web_project_cleaner -h'"