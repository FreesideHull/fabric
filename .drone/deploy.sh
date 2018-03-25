head=$(git rev-parse HEAD)
hash=$(git log --pretty=%H --merges | sed -n 2p)
git reset --hard $hash
fab --list --short > ~/tasks_before
git reset --hard $head
fab --list --short > ~/tasks_after

echo "New tasks to run:"
comm -13 --nocheck-order ~/tasks_before ~/tasks_after

compare=$(comm -13 --nocheck-order ~/tasks_before ~/tasks_after)

echo "$compare"

for x in $compare; do
   fab install -R desktops "$x" -p $SSH_PASSOWRD
done