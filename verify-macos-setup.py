#!/usr/bin/env python3
"""
Verification script for macOS theme setup
Checks that all required files and configurations are in place
"""

import os
import sys
import json
from pathlib import Path

# Ensure standard output can print UTF-8 emojis on Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def check_file(path, name):
    """Check if a file exists"""
    exists = os.path.exists(path)
    status = "✅" if exists else "❌"
    print(f"{status} {name}")
    return exists

def check_font_in_file(file_path, search_term):
    """Check if a file contains the macOS font configuration"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return search_term in content
    except:
        return False

def main():
    print("\n" + "="*60)
    print("🔍 macOS Theme Setup Verification")
    print("="*60 + "\n")
    
    base_dir = Path(__file__).parent
    all_good = True
    
    # Check font files
    print("📁 Font Files:")
    font_dir = base_dir / "static" / "fonts" / "sf-pro"
    fonts = [
        "SF-Pro-Display-Regular.otf",
        "SF-Pro-Display-Medium.otf",
        "SF-Pro-Display-Semibold.otf",
        "SF-Pro-Display-Bold.otf"
    ]
    
    for font in fonts:
        font_path = font_dir / font
        if not check_file(font_path, f"  {font}"):
            all_good = False
    
    # Check CSS file
    print("\n📄 CSS Configuration:")
    css_path = base_dir / "static" / "style.css"
    if check_file(css_path, "  style.css exists"):
        has_font_face = check_font_in_file(css_path, "font-family: 'SF Pro Display'")
        status = "✅" if has_font_face else "❌"
        print(f"{status}   SF Pro Display @font-face declarations")
        if not has_font_face:
            all_good = False
    else:
        all_good = False
    
    # Check theme.js
    print("\n🎨 Theme Configuration:")
    theme_js_path = base_dir / "static" / "js" / "theme.js"
    if check_file(theme_js_path, "  theme.js exists"):
        has_macos_font = check_font_in_file(theme_js_path, "macos: \"'SF Pro Display'")
        has_macos_light = check_font_in_file(theme_js_path, "'macos-light'")
        has_macos_dark = check_font_in_file(theme_js_path, "'macos-dark'")
        
        status = "✅" if has_macos_font else "❌"
        print(f"{status}   macOS font in FONT_MAP")
        if not has_macos_font:
            all_good = False
        
        status = "✅" if has_macos_light else "❌"
        print(f"{status}   macOS light theme configured")
        if not has_macos_light:
            all_good = False
            
        status = "✅" if has_macos_dark else "❌"
        print(f"{status}   macOS dark theme configured")
        if not has_macos_dark:
            all_good = False
    else:
        all_good = False
    
    # Check index.html
    print("\n📝 HTML Configuration:")
    index_path = base_dir / "static" / "index.html"
    if check_file(index_path, "  index.html exists"):
        has_early_font = check_font_in_file(index_path, "macos:\"'SF Pro Display'")
        status = "✅" if has_early_font else "❌"
        print(f"{status}   Early head script font map")
        if not has_early_font:
            all_good = False
    else:
        all_good = False
    
    # Check applicator files
    print("\n🚀 Theme Applicator Tools:")
    check_file(base_dir / "static" / "quick-apply.html", "  quick-apply.html")
    check_file(base_dir / "static" / "apply-macos-theme.html", "  apply-macos-theme.html")
    check_file(base_dir / "apply_macos_theme.py", "  apply_macos_theme.py")
    check_file(base_dir / "APPLY-MACOS-THEME.md", "  APPLY-MACOS-THEME.md")
    check_file(base_dir / "MACOS-THEME-SETUP-COMPLETE.md", "  MACOS-THEME-SETUP-COMPLETE.md")
    
    # Final summary
    print("\n" + "="*60)
    if all_good:
        print("✅ ALL CHECKS PASSED!")
        print("="*60)
        print("\n🎉 Your macOS theme is ready to use!")
        print("\n📍 Next Steps:")
        print("   1. Start AVA: python app.py")
        print("   2. Visit: http://localhost:5000/static/quick-apply.html")
        print("   3. Click Light or Dark theme")
        print("   4. Enjoy! 🚀\n")
    else:
        print("⚠️  SOME CHECKS FAILED")
        print("="*60)
        print("\nPlease review the items marked with ❌ above.\n")
    
    return 0 if all_good else 1

if __name__ == "__main__":
    exit(main())
