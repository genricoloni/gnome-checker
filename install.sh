pip install pyinstaller
pyinstaller --onefile gnome_check.py
sudo cp dist/gnome_check /bin/gnome_check
sudo chmod +x /bin/gnome_check
rm -rf build dist gnome_check.spec
echo "Installation complete. Run 'gnome-check' to check for GNOME desktop environment."