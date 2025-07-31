from .Base import *
from typing import Dict, Optional, Union, List

class ChatRoomApi:
    def __init__(self):
        pass

    async def getGroupInfo(self, roomid: str, selfWxid: str) -> Optional[Dict]:
        """
        获取群信息
        :param roomid: 群ID
        :param selfWxid: 机器人ID
        :return: 群信息
        """
        try:
            data = {
                "Wxid": selfWxid,
                "QID": roomid
            }
            return await sendPostReq("Group/GetChatRoomInfo", data)
        except Exception as e:
            logger.error(f"获取群信息失败: {e}")
            return None

    async def getGroupInfoDetail(self, roomid: str, selfWxid: str) -> Optional[Dict]:
        """
        获取群详细信息
        :param roomid: 群ID
        :param selfWxid: 机器人ID
        :return: 群详细信息
        """
        try:
            data = {
                "Wxid": selfWxid,
                "QID": roomid
            }
            return await sendPostReq("Group/GetChatRoomInfoDetail", data)
        except Exception as e:
            logger.error(f"获取群详细信息失败: {e}")
            return None

    async def getGroupMemberInfos(self, roomid: str, selfWxid: str) -> Optional[Dict]:
        """
        获取群成员信息
        :param roomid: 群ID
        :param selfWxid: 机器人ID
        :return: 群成员信息
        """
        try:
            data = {
                "Wxid": selfWxid,
                "QID": roomid
            }
            return await sendPostReq("Group/GetChatRoomMemberDetail", data)
        except Exception as e:
            logger.error(f"获取群成员信息失败: {e}")
            return None

    async def inviteMember(self, roomid: str, towxid: str, selfWxid: str) -> Optional[Dict]:
        """
        邀请成员加入群
        :param roomid: 群ID
        :param towxid: 要邀请的成员ID或ID列表
        :param selfWxid: 机器人ID
        :return: 邀请结果
        """
        try:

            data = {
                "ChatRoomName": roomid,
                "ToWxids": towxid,
                "Wxid": selfWxid
            }
            return await sendPostReq("Group/InviteChatRoomMember", data)
        except Exception as e:
            logger.error(f"邀请成员失败: {e}")
            return None

    async def deleteMember(self, roomid: str, towxid: Union[str, List[str]], selfWxid: str) -> Optional[Dict]:
        """
        从群中删除成员
        :param roomid: 群ID
        :param towxid: 要删除的成员ID或ID列表
        :param selfWxid: 机器人ID
        :return: 删除结果
        """
        try:
            # 如果是单个wxid，转换为列表
            if isinstance(towxid, str):
                member_list = [towxid]
            else:
                member_list = towxid

            data = {
                "ChatRoomName": roomid,
                "ToWxids": member_list,
                "Wxid": selfWxid
            }
            return await sendPostReq("Group/DelChatRoomMember", data)
        except Exception as e:
            logger.error(f"删除成员失败: {e}")
            return None

