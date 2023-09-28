# Microsoft Teams Bot Integration

## Overview
<p align="justify">
The main idea of this project is creating a bot in Python for Microsoft Teams 
using Microsoft Bot Framework.

The bot is implemented as an "Echo" service: when a user posts a message 
in the chat, the bot captures the message and post a copy of it 
back to the same chat. Essentially, it echoes the user's message.

The bot application is packaged in a Docker container.
There is also created a web service for a bot to be able to post a random message 
when called via an API, and the bot is attached to a specific chat in Microsoft Teams.
</p>


## How to run
### To use this project locally you need:

**Step 1. Clone the repository and enter the root directory.**
```bash
git clone https://github.com/VoorheesDev/msTeams_Bot.git
cd msTeams_Bot
```

**Step 2. Register on [portal.azure.com](https://portal.azure.com/)**

**Step 3. Look for a service called "Azure Bot" and [create a new bot](https://portal.azure.com/#create/Microsoft.AzureBot)**

**Step 4. Add Microsoft Teams channel to your bot service.**

+ Open "**Channels**" section and add "**Microsoft Teams**".

**Step 5. Obtain the APP_ID and create the APP_PASSWORD.**

+ At the "**configuration**" section of the created bot service 
use a "**Manage Password**" link (next to "**Microsoft App ID**") to generate
a new secret key.

**Step 6. Configure the runtime environment of the project.**

+ Environmental data is set up via .ENV file. Create ".env" file in the root 
directory of a project (next to the Dockerfile). 
The file must include the following info:

```env
APP_ID=
APP_PASSWORD=
CONVERSATION_ID=
```

**Step 7. Upload your app in Teams**
+ [Sideload your app in Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/apps-upload): upload a manifest schema ([sample](https://learn.microsoft.com/en-us/microsoftteams/platform/resources/schema/manifest-schema#sample-app-manifest))

    or

+ [Publish app to your organization](https://learn.microsoft.com/en-us/MicrosoftTeams/manage-apps?toc=%2Fmicrosoftteams%2Fplatform%2Ftoc.json&bc=%2Fmicrosoftteams%2Fbreadcrumb%2Ftoc.json): 
register an app at [Teams Developer Portal](https://dev.teams.microsoft.com) 
and allow the app by admin at [admin.teams.com](https://admin.teams.microsoft.com/policies/manage-apps)

**Step 8. Start the project by running the following commands:**

```bash
docker-compose build
docker-compose up
```

+ After run, by default Ngrok UI will be available at 
http://localhost:4040 where you will find your public URL 
assigned by ngrok. Copy the public https link.

**Step 8. Set the messaging endpoint**

+ Navigate to "**configuration**" section of your bot at [portal.azure.com](https://portal.azure.com/) 
and fill in the "**Messaging endpoint**" field with the copied 
public https link followed by "**/api/messages**".
+ Apply changes at the bottom of the page.


**(Optional)Step 9. Send hello message to a specific conversation.**

+ Set a "**CONVERSATION_ID**" in .env file.
+ Make a POST request to http://localhost:3978/api/notify
