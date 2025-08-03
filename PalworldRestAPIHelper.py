import requests
from requests import HTTPError
import base64
import json


class PalworldServerHelper:

    def __init__(self, server_url, server_admin_name, server_admin_password):
        self.server_url = server_url
        self.credentials = f'{server_admin_name}:{server_admin_password}'
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'Basic {str(base64.b64encode(self.credentials.encode()).decode())}'
        }

    def __base_request(self, endpoint, payload=None, method="GET") -> dict:
        try:
            if payload:
                response = requests.request(method,
                                            url=f'{self.server_url}/{endpoint}',
                                            headers=self.headers,
                                            data=payload,
                                            timeout=30)
            else:
                response = requests.request(method,
                                            url=f'{self.server_url}/{endpoint}',
                                            headers=self.headers,
                                            timeout=30)

            response.raise_for_status()
            if "application/json" in response.headers.get("Content-Type", ""):
                return response.json()

            else: return {"Response": response.text}

        except HTTPError as e:
            return {"Error": f'Http Error - {e}'}

        except Exception as e:
            return {
                "Error": "There was a problem with your request. Check the logs for more info.",
                "Details": e
            }

    def get_server_info(self) -> dict:
        """
        Returns a dictionary with version, servername, description, and worldguid.

        Example:
            {
              "version": "v0.1.5.0",
              "servername": "Palworld example Server",
              "description": "This is a Palworld server.",
              "worldguid": "A7E97BAA767DB9029EF013BB71E993A0"
            }
        """

        try:
            server_info = self.__base_request("info")
            return server_info

        except Exception as e:
            return {
                "Error": "There was a problem with your request. Check the logs for more info.",
                "Details": e
            }

    def get_player_list(self) -> list[dict]:
        """

        Returns a list of players.

        Example:
        [
            {
              "name": "PalUser",
              "accountName": "paluser",
              "playerId": "AFAFD830000000000000000000000000",
              "userId": "steam_00000000000000000",
              "ip": "127.0.0.1",
              "ping": 3.14,
              "location_x": 123.45,
              "location_y": 67.89,
              "level": 1,
              "building_count": 119
            }
        ]
        """

        try:
            player_list = self.__base_request("players")
            return player_list.get("players")

        except Exception as e:
            return [{
                "Error": "There was a problem with your request. Check the logs for more info.",
                "Details": e
            }]

    def get_server_settings(self) -> dict:
        """
         Returns a dictionary containing the server's current settings.

         Example:
         {
           "Difficulty": "string",
           "DayTimeSpeedRate": 0,
           "NightTimeSpeedRate": 0,
           "ExpRate": 0,
           "PalCaptureRate": 0,
           "PalSpawnNumRate": 0,
           "PalDamageRateAttack": 0,
           "PalDamageRateDefense": 0,
           "PlayerDamageRateAttack": 0,
           "PlayerDamageRateDefense": 0,
           "PlayerStomachDecreaceRate": 0,
           "PlayerStaminaDecreaceRate": 0,
           "PlayerAutoHPRegeneRate": 0,
           "PlayerAutoHpRegeneRateInSleep": 0,
           "PalStomachDecreaceRate": 0,
           "PalStaminaDecreaceRate": 0,
           "PalAutoHPRegeneRate": 0,
           "PalAutoHpRegeneRateInSleep": 0,
           "BuildObjectDamageRate": 0,
           "BuildObjectDeteriorationDamageRate": 0,
           "CollectionDropRate": 0,
           "CollectionObjectHpRate": 0,
           "CollectionObjectRespawnSpeedRate": 0,
           "EnemyDropItemRate": 0,
           "DeathPenalty": "string",
           "bEnablePlayerToPlayerDamage": true,
           "bEnableFriendlyFire": true,
           "bEnableInvaderEnemy": true,
           "bActiveUNKO": true,
           "bEnableAimAssistPad": true,
           "bEnableAimAssistKeyboard": true,
           "DropItemMaxNum": 0,
           "DropItemMaxNum_UNKO": 0,
           "BaseCampMaxNum": 0,
           "BaseCampWorkerMaxNum": 0,
           "DropItemAliveMaxHours": 0,
           "bAutoResetGuildNoOnlinePlayers": true,
           "AutoResetGuildTimeNoOnlinePlayers": 0,
           "GuildPlayerMaxNum": 0,
           "PalEggDefaultHatchingTime": 0,
           "WorkSpeedRate": 0,
           "bIsMultiplay": true,
           "bIsPvP": true,
           "bCanPickupOtherGuildDeathPenaltyDrop": true,
           "bEnableNonLoginPenalty": true,
           "bEnableFastTravel": true,
           "bIsStartLocationSelectByMap": true,
           "bExistPlayerAfterLogout": true,
           "bEnableDefenseOtherGuildPlayer": true,
           "CoopPlayerMaxNum": 0,
           "ServerPlayerMaxNum": 0,
           "ServerName": "string",
           "ServerDescription": "string",
           "PublicPort": 0,
           "PublicIP": "string",
           "RCONEnabled": true,
           "RCONPort": 0,
           "Region": "string",
           "bUseAuth": true,
           "BanListURL": "string",
           "RESTAPIEnabled": true,
           "RESTAPIPort": 0,
           "bShowPlayerList": true,
           "AllowConnectPlatform": "string",
           "bIsUseBackupSaveData": true,
           "LogFormatType": "string"
     }
         """

        try:
            server_settings = self.__base_request("settings")
            return server_settings

        except Exception as e:
            return {
                "Error": "There was a problem with your request. Check the logs for more info.",
                "Details": e
            }

    def get_server_metrics(self) -> dict:
        """
        Returns a dict of the current server metrics.

        Example:
            {
              "serverfps": 57,
              "currentplayernum": 10,
              "serverframetime": 16.7671,
              "maxplayernum": 32,
              "uptime": 3600,
              "days": 1
            }
        """

        try:
            server_metrics = self.__base_request("metrics")
            return server_metrics

        except Exception as e:
            return {
                "Error": "There was a problem with your request. Check the logs for more info.",
                "Details": e
            }

    def announce_message(self,message_in: str) -> dict:
        """
        Returns response in dict {Response: "results"}
        """

        try:
            payload = json.dumps({"message": message_in})
            response = self.__base_request("announce", payload=payload, method="POST")
            return response

        except Exception as e:
            return {"Error": "Error occurred. Check logs for more details."}

    def kick_player(self, user_id, message) -> dict:
        """
        Returns response in dict {Response: "results"}
        """

        try:
            payload = json.dumps({
                "userid": user_id,
                "message": message
            })
            response = self.__base_request("kick", payload=payload, method="POST")
            return response

        except Exception as e:
            return {"Error": "Error occurred. Check logs for more details."}

    def ban_player(self, user_id, message) -> dict:
        """
        Returns response in dict {Response: "results"}
        """

        try:
            payload = json.dumps({
                "userid": user_id,
                "message": message
            })
            response = self.__base_request("ban", payload=payload, method="POST")
            return response

        except Exception as e:
            return {"Error": "Error occurred. Check logs for more details."}

    def unban_player(self, user_id) -> dict:
        """
        Returns response in dict {Response: "results"}
        """

        try:
            payload = json.dumps({
                "userid": user_id,
            })
            response = self.__base_request("unban", payload=payload, method="POST")
            return response

        except Exception as e:
            return {"Error": "Error occurred. Check logs for more details."}

    def save_world(self) -> dict:
        """
        Returns response in dict {Response: "results"}
        """

        try:
            save_result = self.__base_request("save", method="POST")
            return save_result

        except Exception as e:
            return {
                "Error": "There was a problem with your request. Check the logs for more info.",
                "Details": e
            }

    def shutdown_server(self, wait_time, message) -> dict:
        """
        Returns response in dict {Response: "results"}
        """

        try:
            payload = {
                "waittime": wait_time,
                "message": message
            }
            shutdown_result = self.__base_request("shutdown", payload=payload, method="POST")
            return shutdown_result

        except Exception as e:
            return {
                "Error": "There was a problem with your request. Check the logs for more info.",
                "Details": e
            }

    def force_stop_server(self, wait_time, message) -> dict:
        """
        Returns response in dict {Response: "results"}
        """

        try:
            payload = {
                "waittime": wait_time,
                "message": message
            }
            stop_result = self.__base_request("save", payload=payload, method="POST")
            return stop_result

        except Exception as e:
            return {
                "Error": "There was a problem with your request. Check the logs for more info.",
                "Details": e
            }

