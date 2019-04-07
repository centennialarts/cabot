Welcome to the caBot wiki!

We will be updated the purpose and features of the caBot here.

Supported in Python Version 3.x

# Module Dependencies

pip install irc
pip install requests

# Structure

## Command Modules

These are modules that pass commands into the bot for processing

### Currently Integrated Command Modules

#### Twitch IRC
https://dev.twitch.tv/docs/irc/guide/

OAuth Key can be obtained at https://twitchapps.com/tmi/

## Backend Modules

These are modules that register commands to act on and provide the backend integrations for the module's specific integrations. The can be anything from an asyncrounous RESTful API call or an active TCP Socket for realtime actions.

### Currently Integrated Backend Modules

#### Twitch API
https://dev.twitch.tv/docs/v5

App credentials can be obtained at https://glass.twitch.tv/console/apps

Integration specifications are outlined at https://dev.twitch.tv/docs/authentication/. We will work on rolling forwards the API support to the new Bearer token method.

# Future Modules

* RESTful API as Command Module
https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
