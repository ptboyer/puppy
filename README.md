# pup.py 🐶

pup.py helps neatly manage your Python virtual environments and packages.

It serves as a wrapper of sorts over `pip`, implementing an `npm`-like CLI and `package.json` dependency file, `puppy.json`.

Install packages automatically creates a virtual environment using `virtualenv`.

------

**This tool is in an alpha, and is very much a work in progress.**

Namings and commands are likely to change before any formal release.

## Commands

### Install packages

```shell
$ pup install [<package>...] [-s|--save]
```

- Creates a virtual environment in current directory.
- Installs specified packages.
- Without `package` args installs all dependencies from `puppy.json`.
- If `--save`, package(s) are also pinned and added to the `puppy.json`.

### Uninstall packages

```shell
$ pup uninstall <package>... [-s|--save]
```

- Uninstalls specified packages.
- If `--save`, package(s) are also removed from the pupfile.

### List packages

```shell
$ pup list
```

- Lists all installed packages in the virtual environment.
- Highlights the dependencies specified in the pupfile.

### Run python from virtual environment

```shell
$ pup run <args>
```

- Runs `args` as a parameter to `python` as managed by the virtual environment.

### Destroy virtual environment

```shell
$ pup destroy
```

- Destroys the virtual environment (`./.puppy`) in the current directory.