@REM pyinstaller months_setup.py
pyinstaller --windowed ../src/months_setup.py --icon=../images/tree.ico
@REM cd ../../../Desktop
@REM mklink /d Months c:\Users\zrodr\Documents\Projects\Months\dist\Month_Reflections\Month_Reflections