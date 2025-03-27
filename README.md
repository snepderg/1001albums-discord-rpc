# 1001Albums Discord RPC
*\ ~ A Python project by Snepderg*

## About
1001Albums Discord RPC is a script that utilizes the `discord-rpc` Python API to show the status of your 1001 Albums project.

It shows the following about your oldest unrated album:
(1001 Albums does not allow you to skip rating, only review.)
- Album Title and Artist
- Album artwork
- Rated Albums out of Total Generated Albums

## Dependencies
- **Python (3.8.8):**
    - [Discord RPC](https://pypi.org/project/discord-rpc/)
    - [python-dotenv](https://pypi.org/project/python-dotenv/)
    - [Requests](https://pypi.org/project/requests/)
- **Applications**
    - [Discord Client with Dev Application](https://discord.com/developers/applications)
    - [1001 Albums Account](https://1001albumsgenerator.com/)

## Installation
1. Download from source or from Releases
2. Unzip the folder
3. Run the included `start.bat` script
4. Fill out the `.env` config file
- You will need to create a Discord Application and store the token in the config file.
- You will need to create a 1001 Albums project and store the ID in the config file. I strongly recommend going to your summary page and copying that ID.
5. Run the `start.bat` script again
- NOTE: Currently only supports Windows, I might write an installer for other systems (But frankly it's pretty straightforward).

### Example .env Configuration
*The installer creates a blank.env*

```ini
# Your Discord Application ID (Create one at https://discord.com/developers/applications)
DISCORD_ACTIVITY_TOKEN=0938586491844541502

# Your 1001 Albums Project ID. Create one here:
# Create one at https://1001albumsgenerator.com/
# (Summary ID is recommended for security)
PROJECT_ID="xbhd3w19662a4la0t1u0ij3w"

# How many seconds between updates. If left blank will default to 300.
UPDATE_INTERVAL=300
```