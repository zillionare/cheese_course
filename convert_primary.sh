src="/apps/cheese_course/docs/课程/primary"
dst="/apps/cheese_course/code/courses/primary"
for file in `ls $src`;do echo $file; notedown --match=python $src/$file > $dst/${file%.*}.ipynb; done


