#!/usr/bin/env bash
# Runs ON the Hetzner server (as root), after deploy.sh has rsynced the built
# static site to $APP_DIR/dist. Idempotent: safe to run on every deploy.
#
# Sets up two nginx vhosts and TLS, sharing the box with the existing Python
# apps (nginx routes by Host header / server_name, so this leaves mood and
# convolingo untouched):
#   - PRIMARY_DOMAIN  -> serves the static site from $APP_DIR/dist
#   - OLD_DOMAIN      -> permanent 301 to PRIMARY_DOMAIN, preserving the path
#
# Driven by environment variables (see deploy.sh):
#   APP_DIR         app dir on server     (default: /opt/desciencemodel)
#   PRIMARY_DOMAIN  new canonical domain  (default: dasmodel.co)
#   OLD_DOMAIN      domain to redirect    (default: desciencemodel.com)
#   EMAIL           certbot contact       (default: carla@positron.vc)
set -euo pipefail

APP_DIR="${APP_DIR:-/opt/desciencemodel}"
PRIMARY_DOMAIN="${PRIMARY_DOMAIN:-dasmodel.co}"
OLD_DOMAIN="${OLD_DOMAIN:-desciencemodel.com}"
EMAIL="${EMAIL:-carla@positron.vc}"
WEBROOT="$APP_DIR/dist"

if [ ! -f "$WEBROOT/index.html" ]; then
  echo "✗ $WEBROOT/index.html missing — did deploy.sh rsync the build?" >&2
  exit 1
fi

# ── packages (only installs what's missing) ─────────────────────────────────
command -v nginx   >/dev/null 2>&1 || { apt-get update && apt-get install -y nginx; }
command -v certbot >/dev/null 2>&1 || { apt-get update && apt-get install -y certbot python3-certbot-nginx; }

# ── primary vhost: serve the static site ────────────────────────────────────
# HTTP only here; certbot --nginx adds the 443 listener + http->https redirect.
echo "→ nginx vhost for $PRIMARY_DOMAIN (static: $WEBROOT)"
cat > /etc/nginx/sites-available/dasmodel <<NGINX
server {
    listen 80;
    listen [::]:80;
    server_name $PRIMARY_DOMAIN www.$PRIMARY_DOMAIN;

    root $WEBROOT;
    index index.html;

    # Astro emits page/index.html (directory format); cover .html too.
    location / {
        try_files \$uri \$uri/ \$uri.html =404;
    }
}
NGINX

# ── old domain: permanent 301 to the new canonical domain, keeping the path ──
echo "→ nginx vhost for $OLD_DOMAIN (301 -> $PRIMARY_DOMAIN)"
cat > /etc/nginx/sites-available/desciencemodel <<NGINX
server {
    listen 80;
    listen [::]:80;
    server_name $OLD_DOMAIN www.$OLD_DOMAIN;
    return 301 https://$PRIMARY_DOMAIN\$request_uri;
}
NGINX

ln -sf /etc/nginx/sites-available/dasmodel       /etc/nginx/sites-enabled/dasmodel
ln -sf /etc/nginx/sites-available/desciencemodel /etc/nginx/sites-enabled/desciencemodel
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl reload nginx

# ── TLS for all four names in one cert; idempotent across redeploys ──────────
# --redirect makes plain HTTP 301 to HTTPS. Requires every name below to
# already resolve to THIS server, or the ACME challenge fails.
echo "→ certbot (TLS for $PRIMARY_DOMAIN, www, $OLD_DOMAIN, www)"
if certbot --nginx --non-interactive --agree-tos -m "$EMAIL" --keep-until-expiring --redirect \
     -d "$PRIMARY_DOMAIN" -d "www.$PRIMARY_DOMAIN" \
     -d "$OLD_DOMAIN"     -d "www.$OLD_DOMAIN"; then
  systemctl reload nginx
  echo "✅ $PRIMARY_DOMAIN is live (HTTPS); $OLD_DOMAIN 301s to it."
else
  echo "⚠️  certbot failed. Confirm all four names resolve to this server:" >&2
  echo "    dig +short $PRIMARY_DOMAIN www.$PRIMARY_DOMAIN $OLD_DOMAIN www.$OLD_DOMAIN" >&2
  echo "    then re-run deploy.sh. The site already serves over HTTP in the meantime." >&2
  exit 1
fi
