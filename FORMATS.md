# Kai's FileSystem Formats

KSYSFS is the name of Kai's FileSystem Formats, essentially they help manage the system and it's programs in a nice manner, and there are different types of filesystems, all with their own benefits.

## Unprotected VS Protected

A protected filesystem contains files that ensure that the directories do not allow the user to make
any serious harmful operations on them. Systems such as GTerminal and KTerminal use this system. Kux, FreeKSD, Dax, and
other systems do not.

Here is an example of a protected filesystem:

```
example-of-protected-system/
├── main-system
└── system-files
    ├── important-things
    └── .NO_ACCESS # This removes access so you can do important things without risk
```

An unprotected filesystem would remove the .NO_ACCESS file, or similar.

```
example-of-unprotected-system/
├── main-system
└── system-files
    ├── important-things # important things run, but can be interveined and cause serious damage!
```

## Formats

### Unix 86

Unix 86 is a reincarnation of the original Unix filesystem format. At it's core it contains a `USR` directory, and a `USR/BIN` directory. Systems that fully implement this filesystem are Kux, and DAX. Although, DAX does not use Unix 86, instead it uses Unix 86 (Reduced)

```
unix-86-format/
└── usr
    ├── bin
    ├── games
    └── lib . . .
```

### Unix 86 Reduced

Unix 86 Reduced is similar to the Unix 86 format, in that it contains a USR directory, but no LIB, or anything extra. The main use of this format is to reduce clutter when the system looks for / cleans any files. The main system that uses this is DAX. It essentially pioneered the U86R format.

```
unix-86-redux/
├── ext
└── usr
    ├── bin
    └── src
```

### Free System 64

FS64 is a basic format utilized by GTerminal which in essence, is more user friendly than U86, it contains a "system" directory which is basically a replacement to the "usr" directory, and that contains "scripts", which are run by a shell.

```
system/
├── help
│   ├── fpc.1
│   └── src
│       └── fpc.md
├── scripts
│   ├── fpc.py
│   ├── hello.py
│   ├── help.py
│   └── pkg.py
└── system.cfg
```

### FSU86 (Free System + Unix 86) Hybrid

The FSU86 is the name for the hybrid filesystem utilized by KTerminal and FreeKSD. It contains a USR directory, and also contains a SYSTEM directory, as they both work together to reduce clutter and improve sorting. KTerminal really pioneered this filesystem, with it's failed releases of Kefi, it paved the way for this filesystem to find some meaning, which is now used by FreeKSD in modern times.

```
example-of-fsu86/
├── system
│   ├── help
│   ├── info
│   └── scripts
└── usr
    ├── bin
    ├── games
    └── src
```