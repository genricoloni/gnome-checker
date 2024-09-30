# gnome-checker

Check extensions compatibility with your gnome-shell version with ease!

## usage

```bash
python ./gnome-checker.py [gnome-shell-version]
```

If you don't provide the gnome-shell version, the script will use the version installed on your system.

An example of the output:

```bash
$ python ./gnome-checker.py 46
Gnome version: 46.x
Incompatible extensions:
 gestureImprovements@gestures 
 expandable-notifications@kaan.g.inam.org 
 cpudots@kdevmen.gmail.com 
 hanabi-extension@jeffshee.github.io 
 cpufreq@konkor 
```

## installation

If you want to add the script to your PATH, you can run `install.sh`. Note that you may need to add the `execute` permission to that file before running it.

```bash
chmod +x ./install.sh #if needed
./install.sh
```

It uses `pyinstaller` to create a binary file and move it to `/usr/local/bin`. Since `sudo` is required to move the file into `$PATH`, you'll be prompted to enter your password. After that, you can run the script from anywhere in your system.