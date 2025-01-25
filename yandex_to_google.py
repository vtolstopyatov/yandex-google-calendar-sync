import base64

import requests


def handler(event, context):
    params = event.get('queryStringParameters')
    response = requests.get(f'https://calendar.yandex.ru/export/ics.xml', params=params)
    content = response.content.decode()
    content = content.replace('CLASS:PRIVATE', 'CLASS:PUBLIC')
    content = base64.b64encode(content.encode())
    return {
        'statusCode': response.status_code,
        'body': content.decode(),
        'isBase64Encoded': True,
        'headers': {
            'Content-Type': 'text/calendar; charset=utf-8',
            'Content-Disposition': 'attachment; filename=calendar.ics',
        }
    }
