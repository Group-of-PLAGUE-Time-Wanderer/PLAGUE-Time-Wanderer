#!/usr/bin/sh
echo "Syncing..."
echo " Fetching..."
git fetch
echo " Done."
echo " Pulling..."
git pull
echo " Done."
echo " Adding..."
git add .
echo " Done."
echo " Commiting..."
git commit -a -m "Sync"
echo " Done."
echo " Pushing..."
git push
echo " Done."
echo "Done."
