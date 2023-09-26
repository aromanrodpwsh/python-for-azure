
$Nombre=Read-Host "Cual es su nombre"
$Apellido = Read-Host "Cual es tu apellido"
$FechaNacimiento= Read-Host "Cual es tu fecha de nacimiento"
$Sexo= Read-Host "Eres hombre o mujer"
Write-Host "Felicitaciones ingresaste la informacion correctamente"
[System.Diagnostics.Process]::Start("Safari","http://google.com")