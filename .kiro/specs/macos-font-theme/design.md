# Design Document: macOS Font Theme

## Overview

This design document specifies the implementation details for adding macOS-specific font and theme options to AVA's theme system. The feature adds two distinct but complementary enhancements:

1. **macOS Font Option**: A new font choice that uses Apple's SF Pro Display font family with appropriate cross-platform fallbacks
2. **macOS Theme Preset**: A new color scheme inspired by macOS Big Sur/Ventura design language, featuring light gray backgrounds, subtle borders, and blue accents

Both options will be available on all platforms (not restricted to macOS devices) and will integrate seamlessly with AVA's existing theme system architecture.

## Architecture

The implementation follows AVA's existing theme system architecture:

1. **Static Configuration**: Font and theme definitions are stored in `static/js/theme.js` as JavaScript objects (FONT_MAP, THEMES)
2. **Early Loading**: Theme and font settings are applied in the early head script in `static/index.html` to prevent flash of unstyled content
3. **Runtime Management**: The theme.js module handles runtime theme switching and persistence
4. **Local Storage**: User preferences are persisted to localStorage and synced to the server

The macOS additions will follow these same patterns, requiring no architectural changes to the theme system.

## Components and Interfaces

### Component 1: FONT_MAP Update (theme.js)

**Location**: `static/js/theme.js` (lines 36-40)

**Current Structure**:
```javascript
const FONT_MAP = {
  mono: "'Fira Code', monospace",
  sans: "system-ui, -apple-system, 'Segoe UI', sans-serif",
  serif: "Georgia, 'Times New Roman', serif",
};
```

**Required Change**:
Add a new `macos` entry with the SF Pro font stack:

```javascript
const FONT_MAP = {
  mono: "'Fira Code', monospace",
  sans: "system-ui, -apple-system, 'Segoe UI', sans-serif",
  serif: "Georgia, 'Times New Roman', serif",
  macos: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', system-ui, sans-serif",
};
```

**Font Stack Rationale**:
- `-apple-system`: macOS native font API (includes SF Pro on modern macOS)
- `BlinkMacSystemFont`: Chrome on macOS fallback
- `'SF Pro Display'`: Explicit SF Pro if installed
- `'SF Pro Text'`: SF Pro variant for body text
- `system-ui`: Generic system font fallback
- `sans-serif`: Final generic fallback

### Component 2: THEMES Update (theme.js)

**Location**: `static/js/theme.js` (lines 11-30)

**Current Structure**: Object containing theme presets like `dark`, `light`, `midnight`, etc.

**Required Change**:
Add a new `macos` theme entry after the existing themes:

```javascript
export const THEMES = {
  dark:       { bg:'#282c34', fg:'#9cdef2', panel:'#111111', border:'#355a66', red:'#e06c75' },
  light:      { bg:'#f0ebe3', fg:'#5a5248', panel:'#faf6f0', border:'#d4cdc2', red:'#c47d5a' },
  midnight:   { bg:'#0d1117', fg:'#c9d1d9', panel:'#161b22', border:'#30363d', red:'#f85149' },
  paper:      { bg:'#faf8f5', fg:'#3b3836', panel:'#ffffff', border:'#d5d0c8', red:'#c5ac4a' },
  // ... existing themes ...
  macos:      { bg:'#f5f5f7', fg:'#1d1d1f', panel:'#ffffff', border:'#d2d2d7', red:'#007aff' },
};
```

**Color Scheme Details**:
- `bg: '#f5f5f7'`: Light gray background (macOS system background)
- `fg: '#1d1d1f'`: Near-black text (macOS label color)
- `panel: '#ffffff'`: White panels (macOS elevated surfaces)
- `border: '#d2d2d7'`: Subtle gray borders (macOS separator color)
- `red: '#007aff'`: Blue accent (macOS system blue for links/buttons)

These colors are derived from Apple's Human Interface Guidelines and match the macOS Big Sur/Ventura design system.

### Component 3: THEME_DEFAULT_PATTERN Update (theme.js)

**Location**: `static/js/theme.js` (lines 45-58)

**Current Structure**: Object mapping theme names to default background patterns

**Required Change**:
Add a `macos` entry with no pattern (clean appearance):

```javascript
const THEME_DEFAULT_PATTERN = {
  dark:       'none',
  light:      'dots',
  // ... existing themes ...
  macos:      'none',
};
```

**Rationale**: macOS design emphasizes clean, minimal backgrounds without decorative patterns.

### Component 4: THEME_DEFAULT_FROSTED Update (theme.js)

**Location**: `static/js/theme.js` (lines 71-73)

**Current Structure**: Object mapping theme names to frosted glass state (only lavender is currently enabled)

**Required Change**:
Add a `macos` entry with frosted glass enabled:

```javascript
const THEME_DEFAULT_FROSTED = {
  lavender:   true,
  macos:      true,
};
```

**Rationale**: Frosted glass (translucent blur) is a signature macOS visual effect used throughout the operating system for panels and windows.

### Component 5: Font Dropdown HTML (index.html)

**Location**: `static/index.html` (lines 571-576)

**Current Structure**:
```html
<select id="theme-font-select" class="theme-fd-select" aria-label="Font">
  <option value="mono">Monospace</option>
  <option value="sans">Sans-serif</option>
  <option value="serif">Serif</option>
</select>
```

**Required Change**:
Add a new option for macOS font:

```html
<select id="theme-font-select" class="theme-fd-select" aria-label="Font">
  <option value="mono">Monospace</option>
  <option value="sans">Sans-serif</option>
  <option value="serif">Serif</option>
  <option value="macos">macOS</option>
</select>
```

### Component 6: Early Head Script Font Map (index.html)

**Location**: `static/index.html` (line 89 in the early head script)

**Current Structure**:
```javascript
var fm = {mono:"'Fira Code', monospace",sans:"system-ui, -apple-system, 'Segoe UI', sans-serif",serif:"Georgia, 'Times New Roman', serif"};
```

**Required Change**:
Add the macOS font stack to match the FONT_MAP in theme.js:

```javascript
var fm = {
  mono:"'Fira Code', monospace",
  sans:"system-ui, -apple-system, 'Segoe UI', sans-serif",
  serif:"Georgia, 'Times New Roman', serif",
  macos:"-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', system-ui, sans-serif"
};
```

**Critical Note**: The font map in the early head script MUST match the FONT_MAP in theme.js exactly to prevent font flickering on page load.

## Data Models

### Theme Object Structure

The theme system uses the following data model for stored preferences:

```javascript
{
  name: string,              // Theme name (e.g., "macos")
  colors: {
    bg: string,              // Hex color for background
    fg: string,              // Hex color for foreground text
    panel: string,           // Hex color for panel backgrounds
    border: string,          // Hex color for borders
    red: string,             // Hex color for accent/links/buttons
    advanced?: {             // Optional advanced color overrides
      userBubbleBg: string,
      aiBubbleBg: string,
      // ... other advanced properties
    }
  },
  font?: string,             // Optional font identifier (e.g., "macos")
  density?: string,          // Optional density setting
  bgPattern?: string,        // Optional background pattern
  bgEffectColor?: string,    // Optional effect color override
  bgEffectIntensity?: number,// Optional intensity (0-1)
  bgEffectSize?: number,     // Optional size multiplier
  frosted?: boolean          // Optional frosted glass state
}
```

### Font Map Data Model

```javascript
{
  [fontId: string]: string   // Maps font ID to CSS font-family declaration
}
```

Example:
```javascript
{
  "mono": "'Fira Code', monospace",
  "macos": "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', system-ui, sans-serif"
}
```

## Error Handling

### Font Fallback Chain

If SF Pro fonts are not available (non-Apple platforms or older macOS versions):
1. `-apple-system` and `BlinkMacSystemFont` will resolve to the system's default UI font
2. `system-ui` provides a generic system font
3. `sans-serif` ensures a readable font is always available

No error handling code is needed—CSS font fallback is automatic.

### Theme Loading Errors

Existing error handling in the early head script (lines 17-103 in index.html) catches and ignores theme loading errors:

```javascript
try {
  var t = JSON.parse(localStorage.getItem('ava-theme'));
  // ... theme application logic ...
} catch(e){}
```

This ensures the page loads with default styling even if theme data is corrupted.

### Missing Theme Properties

The theme system provides defaults for missing properties:
- If `THEME_DEFAULT_PATTERN` lacks a theme entry, pattern defaults to 'none'
- If `THEME_DEFAULT_FROSTED` lacks a theme entry, frosted defaults to false
- If `THEME_DEFAULT_INTENSITY` lacks a theme entry, intensity defaults to 1.0

## Testing Strategy

### Unit Testing

Since this feature involves configuration changes rather than complex logic, unit tests should focus on:

1. **Font Map Integrity**: Verify that FONT_MAP contains valid CSS font-family declarations
   - Test that each font stack is a valid CSS string
   - Test that font IDs match between theme.js and index.html

2. **Theme Color Validation**: Verify that theme colors are valid hex codes
   - Test that all macOS theme colors are 6-digit hex codes
   - Test that colors meet contrast requirements for accessibility

3. **Default Configuration Consistency**: Verify that default settings are defined
   - Test that THEME_DEFAULT_PATTERN has a 'macos' entry
   - Test that THEME_DEFAULT_FROSTED has a 'macos' entry

4. **HTML Dropdown Consistency**: Verify that font dropdown options match FONT_MAP keys
   - Test that each option value corresponds to a FONT_MAP key

### Integration Testing

Integration tests should verify end-to-end functionality:

1. **Theme Selection Flow**:
   - Test selecting macOS theme from the theme popup
   - Verify colors are applied to CSS variables
   - Verify localStorage is updated
   - Verify server sync API is called

2. **Font Selection Flow**:
   - Test selecting macOS font from the font dropdown
   - Verify --font-family CSS variable is updated
   - Verify localStorage is updated

3. **Early Loading**:
   - Test that macOS theme colors appear on initial page load (no FOUC)
   - Test that macOS font applies before DOMContentLoaded

4. **Cross-Browser Compatibility**:
   - Test font rendering on Chrome (should use BlinkMacSystemFont on macOS)
   - Test font rendering on Safari (should use -apple-system)
   - Test font rendering on Firefox (should use system-ui fallback)
   - Test on Windows/Linux (should gracefully fall back to system fonts)

5. **Frosted Glass Effect**:
   - Test that macOS theme enables frosted glass by default
   - Verify that body.theme-frosted class is applied
   - Test visual appearance of panels with translucent blur

### Manual Testing Checklist

- [ ] Select macOS theme from theme popup
- [ ] Verify colors match macOS design system
- [ ] Select macOS font from font dropdown
- [ ] Verify font renders as SF Pro on macOS devices
- [ ] Verify font falls back gracefully on non-macOS devices
- [ ] Verify frosted glass effect is enabled by default
- [ ] Test with background patterns disabled
- [ ] Reload page and verify settings persist
- [ ] Test syntax highlighting colors are generated correctly
- [ ] Test in Safari on macOS
- [ ] Test in Chrome on macOS
- [ ] Test in Chrome on Windows
- [ ] Test in Firefox on Linux

### Accessibility Testing

- [ ] Verify macOS theme meets WCAG AA contrast requirements (4.5:1 for normal text)
- [ ] Test with screen reader to ensure font dropdown is properly labeled
- [ ] Verify frosted glass effect doesn't reduce readability below accessibility standards

## Implementation Notes

### Order of Operations

To prevent visual artifacts, changes must be applied in this order:

1. Update `FONT_MAP` in theme.js
2. Update `THEMES` in theme.js
3. Update `THEME_DEFAULT_PATTERN` in theme.js
4. Update `THEME_DEFAULT_FROSTED` in theme.js
5. Update font dropdown HTML in index.html
6. Update early head script font map in index.html

### Testing During Development

After making changes, test by:

1. Opening browser DevTools
2. Clearing localStorage: `localStorage.clear()`
3. Hard refreshing the page (Ctrl+Shift+R / Cmd+Shift+R)
4. Selecting macOS theme and font
5. Refreshing to verify persistence

### SF Pro Font Availability

SF Pro is NOT bundled with AVA—it relies on system fonts. On macOS:
- macOS 10.11+: SF Pro is the system UI font via `-apple-system`
- macOS 10.10 and earlier: Falls back to Helvetica Neue via system-ui

On non-macOS platforms:
- Windows: Falls back to Segoe UI via system-ui
- Linux: Falls back to default sans-serif (usually Liberation Sans or DejaVu Sans)

### Color Derivation

The theme system automatically derives syntax highlighting colors from the base colors using HSL color space transformations (see `deriveSyntaxColors` function in theme.js, lines 161-179). The macOS theme's colors will produce:
- Keyword colors: Purple-blue tones
- String colors: Orange-amber tones
- Comment colors: Muted gray
- Function colors: Blue tones

These are calculated automatically—no manual syntax color definition is needed.

## Alternatives Considered

### Alternative 1: Bundle SF Pro Font Files

**Considered**: Including SF Pro .woff2 files in `static/fonts/`

**Rejected**: Apple's font license prohibits redistribution. Using system fonts via `-apple-system` is the only legal and officially supported approach.

### Alternative 2: Separate Light/Dark macOS Themes

**Considered**: Creating `macos-light` and `macos-dark` theme presets

**Rejected**: The single light macOS theme is sufficient for v1. If demand exists, a dark variant can be added in a future iteration without affecting this implementation.

### Alternative 3: Auto-Detect Platform

**Considered**: Automatically applying the macOS theme/font on macOS devices

**Rejected**: Users should have explicit control over their theme choices. Auto-detection would be surprising behavior and harder to test/debug.

## Future Enhancements

Potential improvements for future iterations:

1. **macOS Dark Theme**: A dark variant using macOS dark mode colors
2. **Dynamic Color Adjustment**: Respond to system dark/light mode changes
3. **SF Pro Weight Variants**: Support for SF Pro Text, Display, and Rounded variants
4. **Advanced Color Customization**: Allow users to customize the blue accent color
5. **Platform-Specific Defaults**: Suggest macOS theme on first load for macOS users (with opt-out)
