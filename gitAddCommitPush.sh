git add .
read -p 'Your massage: ' msg
git commit -m "$msg"
read -p 'Push branch name: ' branch
git push origin $branch
read -p 'Pull branch name: ' pBranch
git pull origin $pBranch