echo "*******************************************"
echo "Now installing necessary packages"
echo "*******************************************"
# Need password to install logilab
sudo chown -R $USER /Library/Python/2.7
cd logilab-constraint-0.5.0
# Install logilab
python setup.py install
cd ..
# Install pandas
pip install pandas
# Run program
echo "*******************************************"
echo "Please look for a tkinter application (the icon is a feather)"
echo "*******************************************"
python ShiftScheduler.py
echo "*******************************************"
echo "Please look for your results in the file you specified."
echo "*******************************************"
