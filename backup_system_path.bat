@echo off
setlocal

rem 현재 날짜와 시간을 포맷하여 파일 이름에 사용
set "timestamp=%DATE:~-4,4%-%DATE:~-7,2%-%DATE:~-10,2%_%TIME:~-11,2%-%TIME:~-8,2%"
set "backupFile=PATH_Backup_%timestamp%.txt"

rem 현재 PATH 환경 변수를 백업 파일에 저장
echo Backing up PATH variable to %backupFile%
echo %PATH% > "%backupFile%"

echo Backup completed successfully.
endlocal