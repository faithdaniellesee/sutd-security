#!/bin/sh

# Download and install phantomjs; 
if ! which phantomjs > /dev/null; 
then
  sudo apt install phantomjs -y
  sudo rm $HOME/phantomjs -f
  sudo rm /usr/bin/phantomjs -f
  PHANTOM_CMD='#!/bin/sh\nLD_LIBRARY_PATH="/usr/lib/phantomjs:$LD_LIBRARY_PATH"\nexport LD_LIBRARY_PATH\nexport QT_QPA_PLATFORM=offscreen\nexec "/usr/lib/phantomjs/phantomjs" "$@"' > $HOME/phantomjs  
  sudo touch /usr/bin/phantomjs
  sudo chown httpd:httpd /usr/bin/phantomjs
  echo $PHANTOM_CMD > $HOME/phantomjs
  echo $PHANTOM_CMD > /usr/bin/phantomjs
  chmod +x $HOME/phantomjs
  chmod +x /usr/bin/phantomjs
  echo -e "Done, phantomjs saved to /home/httpd/phantomjs.\nMake sure to call phantomjs as follows: QT_QPA_PLATFORM=offscreen phantomjs"
fi
