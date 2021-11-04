Title: Pyenv - Managing Multiple Python Versions
Date: 2021-10-04 16:47
Modified: 2021-10-04 16:47
Category: Blog
Tags: pelican, publishing
Slug: pyenv 
Authors: Christian Prada
Summary: Aprende a manejar multiples versiones de python la con la ayuda de  **« Python Granada »**
Extract: Aprende a manejar multiples versiones de python con la ayuda de « Python Granada »

## ¿Porqué usar pyenv y no el que trae el sistema por defecto?

Imagina que trabajas en una empresa donde el proyecto que se desarrolla tiene varias versiones de Python, por ejemplo [Odoo](https://www.odoo.com/es_ES) el cual como es habitual podemos tener varios clientes con versiones más actuales o no y tienes que dar soporte a cada una de ellas. 

O más fácil aun, simplemente eres como yo, desarrollador inquieto que le gusta trastear y probar los cambios que traen las nuevas versiones de Python.

En cualquiera de los dos ejemplos que te expongo, puede resultarnos tedioso o engorroso la tarea de gestionar muchas versiones, y más aun no meter la pata ejecutando una versión que no es.

Pyenv es una herramienta que te permite fijar versiones de python por directorios locales o seleccionar por defecto una versión global que usarás para tu sistema.

## ¿Para qué sistemas operativos está disponible?

* Windows
* MacOS
* Linux (Debian, Ubuntu, Fedora/CentOS/RHEL, OpenSUSE, Alpine, Archlinux, ...)

## Dependencias necesarias e Instalación

### MacOs & Linux

Ubuntu / Debian

```bash
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

```bash
# the sed invocation inserts the lines at the start of the file
# after any initial comment lines
sed -Ei -e '/^([^#]|$)/ {a \
export PYENV_ROOT="$HOME/.pyenv"
a \
export PATH="$PYENV_ROOT/bin:$PATH"
a \
' -e ':a' -e '$!{n;ba};}' ~/.profile
echo 'eval "$(pyenv init --path)"' >>~/.profile

echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

Fedora/CentOS/RHEL

```bash
$ sudo yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite \
sqlite-devel openssl-devel xz xz-devel libffi-devel
```

```bash
sed -Ei -e '/^([^#]|$)/ {a \
export PYENV_ROOT="$HOME/.pyenv"
a \
export PATH="$PYENV_ROOT/bin:$PATH"
a \
' -e ':a' -e '$!{n;ba};}' ~/.bash_profile
echo 'eval "$(pyenv init --path)"' >> ~/.bash_profile

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init --path)"' >> ~/.profile

echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

OpenSUSE

```bash
zypper in zlib-devel bzip2 libbz2-devel libffi-devel \
libopenssl-devel readline-devel sqlite3 sqlite3-devel xz xz-devel
```

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init --path)"' >> ~/.profile

echo 'if command -v pyenv >/dev/null; then eval "$(pyenv init -)"; fi' >> ~/.bashrc
```

Alpine

```
apk add libffi-dev ncurses-dev openssl-dev readline-dev \
tk-dev xz-dev zlib-dev
```

Archlinux

```
yay -S pyenv
```

MacOS

```bash
$ brew install openssl readline sqlite3 xz zlib pyenv
```

```bash
# BASH
# the sed invocation inserts the lines at the start of the file
# after any initial comment lines
sed -Ei -e '/^([^#]|$)/ {a \
export PYENV_ROOT="$HOME/.pyenv"
a \
export PATH="$PYENV_ROOT/bin:$PATH"
a \
' -e ':a' -e '$!{n;ba};}' ~/.profile
echo 'eval "$(pyenv init --path)"' >>~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

```bash
# ZSH
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

### Windows:

El paquete se llama: [pyenv-win](https://github.com/pyenv-win/pyenv-win#finish-the-installation), puedes instalarlo de cuatro maneras diferentes, pero aquí usaremos pip, entendiendo que ya dispones de una versión de Python instalada:

```bash
Powershell o Git Bash: pip install pyenv-win --target $HOME\\.pyenv
cmd.exe: pip install pyenv-win --target %USERPROFILE%\.pyenv
```

Pasos para finalizar la instalación:

Añade PYENV, PYENV_HOME and PYENV_ROOT a tus variables de entorno:

Usando PowerShell o Windows 8 / Terminal ejecuta: 
```Powershell
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
```
Ahora añade el siguiente path a tu variable USER PATH para tener acceso al comando pyenv:

```Powershell
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```

Cierra y abre de nuevo la terminal y ejecuta: ```bash pyenv --version```

Si el valor que recibes es la versión de pyenv, continua con el siguiente bloque, si recibes un error sigue leyendo:

Si recibes el error "command not found" asegurate de que todas las variables de entorno se han añadido correctamente en:
```
PC → Properties → Advanced system settings → Advanced → Environment Variables... → PATH
```

Si recibes el error "command not found" y estas usando Visual Studio Code o otro IDE con terminal embebida reniciala y prueba de nuevo.

¿Sigues sin hacerlo funcionar? Entra en la página web de [pyenv-win](https://github.com/pyenv-win/pyenv-win#finish-the-installation)


## Instalando versiones de python
Listamos las versiones disponibles para instalar:
```bash
pyenv install --list
```
o filtrando directamente por la version que queremos
```bash

pyenv install --list | grep '3.9'

  3.9.0
  3.9-dev
  3.9.1
  3.9.2
  3.9.4
  3.9.5
  3.9.6
  3.9.7
  miniconda-3.9.1
  miniconda3-3.9.1
  miniconda3-3.9-4.9.2
  miniconda3-3.9-4.10.3
```
```bash
pyenv install 3.9.7

Downloading Python-3.9.7.tar.xz...
-> https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tar.xz
Installing Python-3.9.7...
...
...
Installed Python-3.9.7 to /Users/morphheus/.pyenv/versions/3.9.7
```
```bash
pyenv install 3.10.0

Downloading Python-3.10.0.tar.xz...
-> https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz
Installing Python-3.10.0...
...
...
Installed Python-3.10.0 to /Users/morphheus/.pyenv/versions/3.10.0
```
## Seleccionando versión de python global (para el sistema)
Esta versión, sera la que tome el sistema por defecto, si no queremos setearla, cogerá la versión de python que tuvieses instalada antes de usar pyenv.

Si queremos setear una versión:

```bash
pyenv global 3.9.7
```

Comprobamos que versión tenemos:

```bash
pyenv global

3.9.7
```
## Seleccionando versión de python local (proyecto)
Nos posicionamos en el proyecto donde queremos añadir una versión de Python diferente de la que usa nuestro sistema.

```bash
cd devZone/foo
pyenv local 3.10.0

ls -la

total 8
drwxr-xr-x@  3 morphheus  staff   96  4 nov 23:56 .
drwxr-xr-x@ 16 morphheus  staff  512  4 nov 23:56 ..
-rw-r--r--   1 morphheus  staff    7  4 nov 23:56 .python-version
```
Comprobamos que versión tenemos:

```bash
pyenv local 

3.10.0
```

## Uso de python

En función de la versión que hayamos elegido anteriormente, si ejecutamos python no saldrá algo parecido a lo siguiente:

```bash
Python 3.9.7 (default, Nov  4 2021, 23:49:47)
[Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

```bash
Python 3.10.0 (default, Nov  4 2021, 23:52:41) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Vamos a probar una de las nuevas características que trae Python 3.10:

Creamos un fichero con el siguiente contenido:

```bash
➜  foo cat handing_errors.py
expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
            38: 4, 39: 4, 45: 5, 46: 5, 47: 5, 48: 5, 49: 5, 54: 6,
```

Ahora seleccionamos como versión local la 3.9.7

```bash
pyenv local 3.9.7
```
Ejecutamos...

```bash
➜  foo python handing_errors.py
  File "/Users/morphheus/Documents/devZone/python/foo/handing_errors.py", line 3

    ^
SyntaxError: unexpected EOF while parsing
```

Y ahora seleccionamos como versión local la 3.10.0

```bash
pyenv local 3.10.0
```
Ejecutamos...

```bash
➜  foo python handing_errors.py
  File "/Users/morphheus/Documents/devZone/python/foo/handing_errors.py", line 1
    expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
               ^
SyntaxError: '{' was never closed
```