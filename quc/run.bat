@echo off
echo Starting QinchuanUnion server...
echo.
echo.
python manage.py runsslserver --certificate server.crt --key server.key 0.0.0.0:3939