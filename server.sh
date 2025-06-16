#!/bin/bash

# Exit if anything fails
set -e

echo "🚀 Connecting to remote server..."

ssh -t -p 1980 prakash2@95.217.203.22 '
  set -e
  source /home3/prakash2/virtualenv/public_html/prakashthapa617.com.np/3.11/bin/activate
  cd /home3/prakash2/public_html/prakashthapa617.com.np
  echo "✅ Environment ready. You are now inside the server shell."
  exec bash
'
