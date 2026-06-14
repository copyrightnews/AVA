#!/usr/bin/env python3
"""
Quick macOS Theme Applicator for AVA
Usage: python apply_macos_theme.py [light|dark]

This script opens your browser and applies the macOS theme automatically.
"""

import sys
import webbrowser
import json
from urllib.parse import quote

def apply_theme(theme_type='light'):
    """Apply macOS theme by opening browser with pre-filled localStorage"""
    
    if theme_type not in ['light', 'dark']:
        print("❌ Invalid theme. Use 'light' or 'dark'")
        sys.exit(1)
    
    theme_data = {
        'light': {
            'name': 'macos-light',
            'colors': {
                'bg': '#f5f5f7',
                'fg': '#1d1d1f',
                'panel': '#ffffff',
                'border': '#d2d2d7',
                'red': '#007aff'
            },
            'font': 'macos',
            'bgPattern': 'none',
            'frosted': True,
            'density': 'comfortable'
        },
        'dark': {
            'name': 'macos-dark',
            'colors': {
                'bg': '#1e1e1e',
                'fg': '#ffffff',
                'panel': '#2d2d2d',
                'border': '#3a3a3c',
                'red': '#0a84ff'
            },
            'font': 'macos',
            'bgPattern': 'none',
            'frosted': True,
            'density': 'comfortable'
        }
    }
    
    selected_theme = theme_data[theme_type]
    
    print(f"\n🎨 Applying macOS {theme_type.capitalize()} Theme...\n")
    
    # Method 1: Open the theme applicator page
    url = "http://localhost:5000/static/apply-macos-theme.html"
    
    print(f"✨ Opening: {url}")
    print(f"\nClick 'Apply macOS {theme_type.capitalize()} Theme' button\n")
    
    try:
        webbrowser.open(url)
        print("✅ Browser opened successfully!")
    except Exception as e:
        print(f"❌ Could not open browser: {e}")
        print("\n📋 Alternative: Copy this command and paste in browser console:")
        print(f"\nlocalStorage.setItem('ava-theme', '{json.dumps(selected_theme)}'); location.reload();")
    
    print("\n" + "="*60)
    print("Manual Steps:")
    print("="*60)
    print("1. Open: http://localhost:5000/static/apply-macos-theme.html")
    print(f"2. Click: 'Apply macOS {theme_type.capitalize()} Theme'")
    print("3. Wait for redirect to AVA")
    print("4. Enjoy your macOS theme! 🎉\n")

if __name__ == "__main__":
    theme = sys.argv[1] if len(sys.argv) > 1 else 'light'
    apply_theme(theme)
