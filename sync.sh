#!/usr/bin/sh
echo "Syncing..."
echo -n " Fetching... "
git fetch > log.txt
echo " Done."
echo -n " Pulling..."
git pull > log.txt
echo " Done."
echo -n " Adding..."
git add . > log.txt
echo " Done."
echo -n " Commiting..."
git commit -a -m "Sync" > log.txt
echo " Done."
echo -n " Pushing..."
git push > log.txt
echo " Done."
echo "Done."
