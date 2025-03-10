# Installation & Setup

## Requirements
Ensure you have the following dependencies installed:

```plaintext
certifi==2025.1.31
charset-normalizer==3.4.1
discord-rpc==5.1
dotenv==0.9.9
idna==3.10
python-dotenv==1.0.1
requests==2.32.3
urllib3==2.2.3
```

## Environment Configuration
Create a `.env` file in your project directory with the following variables:

```ini
# Your Discord Application ID (Create one at https://discord.com/developers/applications)
DISCORD_CLIENT_ID=1346979281963847772

# Your 1001 Albums Project URL (Summary ID is recommended for stability)
# Create one at https://1001albumsgenerator.com/
PROJECT_ID="67aa667485b7ba37e8af0608"

# Update interval in seconds
UPDATE_INTERVAL=3600
```

## Important Notes
- **Avoid upgrading `pip`** within the virtual environment, as it may cause corruption.
  - The exact cause is still under investigation.