#LINK : https://pypi.org/project/pyfcm/
# pip install pyfcm
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAANs-SMqY:APA91bFcdhIKXFdDpD007zjx2JphhTF5qF-pvsUR5abfSU74vF1lwUIAT8aX_5jDTci3rhQhGk26ue29fiDiIIJKdcR0HhcKeQNaCGt9UUYfpiNO6P_r7mgNselPQuQ6nu7d2pmhnikN")

# OR initialize with proxies

# proxy_dict = {
#           "http"  : "http://127.0.0.1",
#           "https" : "http://127.0.0.1",
#         }
# push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

# Send to single device.
# registration_id = "<device registration_id>"
#push_service.notify_single_device(registration_id=registration_id,);

# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# push_service.notify_multiple_devices(registration_ids=registration_ids,)

registration_ids = ["c6CmtkKFSsepdreoi5zEV7:APA91bEbHpgYsut2nLinJoR9QTXvmlYRCiFJvxnZ0wg-IHcefUN_efr_6X5Hq8j-U-yjq_8a3mPD7Ojt6-yks67FhPGXu5lNjsmX7hd9P0u4yOdQK4bpQ0vVkBTXw5vZQlehlT0SDgyJ",]
message_title = "Message title"
message_body = "Message body"
data_message = {
    "Nick" : "Mario",
    "body" : "great match!",
    "Room" : "PortugalVSDenmark"
}
extra_notification_kwargs = {
    "image":  "https://d3po247hen37pb.cloudfront.net/echo-retail/echo-music-thumbnail/echo-us-en-18.png"
}
extra_kwargs = {
    'mutable_content': True
}
result = push_service.notify_multiple_devices(
    registration_ids=registration_ids,
    message_title=message_title,
    message_body=message_body,
    message_icon=None,
    sound=None,
    condition=None,
    collapse_key=None,
    delay_while_idle=False,
    time_to_live=None,
    restricted_package_name=None,
    low_priority=False,
    dry_run=False,
    data_message=None,
    click_action=None,
    badge=None,
    color=None,
    tag=None,
    body_loc_key=None,
    body_loc_args=None,
    title_loc_key=None,
    title_loc_args=None,
    content_available=True,
    extra_kwargs=extra_kwargs,
    extra_notification_kwargs=extra_notification_kwargs
)
print(result)