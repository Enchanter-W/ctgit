@echo off
setlocal enabledelayedexpansion

set "num=0"
set "budget=20000"

:loop
if %num% gtr 5 goto end

for /L %%i in (1,1,3) do (
    python gen.py --num %num% --budget %budget%
    timeout /t 30
)

set /a num+=1
goto loop

:end
echo All tasks completed.
pause