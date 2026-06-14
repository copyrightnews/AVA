# 🎨 Apply macOS Theme to AVA

You now have the authentic SF Pro Display fonts and macOS themes configured in your AVA application. Here are **three ways** to apply them:

---

## Method 1: Use the Theme Applicator Page ⭐ EASIEST

1. Start your AVA server (if not running)
2. Navigate to: **http://localhost:5000/static/apply-macos-theme.html**
3. Click either:
   - **Apply macOS Light Theme** - for the light appearance
   - **Apply macOS Dark Theme** - for the dark appearance
4. You'll be automatically redirected to AVA with the theme applied!

---

## Method 2: Browser Console (Quick)

1. Open AVA in your browser: **http://localhost:5000**
2. Press **F12** to open Developer Tools
3. Go to the **Console** tab
4. Paste one of these commands:

### For macOS Light Theme:
```javascript
localStorage.setItem('ava-theme', JSON.stringify({
  name: 'macos-light',
  colors: {
    bg: '#f5f5f7',
    fg: '#1d1d1f',
    panel: '#ffffff',
    border: '#d2d2d7',
    red: '#007aff'
  },
  font: 'macos',
  bgPattern: 'none',
  frosted: true,
  density: 'comfortable'
}));
location.reload();
```

### For macOS Dark Theme:
```javascript
localStorage.setItem('ava-theme', JSON.stringify({
  name: 'macos-dark',
  colors: {
    bg: '#1e1e1e',
    fg: '#ffffff',
    panel: '#2d2d2d',
    border: '#3a3a3c',
    red: '#0a84ff'
  },
  font: 'macos',
  bgPattern: 'none',
  frosted: true,
  density: 'comfortable'
}));
location.reload();
```

5. Press **Enter** - the page will reload with the macOS theme applied!

---

## Method 3: Through AVA UI (Manual)

1. Open AVA in your browser
2. Click the **⚙️ Settings** or **Theme** button
3. In the theme picker:
   - Select **"macOS"** for light theme OR **"macOS dark"** for dark theme
4. In the font dropdown:
   - Select **"macOS"**
5. Make sure **Frosted Glass** effect is enabled
6. The theme will be automatically saved!

---

## ✅ What You'll Get

Once applied, you'll see:

### 🎨 Visual Changes:
- **Authentic SF Pro Display font** globally (the real macOS system font)
- **macOS color palette** - light gray (#f5f5f7) or dark gray (#1e1e1e) backgrounds
- **Blue accent colors** - #007aff (light) or #0a84ff (dark)
- **Frosted glass effects** on panels and modals
- **Clean, minimal appearance** matching macOS Big Sur/Monterey/Sonoma

### 📝 Font Details:
- Primary: SF Pro Display (Regular, Medium, Semibold, Bold)
- Loaded from: `/static/fonts/sf-pro/`
- Fallbacks: -apple-system, BlinkMacSystemFont, system-ui

---

## 🔧 Troubleshooting

### Fonts Not Loading?
1. Check browser console for errors (F12)
2. Verify font files exist: `/static/fonts/sf-pro/SF-Pro-Display-*.otf`
3. Hard refresh: **Ctrl+Shift+R** (Windows) or **Cmd+Shift+R** (Mac)

### Theme Not Applying?
1. Clear localStorage: Open console and run `localStorage.clear()`
2. Hard refresh the page
3. Reapply the theme using Method 1 or 2

### Still Issues?
- Check the browser's Network tab to see if fonts are loading (200 status)
- Ensure your AVA server is running
- Try a different browser to rule out caching issues

---

## 🎯 Quick Start Command

If you just want to get started quickly:

1. **Start AVA**: `python app.py` (in the AVA directory)
2. **Open**: http://localhost:5000/static/apply-macos-theme.html
3. **Click**: "Apply macOS Light Theme" or "Apply macOS Dark Theme"
4. **Done!** 🎉

---

## 📸 What to Expect

The authentic macOS theme will give you:
- The same font rendering as macOS system apps
- Blue accent colors (AVA's signature color)
- Subtle frosted glass panels
- Clean, minimal spacing and borders
- Professional macOS-style appearance

Enjoy your authentic macOS-styled AVA! 🍎✨
