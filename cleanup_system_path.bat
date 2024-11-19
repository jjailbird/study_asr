rem Not working 1024 characters limit !!!!

@echo off
setlocal enabledelayedexpansion

rem Get the current PATH
set "oldPath=%PATH%"
set "newPath="

rem Split the old PATH into individual paths
for %%A in ("%oldPath:;=" "%") do (
    if exist %%~A (
        rem If the path exists, add it to newPath
        set "newPath=!newPath!%%~A;"
    ) else (
        echo Removing non-existent path: %%~A
    )
)

rem Remove the trailing semicolon
set "newPath=!newPath:~0,-1!"

rem Update the PATH environment variable
setx PATH "!newPath!" >nul

echo Updated PATH variable.
endlocal