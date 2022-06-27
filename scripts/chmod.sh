#!/bin/bash

function FileSuffix() {
    local filename="$1"
    if [ -n "$filename" ]; then
        echo "${filename##*.}"
    fi
}

file=`ls`
echo $file
for pyfile in $file 
do
	if [ "$(FileSuffix ${pyfile})" = "py" ]; then
        chmod a+x $pyfile
		echo "------------"
		echo $pyfile
	else
		echo "++++++++++++"
        echo "not pyscript" $pyfile
		echo "++++++++++++"
    fi
done
echo "------Done!------"