# KBL

Kai's BootLoaders are different ways of loading into a shell / program automatically. Some of these methods are used by multiple shells, and have their own unique features and uniform.

## No Loader

No loader is the simplest approach to a shell, have the user start a program which immediately throws them into a shell. No pre-computing, booting, or anything of the sort required. This method is the fastest and most effective for quick systems that don't need much setup/requirement. The main shell engines which utilize this method are Kux (Somewhat, see below) and KTerminal.

A no-loader would look something like this:

```
$ ./prog
Welcome to the shell
> 
```

> NOTE: Kux is not, technically, using a NL, it uses
> something known as the NLPM (No-Loader Preprocessing Manager) which is like a No-Loader, but is
> mainly backend to keep user friendliness.

## NLPM (No-Loader W/ Preprocessing Management)

The NLPM is similar to the [No-Loader](#no-loader) except in the backend, it contains a setup to create a program to startup on program launch. Kind of like a pre-setup into the No-Loader which aids in user friendliness and allows the user to figure out problems when it starts, instead of being thrown right into the water. This is mainly used by Kux, Dax, ModernKux, and Kux, and Kuxel.

A system that utilizes the NLPM would look something like this:

```
# first time loading the system
$ ./prog
Welcome to setup
> 

# second time running the system
$ ./prog
Welcome to shell
> 
```

## TSWCBT (The Snarwin Customizable Boot Table)

Snarwin contains a very, *very* unique boot system, in the sense it allows the user to have **full control** over the system that they are running, unlike NL/NLPM, TSWCBT is mainly for many differently structured systems, and it is fast and very parallel, making Snarwin a very fun option for many people who enjoy getting their hands dirty. TSWCBT allows users to even have backward compatibility with Kux, ModernKux and Kuxel, if you really tried.

Snarwin is the only known system that utilizes this boot manager.

```
$ ./prog
choose your system:
* 0x00 - Recovery
* 0x01 - Fun OS
* 0x02 - SaSH
* 0x03 - DSH (Kux Default Shell)
```

## FKSAS (FreeKSD Secure Account System)

The FKSAS is an account-based, send-and-recieve system that passes around codes to be able to log a user into the shell. Unlike all the others, this system is unique because it allows the user to run a system securely, and has very minimal room for error.

The account system is one of the main reasons that FreeKSD has succeeded in the Operation System industry, due to the fact it's lenient, parallel, and lightweight. It works off of multiple files and different codes for each of them. FreeKSD is one of the most chosen Operation Shells when it comes to stability.

As of recent times, GTerminal has finally taken upon this SAS and they now have implemented accounts into the latest versions of GTerminal.

```
$ ./prog
logging you in...
type password: . . .
sending request to login
logged in!
>
```
