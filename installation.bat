@echo off
@title Installing modules...

cd %~dp0

if not exist venv (
    python -m venv venv

    if errorlevel 1 (
        echo Error: Failed to create virtual environment.
        exit /b 1
    )
	echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
)

call venv\Scripts\activate.bat

pip install -r requirements.txt

call venv\Scripts\deactivate.bat

cls

@title Modules have been installed!

echo.
echo All packages were installed. Thanks for using A.K. software
echo.
pause