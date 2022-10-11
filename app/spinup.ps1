Remove-Item .\db.sqlite3 -Force

$migrate = "python .\manage.py migrate"
$fixtures = "python .\manage.py loaddata investors investments"
$runserver = "python .\manage.py runserver 8000"

Invoke-Expression $migrate
Invoke-Expression $fixtures
Invoke-Expression $runserver