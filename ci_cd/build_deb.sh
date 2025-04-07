#!/bin/bash
set -e

APP_NAME="emergency-response-system"
VERSION="1.0.0"
ARCH="amd64"
BUILD_DIR="./build"
DEB_DIR="${BUILD_DIR}/${APP_NAME}_${VERSION}_${ARCH}"

# Cleanup
rm -rf ${BUILD_DIR}
mkdir -p ${DEB_DIR}/usr/local/bin

# Copy application
cp main.py ${DEB_DIR}/usr/local/bin/${APP_NAME}
chmod +x ${DEB_DIR}/usr/local/bin/${APP_NAME}

# Create control file
mkdir -p ${DEB_DIR}/DEBIAN
cat <<EOF > ${DEB_DIR}/DEBIAN/control
Package: ${APP_NAME}
Version: ${VERSION}
Section: base
Priority: optional
Architecture: ${ARCH}
Maintainer: ParaCryptid
Description: AI-enabled Emergency Response System
EOF

# Build .deb package
dpkg-deb --build ${DEB_DIR}
