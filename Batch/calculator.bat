@echo off
title Batch Calculator by Craig
color 1f
:top
echo --------------------------------------------------------------
echo Welcome to Batch Calculator by Craig
echo --------------------------------------------------------------
echo.
set /p sum=
set /a ans=%sum%
echo.
echo = %ans%
echo --------------------------------------------------------------
pause
cls
echo Previous Answer: %ans%
goto top
pause
exit