# 📘 Emergency Response System Documentation

## Getting Started

This guide helps you deploy and use the Emergency Response System across different platforms securely and efficiently.

---

## 🔧 Installation (Linux/macOS/Windows)

```bash
pip install -r requirements.txt
python3 main.py
```

## 🧪 Running Tests

```bash
pytest tests/
```

## 🖥️ GUI vs CLI

- Use CLI by default.
- GUI toggle will be enabled by setting `GUI_MODE=True` in `.env`.

## 📦 Packaging

Use the scripts in `ci_cd/`:
- `build_deb.sh`
- `build_exe.bat`
- `build_appimage.sh`

## 🔐 Security Notes

- All models are run locally
- No external API calls
- `.env` for configuration and secrets

For detailed deployment steps, see `secure_deployment.md`
