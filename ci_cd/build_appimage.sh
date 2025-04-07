#!/bin/bash
set -e

APP=emergency-response-system
VERSION=1.0.0

# Ensure AppImage tool is installed
if ! command -v appimagetool &> /dev/null; then
    echo "appimagetool not found. Please install it first."
    exit 1
fi

# Prepare AppDir structure
mkdir -p AppDir/usr/bin
cp main.py AppDir/usr/bin/${APP}
chmod +x AppDir/usr/bin/${APP}

# Create AppRun script
cat <<EOF > AppDir/AppRun
#!/bin/bash
exec /usr/bin/${APP}
EOF
chmod +x AppDir/AppRun

# Create desktop entry
mkdir -p AppDir/usr/share/applications
cat <<EOF > AppDir/${APP}.desktop
[Desktop Entry]
Name=Emergency Response System
Exec=${APP}
Icon=emergency
Type=Application
Categories=Utility;
EOF

# Optional: add an icon to AppDir/usr/share/icons

# Build AppImage
appimagetool AppDir
