
import requests
def send_requests(method, url, headers, data=None):
    """
    method: {"GET", "POST", "PATCH", "DELETE"}
    """
    try:
        if method == "GET":
            res = requests.get(url, headers=headers)
        elif method == "POST":
            res = requests.post(url, json=data, headers=headers)
        elif method == "PATCH":
            res = requests.patch(url, json=data, headers=headers)
        elif method == "DELETE":
            res = requests.delete(url, headers=headers)
        res.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
    return res
