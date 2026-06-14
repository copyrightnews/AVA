#!/usr/bin/env node
/**
 * Quick Theme Applicator for AVA
 * Usage: node apply-theme.js [light|dark]
 * 
 * This script generates a URL you can visit to apply the macOS theme
 */

const theme = process.argv[2] || 'light';

if (!['light', 'dark'].includes(theme)) {
  console.error('❌ Invalid theme. Use "light" or "dark"');
  process.exit(1);
}

const themeData = theme === 'light' ? {
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
} : {
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
};

console.log('\n🎨 macOS Theme Applicator\n');
console.log(`Theme: macOS ${theme === 'light' ? 'Light' : 'Dark'}`);
console.log('\n📋 Copy and paste this into your browser console:\n');
console.log(`localStorage.setItem('ava-theme', '${JSON.stringify(themeData)}'); location.reload();`);
console.log('\n✨ Or visit: http://localhost:5000/static/apply-macos-theme.html\n');
