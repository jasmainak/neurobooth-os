call SCHTASKS /S stm /U stm\ACQ /P 5519 /Create /TN TaskOnEvent /TR C:\neurobooth\neurobooth-eel\server_acq.bat /SC ONEVENT /EC Application /MO *[System/EventID=777] /f
call SCHTASKS /S stm /U stm\ACQ /P 5519 /Run /TN "TaskOnEvent"

pause