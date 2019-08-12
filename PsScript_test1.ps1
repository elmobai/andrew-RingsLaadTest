PS C:\Users\Emlyn Farrell> $arr = @()
$path = C:\Users\Emlyn Farrell\Desktop\andrew ps test 
$pattern = "(?<=.*Focus)\w+?(?=Focus.*)"

Get-Content $path | Foreach {if ([Regex]::IsMatch($_, $pattern)) {
           $arr += [Regex]::Match($_, $pattern)
            }
        }
$arr | Foreach {$_.Value} 