#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>MOS Device Management</title>'
echo '</head>'
echo '<body>'

echo '<h3>Device Mangement Submenu</h3><br><br>'
echo '<a href="access_logs.cgi">Access Logs</a><br>'
echo '<a href="monero_settings.cgi">Manage Monero Settings</a><br>'
echo '<a href="ubuntu_settings.cgi">Manage Ubuntu Settings</a><br>'
echo '<a href="status.cgi">Status of Monerodo</a><br>'
echo '<a href="power.cgi">Power Down or Restart</a><br>'



echo '</body>'
echo '</html>'

