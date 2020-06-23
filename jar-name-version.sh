#! /usr/bin/env bash

# A manually created file is passed into the script.
# Let say it is a jarinfo file,  generated after building android-gradle-plugin or someting of a type.
# Can always check file type at (https://paste.debian.net/1153428/).

echo "	~~List of Jars extracted~~"
echo -e "==============================================\n"
echo "Here's all what can be done!"
echo -e "1. Output on the current shell.\n2. Stores the extracted information in a file named jar-info (present in same dir).\n3. To generate a paste. (Make sure you have pastebinit installed).\n"
read -p "Enter your Choice: " choice
case $choice in
	1)
		while read line
		do
			jar="$(echo $line | rev| cut -d'/' -f 1 | rev)"
			echo "$jar" | awk -F ".jar" '{print $1}'
		done < jarinfo
		;;
	2)
		while read line
		do
			jar="$(echo $line | rev| cut -d'/' -f 1 | rev)"
			echo "$jar" | awk -F ".jar" '{print $1}' >>jar-info
		done < jarinfo
		;;
	3)
		while read line
		do
			jar="$(echo $line | rev| cut -d'/' -f 1 | rev)"
			echo "$jar" | awk -F ".jar" '{print $1}' >>jar-info
		done < jarinfo
		less jar-info | pastebinit
		rm jar-info
		;;
esac
echo -e "\n=============================================="
echo "Jars Info Extracted"
