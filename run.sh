echo "*******************************************"
echo "Now installing necessary packages"
echo "*******************************************"
# need password to install logilab
sudo chown -R $USER /Library/Python/2.7
cd logilab-constraint-0.5.0
# install logilab
python setup.py install
cd ..
# install pandas
pip install pandas
# run program
echo "*******************************************"
echo "Please look for a tkinter application (the icon is a feather)"
echo "*******************************************"
python ShiftScheduler.py
echo "*******************************************"
echo "Please look for your results in the file you specified."
echo "*******************************************"
