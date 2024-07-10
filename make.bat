@echo on
set PY_FILE=pes_we_txs_info.py
set PROJECT_NAME=TXS Info
set VERSION=1.0.0
set FILE_VERSION=file_version_info.txt
set ICO_DIR=resources/pes_indie.ico

pyinstaller --onefile "%PY_FILE%" --icon="%ICO_DIR%" --name "%PROJECT_NAME%_%VERSION%"  %EXTRA_ARG% --version-file "%FILE_VERSION%"

cd dist
tar -acvf "%PROJECT_NAME%_%VERSION%.zip" *
pause
