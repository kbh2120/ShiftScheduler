sudo chown -R $USER /Library/Python/2.7
cd logilab-constraint-0.5.0
python setup.py install
cd ..
pip install pandas
python ShiftScheduler.py
