# Implementation Plan: macOS Font Theme

## Overview

This implementation adds macOS-specific font and theme options to AVA's theme system. The changes are purely configurational—adding new entries to existing data structures in `static/js/theme.js` and `static/index.html`. No new code logic is required, only additions to configuration objects and HTML options.

The implementation follows the order specified in the design document to prevent visual artifacts during development.

## Tasks

- [x] 1. Add macOS font to FONT_MAP in theme.js
  - Open `static/js/theme.js`
  - Locate the `FONT_MAP` object (around lines 36-40)
  - Add a new `macos` entry with the SF Pro font stack: `macos: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', system-ui, sans-serif"`
  - Ensure the font stack matches the specification exactly (including quote types and comma spacing)
  - _Requirements: 1.1, 1.2, 4.1, 4.2, 4.3, 4.4, 4.5_

- [x] 2. Add macOS theme preset to THEMES in theme.js
  - Open `static/js/theme.js` (if not already open)
  - Locate the `THEMES` object (around lines 11-30)
  - Add a new `macos` entry after existing themes with colors: `{ bg:'#f5f5f7', fg:'#1d1d1f', panel:'#ffffff', border:'#d2d2d7', red:'#007aff' }`
  - Verify color values are valid 6-digit hex codes
  - _Requirements: 2.1, 2.2, 2.3_

- [x] 3. Add macOS entry to THEME_DEFAULT_PATTERN in theme.js
  - Open `static/js/theme.js` (if not already open)
  - Locate the `THEME_DEFAULT_PATTERN` object (around lines 45-58)
  - Add a new entry: `macos: 'none'`
  - Ensure consistent formatting with existing entries
  - _Requirements: 3.1, 3.3_

- [x] 4. Add macOS entry to THEME_DEFAULT_FROSTED in theme.js
  - Open `static/js/theme.js` (if not already open)
  - Locate the `THEME_DEFAULT_FROSTED` object (around lines 71-73)
  - Add a new entry: `macos: true`
  - Ensure consistent formatting with existing entries
  - _Requirements: 3.2, 3.4_

- [x] 5. Add macOS font option to dropdown in index.html
  - Open `static/index.html`
  - Locate the font select element `#theme-font-select` (around lines 571-576)
  - Add a new option element: `<option value="macos">macOS</option>`
  - Place it after the existing serif option
  - Ensure the value attribute matches the FONT_MAP key exactly ("macos")
  - _Requirements: 1.3, 1.4, 1.5_

- [x] 6. Update early head script font map in index.html
  - Open `static/index.html` (if not already open)
  - Locate the early head script (around line 89)
  - Find the `var fm = {...}` font map declaration
  - Add the macOS font stack to match FONT_MAP: `macos:"-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', system-ui, sans-serif"`
  - **CRITICAL**: Ensure this matches the theme.js FONT_MAP exactly to prevent font flickering
  - _Requirements: 1.1, 1.2, 4.1, 4.2, 4.3, 4.4, 4.5_

- [x] 7. Verify implementation
  - Clear browser localStorage: `localStorage.clear()`
  - Hard refresh the page (Ctrl+Shift+R / Cmd+Shift+R)
  - Open theme settings popup
  - Verify "macOS" appears in the theme preset list
  - Select the macOS theme
  - Verify colors are applied (light gray background, blue accents)
  - Verify frosted glass effect is enabled
  - Open font dropdown in theme settings
  - Verify "macOS" appears as a font option
  - Select the macOS font
  - Verify font changes (should appear as SF Pro on macOS, system default elsewhere)
  - Refresh the page
  - Verify theme and font selections persist
  - _Requirements: All_

- [x] 8. Checkpoint - Ensure changes work correctly
  - Test theme selection persists across page reloads
  - Test font selection persists across page reloads
  - Verify no console errors appear when selecting macOS options
  - Verify the early head script prevents flash of unstyled content (FOUC)
  - Ask the user if questions arise

## Notes

- All changes are configuration additions—no new functions or complex logic required
- The order of operations (tasks 1-6) is important to prevent visual artifacts
- Font fallback is automatic via CSS—no error handling code needed
- The macOS theme automatically derives syntax highlighting colors via existing `deriveSyntaxColors` function
- SF Pro fonts are not bundled—they rely on system fonts via `-apple-system` (legal requirement)
- Both macOS theme and font work on all platforms, not restricted to macOS devices
- Testing should include verification on multiple browsers and platforms
