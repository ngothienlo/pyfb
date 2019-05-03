#!/usr/bin/env python
from pyfb import Pyfb
from utils import Json2ObjectsFactory

# Your APP ID. It Needs to register your application on facebook
# http://developers.facebook.com/
FACEBOOK_APP_ID = '1579990812132101'

facebook = Pyfb(FACEBOOK_APP_ID)

# Opens a new browser tab instance and authenticates with the facebook API
# It redirects to an url like
# http://www.facebook.com/connect
# /login_success.html#access_token=[access_token]&expires_in=0
# facebook.authenticate()

# Copy the [access_token] and enter it below
import pdb;pdb.set_trace()
token = 'EAAWcZCkcbAwUBALImPDi4vzb1C7Obg4nrx5WkbSYmhiI2uFKCLxk7pUvROOLKb9i8cUYxLwYIpY8y1YPjexHSmXakJO4l6ibNEZAwChsZBa48s9Jd7cZAghTkjvfDriGf3BsE0mH9s0xFwUeDbuUos5jI9xTCvclWCsJIwa8uo5yZAmMnDExf'


DATA_DEMO = {
  "messages": {
    "data": [
      {
        "message": "",
        "created_time": "2019-04-24T10:38:15+0000",
        "from": {
          "name": "Chin TestAccount",
          "email": "2638780562860568@facebook.com",
          "id": "2638780562860568"
        },
        "id": "m_xdhP2WqFgU8jYWZLaRNfWYKajei6LuiF7_iRWS8ER8CuyNni3-bkqgFhaNzdRKGDWd4WD_penNkLvv6o574kwg",
        "sticker": "https://scontent.xx.fbcdn.net/v/t39.1997-6/851586_126362170881913_763579892_n.png?_nc_cat=1&_nc_ht=scontent.xx&oh=d0e76dd6d634f3d67b19dcc09dc3d1a5&oe=5D3405AF",
        "tags": {
          "data": [
            {
              "name": "inbox"
            },
            {
              "name": "read"
            },
            {
              "name": "source:chat"
            }
          ]
        },
        "to": {
          "data": [
            {
              "name": "CHIN TEST PAGE API",
              "email": "541964686328018@facebook.com",
              "id": "541964686328018"
            }
          ]
        }
      },
      {
        "message": "",
        "created_time": "2019-04-24T10:38:02+0000",
        "from": {
          "name": "CHIN TEST PAGE API",
          "email": "541964686328018@facebook.com",
          "id": "541964686328018"
        },
        "id": "m_ddS3pvFGX7L_NLM3r3fZSoKajei6LuiF7_iRWS8ER8CA1d1Lq9EwgZX88lMgiXUCd0TiwjqoB9yZoSrFNICBaA",
        "sticker": "https://scontent.xx.fbcdn.net/v/t39.1997-6/10333121_823251601027151_1582826135_n.png?_nc_cat=1&_nc_ht=scontent.xx&oh=c453a805431564e42f090e90b58bf6bb&oe=5D746F01",
        "tags": {
          "data": [
            {
              "name": "inbox"
            },
            {
              "name": "read"
            },
            {
              "name": "sent"
            },
            {
              "name": "source:web"
            }
          ]
        },
        "to": {
          "data": [
            {
              "name": "Chin TestAccount",
              "email": "2638780562860568@facebook.com",
              "id": "2638780562860568"
            }
          ]
        }
      },
      {
        "message": "Đây chỉ là fanpage thử nghiệm, bạn vui lòng tìm chỗ khác mua nha. Cảm ơn bạn.",
        "created_time": "2019-04-24T10:37:25+0000",
        "from": {
          "name": "CHIN TEST PAGE API",
          "email": "541964686328018@facebook.com",
          "id": "541964686328018"
        },
        "id": "m_MMFfOwtZMPd4fiztFC1mUYKajei6LuiF7_iRWS8ER8DcH3rvS4LYbqv-qDmor-GVtDKtFSgGr3kwKy14C0AERQ",
        "tags": {
          "data": [
            {
              "name": "inbox"
            },
            {
              "name": "read"
            },
            {
              "name": "sent"
            },
            {
              "name": "source:web"
            }
          ]
        },
        "to": {
          "data": [
            {
              "name": "Chin TestAccount",
              "email": "2638780562860568@facebook.com",
              "id": "2638780562860568"
            }
          ]
        }
      },
      {
        "message": "Tôi muốn mua 100l sữa nhé",
        "created_time": "2019-04-24T10:36:41+0000",
        "from": {
          "name": "Chin TestAccount",
          "email": "2638780562860568@facebook.com",
          "id": "2638780562860568"
        },
        "id": "m_nwP8003rvi9YxsOaiuSkDYKajei6LuiF7_iRWS8ER8Ab6hzNk9XCuJf7h2-YuEQuO72kS0g4sBg3zZ6GCF0pLw",
        "tags": {
          "data": [
            {
              "name": "inbox"
            },
            {
              "name": "read"
            },
            {
              "name": "source:chat"
            }
          ]
        },
        "to": {
          "data": [
            {
              "name": "CHIN TEST PAGE API",
              "email": "541964686328018@facebook.com",
              "id": "541964686328018"
            }
          ]
        }
      },
      {
        "message": "Chào Chin, Bạn cần gì ?",
        "created_time": "2019-04-24T10:36:14+0000",
        "from": {
          "name": "CHIN TEST PAGE API",
          "email": "541964686328018@facebook.com",
          "id": "541964686328018"
        },
        "id": "m_EYuv36PgrCemGYEnCzmOg4Kajei6LuiF7_iRWS8ER8Bzd_-HXQ3RpGtA00C33lwqy91ytPyEkh8hSvN_ToirRw",
        "tags": {
          "data": [
            {
              "name": "inbox"
            },
            {
              "name": "read"
            },
            {
              "name": "sent"
            },
            {
              "name": "source:web"
            }
          ]
        },
        "to": {
          "data": [
            {
              "name": "Chin TestAccount",
              "email": "2638780562860568@facebook.com",
              "id": "2638780562860568"
            }
          ]
        }
      },
      {
        "message": "Chào Shop",
        "created_time": "2019-04-24T10:35:45+0000",
        "from": {
          "name": "Chin TestAccount",
          "email": "2638780562860568@facebook.com",
          "id": "2638780562860568"
        },
        "id": "m_7_uplzgGrJ-indxTTwpBsIKajei6LuiF7_iRWS8ER8Clrp5TwJQb_51nTbk-PDbFLKMK0tduy-R7aaGaBO8zbg",
        "tags": {
          "data": [
            {
              "name": "inbox"
            },
            {
              "name": "read"
            },
            {
              "name": "source:chat"
            }
          ]
        },
        "to": {
          "data": [
            {
              "name": "CHIN TEST PAGE API",
              "email": "541964686328018@facebook.com",
              "id": "541964686328018"
            }
          ]
        }
      }
    ],
    "paging": {
      "cursors": {
        "before": "QVFIUmUxY0dPYm9xTVJETUdzcUNGd2xtWEJFQTBjSWlWaWdJT1A3bU5zY2I3LWh5VzM5WnFSa1BMUnQ0WFpCajg3ZA1NvbXUxOTJqUGpuWEpWbGRBNW1JSkIwXzN6YW9MZAHZASYkhMRktZAZADlyWjRXVVg1MVllNXBLT2dWVnowVFlxRHRD",
        "after": "QVFIUkdqOXJDLW1XdjU5elN3OWhEZAlNYaV9FU0MzbEFCQUgyWVZAnM29ocDR6ay04bjYwS25pWkF5SFhxTTRERXoycWpYcFg4eno5V1l6ejJ2Uk5xUjFWMm9ONHhiNUp1eHVrUWZAnUHhVTGZArdVZAYVENtZAEdXeUgwUDFDb2F2QjVDS0VT"
      }
    }
  },
  "message_count": 6,
  "senders": {
    "data": [
      {
        "name": "Chin TestAccount",
        "email": "2638780562860568@facebook.com",
        "id": "2638780562860568"
      },
      {
        "name": "CHIN TEST PAGE API",
        "email": "541964686328018@facebook.com",
        "id": "541964686328018"
      }
    ]
  },
  "unread_count": 0,
  "updated_time": "2019-04-24T10:38:15+0000",
  "participants": {
    "data": [
      {
        "name": "Chin TestAccount",
        "email": "2638780562860568@facebook.com",
        "id": "2638780562860568"
      },
      {
        "name": "CHIN TEST PAGE API",
        "email": "541964686328018@facebook.com",
        "id": "541964686328018"
      }
    ]
  },
  "link": "/CHIN-TEST-PAGE-API-541964686328018/inbox/542111299646690/",
  "is_subscribed": True,
  "can_reply": True,
  "former_participants": {
    "data": [
    ]
  },
  "id": "t_888909208120764",
  "scoped_thread_key": "t_888909208120764",
  "snippet": "Chin sent a sticker."
}

factory = Json2ObjectsFactory()

# Sets the authentication token
facebook.set_access_token(token)

# Gets info about myself
# result = facebook.get_myself()
result = factory.make_objects_list('conversations', [DATA_DEMO])


def print_info(fb_object):
    object_attrs = get_fb_attrs_from_object(fb_object)
    for attr in object_attrs:
        data = getattr(fb_object, attr)
        if type(data) is list:
            for data_child in data:
                print_info(data_child)
        elif getattr(data, '__name__', False):
            print_info(data)
        else:
            print('%s ---------> %s' % (attr, data))


def get_fb_attrs_from_object(fb_object):
    data_attrs = filter(lambda field: '__' not in field, dir(fb_object))
    return list(data_attrs)


print("-" * 40)
print()
if isinstance(result, list):
    for data in result:
        print_info(data)
else:
    print_info(result)
print()
print("-" * 40)
