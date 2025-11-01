"""
Configuration management for webl CLI
"""
import os
import json
from pathlib import Path


class Config:
    """Manages webl configuration and API key storage"""

    def __init__(self):
        self.config_dir = Path.home() / '.config' / 'webl'
        self.config_file = self.config_dir / 'config.json'
        self._ensure_config_dir()

    def _ensure_config_dir(self):
        """Create config directory if it doesn't exist"""
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def get_api_key(self):
        """Get stored API key"""
        # Check environment variable first
        env_key = os.environ.get('WEBL_API_KEY')
        if env_key:
            return env_key

        # Check config file
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    return config.get('api_key')
            except (json.JSONDecodeError, IOError):
                return None

        return None

    def set_api_key(self, api_key):
        """Store API key in config file"""
        config = {}

        # Load existing config if it exists
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
            except (json.JSONDecodeError, IOError):
                pass

        # Update API key
        config['api_key'] = api_key

        # Save config
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)

        # Set restrictive permissions (user read/write only)
        os.chmod(self.config_file, 0o600)

    def get_config_path(self):
        """Get path to config file"""
        return str(self.config_file)
