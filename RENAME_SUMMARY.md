# Global Rename: Odysseus → AVA

## Summary

Successfully renamed all occurrences of "Odysseus" to "AVA" throughout the entire project.

## Changes Made

### 1. Content Replacements (237 files modified)
- **ODYSSEUS** → **AVA** (all uppercase)
- **Odysseus** → **AVA** (title case to all caps)
- **odysseus** → **ava** (all lowercase)

### 2. File Renames
- `odysseus-ui.service` → `ava-ui.service`
- `scripts/odysseus` → `scripts/ava`
- `scripts/odysseus-*` → `scripts/ava-*` (all CLI scripts)
- `integrations/claude/skills/odysseus/` → `integrations/claude/skills/ava/`
- `integrations/codex/skills/odysseus/` → `integrations/codex/skills/ava/`
- `docs/odysseus.jpg` → `docs/ava.jpg`

### 3. Environment Variables
All environment variables have been renamed:
- `ODYSSEUS_ADMIN_USER` → `AVA_ADMIN_USER`
- `ODYSSEUS_ADMIN_PASSWORD` → `AVA_ADMIN_PASSWORD`
- `ODYSSEUS_INPROCESS_POLLERS` → `AVA_INPROCESS_POLLERS`
- `ODYSSEUS_INPROCESS_TASKS` → `AVA_INPROCESS_TASKS`
- `ODYSSEUS_SCRIPT_HOST` → `AVA_SCRIPT_HOST`
- `ODYSSEUS_CHAT_UPLOAD_MAX_BYTES` → `AVA_CHAT_UPLOAD_MAX_BYTES`
- `ODYSSEUS_GALLERY_UPLOAD_MAX_BYTES` → `AVA_GALLERY_UPLOAD_MAX_BYTES`
- `ODYSSEUS_GALLERY_TRANSFORM_UPLOAD_MAX_BYTES` → `AVA_GALLERY_TRANSFORM_UPLOAD_MAX_BYTES`
- `ODYSSEUS_MEMORY_IMPORT_MAX_BYTES` → `AVA_MEMORY_IMPORT_MAX_BYTES`
- `ODYSSEUS_PERSONAL_UPLOAD_MAX_BYTES` → `AVA_PERSONAL_UPLOAD_MAX_BYTES`
- `ODYSSEUS_EMAIL_COMPOSE_UPLOAD_MAX_BYTES` → `AVA_EMAIL_COMPOSE_UPLOAD_MAX_BYTES`
- `ODYSSEUS_STT_MAX_AUDIO_BYTES` → `AVA_STT_MAX_AUDIO_BYTES`
- `ODYSSEUS_ICS_MAX_BYTES` → `AVA_ICS_MAX_BYTES`
- `ODYSSEUS_DATA_DIR` → `AVA_DATA_DIR`
- `ODYSSEUS_MAIL_ATTACHMENTS_DIR` → `AVA_MAIL_ATTACHMENTS_DIR`
- `ODYSSEUS_INTERNAL_BASE` → `AVA_INTERNAL_BASE`
- `ODYSSEUS_HOST` → `AVA_HOST`
- `ODYSSEUS_PORT` → `AVA_PORT`
- `ODYSSEUS_COPILOT_CLIENT_ID` → `AVA_COPILOT_CLIENT_ID`
- `ODYSSEUS_COPILOT_API_VERSION` → `AVA_COPILOT_API_VERSION`
- `ODYSSEUS_COPILOT_USER_AGENT` → `AVA_COPILOT_USER_AGENT`
- `ODYSSEUS_COPILOT_INTEGRATION_ID` → `AVA_COPILOT_INTEGRATION_ID`
- `ODYSSEUS_COPILOT_EDITOR_VERSION` → `AVA_COPILOT_EDITOR_VERSION`

### 4. Docker & Service Names
- Docker service: `odysseus` → `ava`
- Docker logs: `docker compose logs odysseus` → `docker compose logs ava`
- Container references throughout docker-compose files

### 5. Code References
- Python imports, function names, and comments
- JavaScript variables and strings
- HTML content and meta tags
- Documentation (README.md, CONTRIBUTING.md, etc.)
- Test files
- Configuration files
- Shell scripts

### 6. URLs & References
- GitHub repository references: `copyrightnews/AVA` → `copyrightnews/AVA`
- Documentation URLs
- Internal API references

## Files Excluded from Processing
- `.git/` directory
- `__pycache__/` directories
- `node_modules/` (if any)
- `venv/` and `.venv/` directories
- `data/` directory (user data)
- `logs/` directory

## Next Steps

### Required Manual Actions:
1. **Rename root directory**: Rename the project folder from `odysseus` to `ava`
2. **Update git remote** (if needed):
   ```bash
   git remote set-url origin https://github.com/copyrightnews/AVA.git
   ```
3. **Update .env file**: If you have a `.env` file, update any `ODYSSEUS_*` variables to `AVA_*`
4. **Restart services**: If Docker is running, recreate containers:
   ```bash
   docker compose down
   docker compose up -d --build
   ```
5. **Test the application**: Verify everything works after the rename

### Verification Checklist:
- [ ] Application starts successfully
- [ ] All features work as expected
- [ ] Docker services start correctly
- [ ] CLI scripts execute properly
- [ ] Environment variables are recognized
- [ ] Database connections work
- [ ] Documentation renders correctly

## Notes
- The rename was case-sensitive and comprehensive
- All text content, code, and configuration files were processed
- Binary files and data directories were intentionally excluded
- The application structure and functionality remain unchanged

---

**Rename completed on**: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
**Total files processed**: 1009
**Total files modified**: 237
