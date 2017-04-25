#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>MOS Device Management</title>'
echo '</head>'
echo '<body>'

echo '<h2>Device Mangement Submenu</h3><br><br>'
echo '<h3>Monero Network Service</h3>'

echo "<form method=GET action=\"${SCRIPT}\">"

  echo '<input type="radio" name="val_z" value="1" checked> Turn Monero Network Service On<br>'\
       '<input type="radio" name="val_z" value="2"> Turn Monero Network Service Off<br>'\

  echo '<br><input type="submit" value="Process Form">'\
       '<input type="reset" value="Reset"></form>'

  # Make sure we have been invoked properly.

  if [ "$REQUEST_METHOD" != "GET" ]; then
        echo "<hr>Script Error:"\
             "<br>Usage error, cannot complete request, REQUEST_METHOD!=GET."\
             "<br>Check your FORM declaration and be sure to use METHOD=\"GET\".<hr>"
        exit 1
  fi

  # If no search arguments, exit gracefully now.

  if [ -z "$QUERY_STRING" ]; then
        exit 0
  else
     # No looping this time, just extract the data you are looking for with sed:
     XX=`echo "$QUERY_STRING" | sed -n 's/^.*val_x=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     YY=`echo "$QUERY_STRING" | sed -n 's/^.*val_y=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     ZZ=`echo "$QUERY_STRING" | sed -n 's/^.*val_z=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     echo "val_x: " $XX
     echo '<br>'
     echo "val_y: " $YY
     echo '<br>'
     echo "val_z: " $ZZ
  fi


echo 'Turn Monero Network Service on<br>'
echo 'Turn Monero Network Service off<br>'
echo 'Modify boot settings<br>'
echo 'Download and upload rates<br>'
echo 'Management Level<br>'
echo 'Manually Update Monero software<br>'


echo 'Set mining address<br>'



echo '</body>'
echo '</html>'

exit 0
