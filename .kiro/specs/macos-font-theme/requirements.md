# Requirements Document

## Introduction

This feature enhances the AVA theme system by adding macOS-specific font and theme options. The macOS font option will provide users with Apple's SF Pro font family (with appropriate fallbacks), and the macOS theme preset will provide a color scheme inspired by macOS design aesthetics.

## Glossary

- **Theme_System**: The AVA theme customization system that manages color schemes, fonts, and visual preferences
- **Font_Dropdown**: The UI dropdown control in the theme settings that allows users to select font families
- **Theme_Preset**: A predefined color scheme in the THEMES object that includes bg, fg, panel, border, and red colors
- **FONT_MAP**: The JavaScript object that maps font identifiers to CSS font-family declarations
- **SF_Pro**: Apple's San Francisco Pro font family used across macOS and iOS interfaces
- **Theme_Preset_Dropdown**: The UI dropdown control that allows users to select from available theme presets

## Requirements

### Requirement 1: macOS Font Option

**User Story:** As a user, I want to select a macOS-style font, so that I can experience a design aesthetic consistent with Apple platforms.

#### Acceptance Criteria

1. THE Theme_System SHALL include a "macos" font option in the FONT_MAP
2. THE "macos" font stack SHALL prioritize SF Pro Display with appropriate fallbacks
3. WHEN a user selects the macOS font from the Font_Dropdown, THE Theme_System SHALL apply the SF Pro font stack to the interface
4. THE macOS font option SHALL be available on all platforms (not restricted to macOS only)
5. THE Font_Dropdown SHALL display "macOS" as the label for the new font option

### Requirement 2: macOS Theme Preset

**User Story:** As a user, I want to select a macOS-style theme, so that I can have a color scheme that matches macOS design aesthetics.

#### Acceptance Criteria

1. THE Theme_System SHALL include a "macos" theme preset in the THEMES object
2. THE macOS theme SHALL define colors for bg, fg, panel, border, and red properties
3. THE macOS theme colors SHALL be inspired by macOS Big Sur and later design language (light gray backgrounds, subtle borders, blue accents)
4. THE macOS theme SHALL be available on all platforms (not restricted to macOS only)
5. WHEN a user selects the macOS theme from the Theme_Preset_Dropdown, THE Theme_System SHALL apply the macOS color scheme to the interface
6. THE Theme_Preset_Dropdown SHALL display "macOS" as an option in the theme list

### Requirement 3: Visual Consistency

**User Story:** As a user, I want the macOS theme to have appropriate default settings, so that it provides a polished experience out of the box.

#### Acceptance Criteria

1. THE macOS theme SHALL have a default background pattern defined in THEME_DEFAULT_PATTERN
2. THE macOS theme SHALL have frosted glass effect enabled by default in THEME_DEFAULT_FROSTED
3. THE macOS theme default pattern SHALL be "none" or a subtle pattern that complements the light color scheme
4. WHEN the macOS theme is applied, THE Theme_System SHALL automatically enable the frosted glass effect without user intervention

### Requirement 4: Font Stack Fallback Chain

**User Story:** As a developer, I want the macOS font to have proper fallbacks, so that users on non-Apple platforms see appropriate alternative fonts.

#### Acceptance Criteria

1. THE macOS font stack SHALL include system-ui as a fallback after SF Pro
2. THE macOS font stack SHALL include -apple-system as a fallback for older Apple devices
3. THE macOS font stack SHALL include BlinkMacSystemFont as a fallback for Chrome on macOS
4. THE macOS font stack SHALL include a generic sans-serif as the final fallback
5. THE font stack order SHALL prioritize fonts that most closely match SF Pro's appearance
