git add .
read -p 'Your massage: ' msg
git commit -m "$msg"
read branch
git push origin $branch
read -p 'Pull branch? ' pBranch
git pull origin $pBranch