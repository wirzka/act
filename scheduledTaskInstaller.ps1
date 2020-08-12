# put here the absolute path of your python
$exe = ""
# put here the script name
$arg = "act.py"
# put here the absolute path of your script
$wd = ""

$A = New-ScheduledTaskAction -Execute $exe -Argument $arg -WorkingDirectory $wd
$T = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -Action $A -Trigger $T -TaskName "CSIRT_Alerting" -Description "CSIRT alert monitoring."
