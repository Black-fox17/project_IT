curl --location 'http://localhost:8000/tick' \
--header 'Content-Type: application/json' \
--data '{
    "channel_id": "0195204d-4679-75ff-8d14-3fbed758cb3d",
    "return_url": "https://ping.telex.im/v1/return/0195204d-4679-75ff-8d14-3fbed758cb3d",
    "settings": [
        {
            "label": "site-1",
            "type": "text",
            "required": true,
            "default": "https://google.com"
        },
        {
            "label": "site-2",
            "default": "https://www.somefakewebsitethatisfake.com",
            "type": "text",
            "required": true
        },
        {
            "label": "interval",
            "type": "text",
            "required": true,
            "default": "* * * * *"
        }
    ]
}'