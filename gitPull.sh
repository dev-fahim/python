echo "Pulling from gitHub..."
read -p 'Pull branch name: ' branch
git pull origin $branch
