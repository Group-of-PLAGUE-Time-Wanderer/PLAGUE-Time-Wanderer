#!/usr/bin/sh
echo "New sync" >> sync.log
echo "Syncing..."
echo -n " Fetching... "
git fetch >> sync.log
echo " Done."
echo -n " Pulling..."
git pull >> sync.log
echo " Done."
echo -n " Adding..."
git add . >> sync.log
echo " Done."
echo -n " Commiting..."
git commit -a -m "Sync" >> sync.log
echo " Done."
echo -n " Pushing..."
git push &>> sync.log
echo " Done."
echo "Done."
