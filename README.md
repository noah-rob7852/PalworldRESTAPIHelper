# PalworldRESTAPIHelper


**PalworldRESTAPIHelper** is a Python module designed to simplify interaction with the Palworld REST API. It wraps common server commands such as retrieving server info, managing players, sending announcements, and controlling the server lifecycle.

**_When instantiating this class, you will need to specify 3 arguments:_**

**server_url** - The URL of the Rest API for the palworld server. Formatted like http://localhost:7000/v1/api

**server_admin_name** - usually "admin". 

server_admin_pass - The admin password for the server.



<h2>Features</h2>
- Fetch server info, metrics, and settings
- Get a list of connected players
- Send global announcements
- Kick, ban, and unban players
- Save the world state
- Gracefully or forcefully shut down the server


<h2>Methods</h2>

_Server Info & Status_
- get_server_info(): Returns version, server name, description, and world GUID.
- get_server_metrics(): Returns metrics like player count, uptime, and FPS.
- get_server_settings(): Returns the current server configuration.

_Player Management_
- get_player_list(): Returns a list of currently connected players.
- kick_player(user_id: str, message: str): Kicks a player with a custom message.
- ban_player(user_id: str, message: str): Bans a player with a custom message.
- unban_player(user_id: str): Unbans a previously banned player.

_Server Control_
- announce_message(message: str): Sends a broadcast message to all players.
- save_world(): Saves the current state of the world.
- shutdown_server(wait_time: int, message: str): Gracefully shuts down the server after a delay.
- force_stop_server(wait_time: int, message: str): Forces the server to stop (actually calls the save endpoint—consider reviewing this).

