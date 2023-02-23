for file in `ls docs/courses/primary`;do echo $file; notedown --match=python docs/primary/$file > docs/code/primary/${file%.*}.ipynb; done

git add .
git commit -m "docs"
git push

mkdocs gh-deploy
