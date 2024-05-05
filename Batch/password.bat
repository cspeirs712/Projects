@Echo off
cls
:Password
Set input=
set /p input= Password (input the press enter) :
if %input%==password goto YES
if not %input%==password goto NO

:yes

Start Notepad
Exit

:NO

Echo INCORRECT Password
pause
goto Password