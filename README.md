# pup.py 🐶

pup.py helps neatly manage your python virtual environments and packages.

It serves as a wrapper of sorts over `pip`, implementing an `npm`-like CLI and `puppy.json` dependencies file.

Installing packages automatically creates a virtual environment (`.puppy/`) using `virtualenv`.

> **This tool is in alpha, and is very much a work in progress.**
>
> Namings and commands are likely to change before any formal release.

## Commands

### Install packages

```
$ pup install [<package>...] [-s|--save]
```

- Installs specified packages through `pip`.
- Creates a virtual environment in current directory.
- Without `package` args, installs all dependencies from `puppy.json`.
- If `--save`, package(s) are *also* pinned and added to `puppy.json`.

### Uninstall packages

```
$ pup uninstall <package>... [-s|--save]
```

- Uninstalls specified packages.
- If `--save`, package(s) are *also* removed from `puppy.json`.

### List packages

```
$ pup list
```

- Lists all installed packages in the virtual environment.
- Highlights the dependencies that are *also* specified in `puppy.json`.

### Run python from virtual environment

```
$ pup run <args>
```

- Runs `args` as a parameter to `python` as managed by the virtual environment (`.puppy/bin/python`).

### Destroy virtual environment

```
$ pup destroy
```

- Destroys the virtual environment (`.puppy/`) in the current directory.
