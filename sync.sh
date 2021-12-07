#!/usr/bin/sh
echo "Syncing..."
echo -n " Fetching... "
git fetch > log1.txt
echo " Done."
echo -n " Pulling..."
git pull > log2.txt
echo " Done."
echo -n " Adding..."
git add . > log3.txt
echo " Done."
echo -n " Commiting..."
git commit -a -m "Sync" > log4.txt
echo " Done."
echo -n " Pushing..."
git push &> log.txt
echo " Done."
echo "Done."
