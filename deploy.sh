#!/usr/bin/env bash
# Deploy the de science model landing page to the Hetzner box, mood/convolingu
# style — but it's a STATIC Astro site, so we build locally and rsync the
# output (no Node toolchain needed on the server, no systemd service).
# Run this from your Mac (your SSH works; the agent's sandbox blocks port 22).
#
# Usage:
#   ./deploy.sh "commit message"   # commit local changes, push main, deploy
#   ./deploy.sh                    # build current tree + deploy (no commit)
#
# Prereq: dasmodel.co + www, and desciencemodel.com + www, must already point
# their A records at this server (159.69.6.146) so certbot can issue TLS.
set -euo pipefail
cd "$(dirname "$0")"

SERVER=root@159.69.6.146
APP_DIR=/opt/desciencemodel
BRANCH=main
PRIMARY_DOMAIN=dasmodel.co
OLD_DOMAIN=desciencemodel.com
EMAIL=carla@positron.vc

# 1. optional commit + push (keeps GitHub as the source of truth)
if [ -n "${1:-}" ]; then
  git add -A
  git commit -m "$1" || echo "Nothing to commit"
fi
git push origin "$BRANCH" || echo "⚠️  push failed (continuing with local build)"

# 2. build the static site locally (dist/ is gitignored; built fresh each time)
echo "→ building Astro site (www/dist)"
npm --prefix www ci
npm --prefix www run build

# 3. ship the build + the server setup script to the box
echo "→ rsync build to $SERVER:$APP_DIR/dist"
ssh "$SERVER" "mkdir -p $APP_DIR/dist"
rsync -az --delete www/dist/        "$SERVER:$APP_DIR/dist/"
rsync -az      infra/server_deploy.sh "$SERVER:$APP_DIR/server_deploy.sh"

# 4. configure nginx + TLS on the server (idempotent)
ssh "$SERVER" "
  APP_DIR=$APP_DIR PRIMARY_DOMAIN=$PRIMARY_DOMAIN OLD_DOMAIN=$OLD_DOMAIN EMAIL=$EMAIL \
    bash $APP_DIR/server_deploy.sh
"

echo
echo "✅ Deployed. Live at: https://$PRIMARY_DOMAIN/"
echo "   $OLD_DOMAIN now 301s to https://$PRIMARY_DOMAIN (path preserved)."
