#!/bin/bash -e
# NOTE: The current working directory is the root of the repository

head=$(git rev-parse HEAD)
hash=$(git log --pretty=%H --merges | sed -n 3p)
git reset --hard $hash
find . -name '*.pyc' -delete
fab --list
fab --list | awk '/^\s+/ { print $1 }' > ~/tasks_before
git reset --hard $head
find . -name '*.pyc' -delete
fab --list
fab --list | awk '/^\s+/ { print $1 }' > ~/tasks_after


compare=$(comm -13 --nocheck-order ~/tasks_before ~/tasks_after)

echo "New tasks to run:"
echo "$compare"

IFS='
'

# Wake up the machines
curl -sSL http://webhook.freeside.co.uk/hooks/wakeup-desktops --data "secret=${webhook_secret}";

# FUTURE: Could we do this in parallel?
for x in $compare; do
   fab -R desktops "$x" -u root
done
